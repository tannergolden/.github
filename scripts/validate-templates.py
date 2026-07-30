#!/usr/bin/env python3
"""Validate the community health defaults this repository serves.

GitHub fails these files silently: a form with the wrong extension, the wrong
filename, or an unsupported category is dropped without an error anywhere. Every
check below exists because nothing else would catch the failure before it reached
every repository on the account.

Rules are grouped by where they come from:

  A. FILE NAMING     GitHub decides whether a file binds at all from its path.
  B. FORM SCHEMA     A subset of GitHub's documented issue-form validation errors.
  C. HOUSE RULES     Conventions this repository publishes and must itself keep.
  D. LINKS           Link forms that survive a default-branch rename.

Usage: python3 scripts/validate-templates.py [--quiet]
Exit status is 0 when every check passes and 1 when any ERROR is recorded.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - surfaced as a usage error, not a finding
    sys.exit("PyYAML is required: pip install pyyaml")

REPO = Path(__file__).resolve().parent.parent
ISSUE_DIR = REPO / ".github" / "ISSUE_TEMPLATE"
DISCUSSION_DIR = REPO / ".github" / "DISCUSSION_TEMPLATE"

# ---------------------------------------------------------------------------
# A. FILE NAMING
# ---------------------------------------------------------------------------

# "Issue templates created with issue forms need a .yml extension."
# https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates
# The discussion category form docs specify .github/DISCUSSION_TEMPLATE/FORM-NAME.yml.
REQUIRED_EXTENSION = ".yml"

# "The name must correspond with the slug for one of your discussion categories."
# https://docs.github.com/en/discussions/managing-discussions-for-your-community/creating-discussion-category-forms
#
# Slugs GitHub creates for every repository when Discussions is enabled. A form
# named for anything else only binds once someone creates a matching category.
STOCK_CATEGORY_SLUGS = {
    "announcements",
    "general",
    "ideas",
    "polls",
    "q-a",
    "show-and-tell",
}

# Slugs this account intends to serve. Stock slugs bind everywhere; custom slugs
# bind only in repositories that have created the category, which is a deliberate
# opt-in rather than an oversight. Adding a form means adding its slug here.
DECLARED_CATEGORY_SLUGS = {
    "announcements": "stock",
    "general": "stock",
    "ideas": "stock",
    "q-a": "stock",
    "show-and-tell": "stock",
    "accessibility": "custom",
    "internationalization-i18n": "custom",
    "roadmap": "custom",
    "tooling-setup": "custom",
}

# "Discussion category forms are not supported for polls."
# https://docs.github.com/en/discussions/managing-discussions-for-your-community/creating-discussion-category-forms
UNSUPPORTED_CATEGORY_SLUGS = {"polls"}

KEBAB_CASE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

# ---------------------------------------------------------------------------
# B. FORM SCHEMA
# ---------------------------------------------------------------------------

ISSUE_TOP_LEVEL_REQUIRED = {"name", "description", "body"}
ISSUE_TOP_LEVEL_PERMITTED = {
    "name",
    "description",
    "body",
    "title",
    "labels",
    "assignees",
    "projects",
    "type",
}
DISCUSSION_TOP_LEVEL_REQUIRED = {"body"}
DISCUSSION_TOP_LEVEL_PERMITTED = {"title", "labels", "body"}

BODY_TYPES = {"markdown", "textarea", "input", "dropdown", "checkboxes"}
ID_CHARSET = re.compile(r"^[A-Za-z0-9_-]+$")

# YAML 1.1 coerces these to booleans, which GitHub rejects in dropdown options.
# Detected in the source rather than after parsing: once loaded, a quoted 'Yes'
# and an unquoted Yes are both the string "Yes", and only the second is a bug.
UNQUOTED_BOOLEAN_OPTION = re.compile(
    r"^\s*-\s+(y|n|yes|no|true|false|on|off)\s*$", re.IGNORECASE
)

# ---------------------------------------------------------------------------
# C. HOUSE RULES
# ---------------------------------------------------------------------------

LABEL_PREFIX = re.compile(r"^(type|status|area): \S")

# Strings that name this account's own setup. A default renders inside
# repositories with different branches, stacks, and conventions.
ACCOUNT_SPECIFIC = [
    ("Development|Preview|Release", "names this account's branch scheme"),
]

# ---------------------------------------------------------------------------
# D. LINKS
# ---------------------------------------------------------------------------

# blob/HEAD follows the default branch; a pinned branch name breaks on rename.
BRANCH_PINNED_LINK = re.compile(r"github\.com/[^/\s)]+/[^/\s)]+/blob/(?!HEAD/)([^/\s)]+)/")


class Report:
    def __init__(self) -> None:
        self.errors: list[tuple[str, str]] = []
        self.notes: list[tuple[str, str]] = []

    def error(self, where: str, message: str) -> None:
        self.errors.append((where, message))

    def note(self, where: str, message: str) -> None:
        self.notes.append((where, message))


def rel(path: Path) -> str:
    return str(path.relative_to(REPO))


def line_of(path: Path, needle: str) -> int:
    """Best-effort 1-indexed line number for a substring, for actionable output."""
    try:
        for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if needle in line:
                return i
    except OSError:
        pass
    return 0


def form_files(directory: Path) -> list[Path]:
    if not directory.is_dir():
        return []
    return sorted(p for p in directory.iterdir() if p.is_file() and p.name != "config.yml")


# ---------------------------------------------------------------------------


def check_naming(report: Report) -> None:
    for path in form_files(ISSUE_DIR):
        if path.suffix != REQUIRED_EXTENSION:
            report.error(
                rel(path),
                f"issue forms need a '{REQUIRED_EXTENSION}' extension, found '{path.suffix}' "
                f"(GitHub documents .yml; .yaml is not documented as supported)",
            )
        if not KEBAB_CASE.match(path.stem):
            report.error(
                rel(path),
                f"filename stem '{path.stem}' is not kebab-case (CONTRIBUTING.md requires it)",
            )

    for path in form_files(DISCUSSION_DIR):
        if path.suffix != REQUIRED_EXTENSION:
            report.error(
                rel(path),
                f"discussion forms need a '{REQUIRED_EXTENSION}' extension, found '{path.suffix}'",
            )
        slug = path.stem
        if slug in UNSUPPORTED_CATEGORY_SLUGS:
            report.error(
                rel(path),
                f"'{slug}' can never render: discussion category forms are not supported for polls",
            )
        elif slug not in DECLARED_CATEGORY_SLUGS:
            near = " or ".join(sorted(STOCK_CATEGORY_SLUGS - set(DECLARED_CATEGORY_SLUGS)))
            hint = f"; unclaimed stock slugs: {near}" if near else ""
            report.error(
                rel(path),
                f"'{slug}' is not a declared category slug, so the form binds to nothing. "
                f"Add it to DECLARED_CATEGORY_SLUGS or rename it to the intended slug{hint}",
            )
        elif DECLARED_CATEGORY_SLUGS[slug] == "custom":
            report.note(rel(path), f"'{slug}' needs a custom category; it will not bind in a stock repository")

    config = ISSUE_DIR / "config.yml"
    if not config.exists():
        report.error(rel(ISSUE_DIR), "config.yml is missing; GitHub fixes this filename")
    if (ISSUE_DIR / "config.yaml").exists():
        report.error(rel(ISSUE_DIR / "config.yaml"), "the chooser config must be named config.yml exactly")


def check_body(path: Path, body: object, report: Report) -> None:
    where = rel(path)
    if not isinstance(body, list) or not body:
        report.error(where, "'body' must be a non-empty list")
        return

    ids: dict[str, int] = {}
    labels: dict[str, int] = {}
    has_field = False

    for index, item in enumerate(body):
        at = f"body[{index}]"
        if not isinstance(item, dict):
            report.error(where, f"{at} must be a mapping")
            continue

        kind = item.get("type")
        if kind not in BODY_TYPES:
            report.error(where, f"{at}: '{kind}' is not a valid input type")
            continue
        if kind != "markdown":
            has_field = True

        attributes = item.get("attributes")
        if not isinstance(attributes, dict):
            report.error(where, f"{at}: 'attributes' is required")
            continue

        if kind == "markdown":
            if not str(attributes.get("value", "")).strip():
                report.error(where, f"{at}: markdown requires a non-empty 'value'")
        else:
            label = str(attributes.get("label", "")).strip()
            if not label:
                report.error(where, f"{at}: required attribute 'label' is missing or empty")
            else:
                if label in labels:
                    report.error(where, f"{at}: duplicate label {label!r} (also body[{labels[label]}])")
                labels[label] = index

            item_id = item.get("id")
            if item_id is not None:
                item_id = str(item_id)
                if not ID_CHARSET.match(item_id):
                    report.error(where, f"{at}: id {item_id!r} may only contain letters, numbers, - and _")
                if item_id in ids:
                    report.error(where, f"{at}: duplicate id {item_id!r} (also body[{ids[item_id]}])")
                ids[item_id] = index

        if kind == "dropdown":
            options = attributes.get("options")
            if not isinstance(options, list) or not options:
                report.error(where, f"{at}: dropdown requires a non-empty 'options' list")
                continue
            seen: set[str] = set()
            for option in options:
                if isinstance(option, bool):
                    report.error(where, f"{at}: options must not include booleans (quote y/n/yes/no/on/off)")
                    continue
                text = str(option).strip()
                if not text:
                    report.error(where, f"{at}: options must not be empty")
                elif text.lower() == "none":
                    report.error(where, f"{at}: options must not include the reserved word 'none'")
                if text in seen:
                    report.error(where, f"{at}: duplicate option {text!r}")
                seen.add(text)

        if kind == "checkboxes":
            options = attributes.get("options")
            if not isinstance(options, list) or not options:
                report.error(where, f"{at}: checkboxes require a non-empty 'options' list")
                continue
            seen = set()
            for option in options:
                text = str(option.get("label", "")).strip() if isinstance(option, dict) else ""
                if not text:
                    report.error(where, f"{at}: every checkbox option needs a 'label'")
                elif text in seen:
                    report.error(where, f"{at}: duplicate checkbox label {text!r}")
                seen.add(text)

    if not has_field:
        report.error(where, "'body' must contain at least one non-markdown field")


def check_labels(path: Path, data: dict, report: Report) -> None:
    labels = data.get("labels")
    if labels is None:
        return
    if isinstance(labels, str):
        labels = [part.strip() for part in labels.split(",")]
    if not isinstance(labels, list):
        report.error(rel(path), "'labels' must be a list or a comma-delimited string")
        return
    for label in labels:
        if not LABEL_PREFIX.match(str(label)):
            report.error(
                rel(path),
                f"label {str(label)!r} is outside the shared taxonomy (expected 'type: ', 'status: ' or 'area: ')",
            )


def check_schema(report: Report) -> dict[Path, dict]:
    parsed: dict[Path, dict] = {}

    for path in form_files(ISSUE_DIR) + form_files(DISCUSSION_DIR):
        source = path.read_text(encoding="utf-8")
        for number, line in enumerate(source.splitlines(), 1):
            if UNQUOTED_BOOLEAN_OPTION.match(line):
                report.error(
                    f"{rel(path)}:{number}",
                    f"unquoted {line.strip().lstrip('- ')!r} is coerced to a boolean by YAML 1.1; quote it",
                )
        try:
            data = yaml.safe_load(source)
        except yaml.YAMLError as exc:
            report.error(rel(path), f"YAML does not parse: {exc}")
            continue
        if not isinstance(data, dict):
            report.error(rel(path), "top level must be a mapping")
            continue

        parsed[path] = data
        is_issue = path.parent == ISSUE_DIR
        required = ISSUE_TOP_LEVEL_REQUIRED if is_issue else DISCUSSION_TOP_LEVEL_REQUIRED
        permitted = ISSUE_TOP_LEVEL_PERMITTED if is_issue else DISCUSSION_TOP_LEVEL_PERMITTED

        for key in sorted(required - set(data)):
            report.error(rel(path), f"required top-level key '{key}' is missing")
        for key in sorted(set(data) - permitted):
            report.error(rel(path), f"'{key}' is not a permitted top-level key")

        check_body(path, data.get("body"), report)
        check_labels(path, data, report)

    return parsed


def check_cross_references(parsed: dict[Path, dict], report: Report) -> None:
    """Every mention of a form must carry that form's own name emoji.

    The forms cross-reference each other constantly ("Documentation issues -> use
    X Documentation Report"). When a form's name emoji and the emoji used to point
    at it drift apart, reporters follow the wrong signpost and nothing complains.
    """
    canonical: dict[str, str] = {}
    for path, data in parsed.items():
        if path.parent != ISSUE_DIR:
            continue
        name = str(data.get("name", "")).strip()
        emoji, _, title = name.partition(" ")
        if title:
            canonical[title.strip()] = emoji

    if not canonical:
        return

    titles = "|".join(re.escape(t) for t in sorted(canonical, key=len, reverse=True))
    idioms = [
        # Forms: "- Documentation issues -> use 📚 Documentation Report"
        re.compile(r"use\s+\*{0,2}(\S+?)\*{0,2}\s+\*{0,2}(" + titles + r")\b"),
        # SUPPORT.md routing table: "| A reproducible bug | 🐛 **Issues -> Bug Report** |"
        re.compile(r"\|\s*(\S+)\s+\*{0,2}(?:Issues|Discussions)\s+→\s+\*{0,2}(" + titles + r")\b"),
    ]

    for path in tracked_files():
        if path.suffix not in {".md", ".yml", ".yaml"} or not path.is_file():
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for idiom in idioms:
                for found, title in idiom.findall(line):
                    expected = canonical[title]
                    if found != expected:
                        report.error(
                            f"{rel(path)}:{number}",
                            f"points at {title!r} with {found!r}; that form's name uses {expected!r}",
                        )


def check_house_rules(parsed: dict[Path, dict], report: Report) -> None:
    for path in sorted(parsed):
        text = path.read_text(encoding="utf-8")
        for needle, why in ACCOUNT_SPECIFIC:
            if needle in text:
                report.error(f"{rel(path)}:{line_of(path, needle)}", f"{needle!r} {why}; keep defaults project-agnostic")


def tracked_files() -> list[Path]:
    out = subprocess.run(
        ["git", "-C", str(REPO), "ls-files"], capture_output=True, text=True, check=True
    ).stdout.split()
    return [REPO / name for name in out]


def check_whitespace(report: Report) -> None:
    for path in tracked_files():
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        offenders = [n for n, line in enumerate(text.splitlines(), 1) if line != line.rstrip()]
        if offenders:
            shown = ", ".join(str(n) for n in offenders[:5])
            more = f" (+{len(offenders) - 5} more)" if len(offenders) > 5 else ""
            report.error(rel(path), f"trailing whitespace on line(s) {shown}{more}")
        if text and not text.endswith("\n"):
            report.error(rel(path), "file does not end with a newline")


def check_links(report: Report) -> None:
    for path in tracked_files():
        if path.suffix not in {".md", ".yml", ".yaml"} or not path.is_file():
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for branch in BRANCH_PINNED_LINK.findall(line):
                report.error(
                    f"{rel(path)}:{number}",
                    f"link is pinned to branch '{branch}'; use 'blob/HEAD/' so it survives a rename",
                )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quiet", action="store_true", help="print only failures")
    args = parser.parse_args()

    report = Report()
    check_naming(report)
    parsed = check_schema(report)
    check_cross_references(parsed, report)
    check_house_rules(parsed, report)
    check_whitespace(report)
    check_links(report)

    if report.notes and not args.quiet:
        print("Notes")
        for where, message in report.notes:
            print(f"  {where}: {message}")
        print()

    if report.errors:
        print(f"FAIL  {len(report.errors)} error(s)")
        for where, message in report.errors:
            print(f"  {where}: {message}")
        return 1

    counted = len(parsed)
    if not args.quiet:
        print(f"OK  {counted} form(s) validated, no errors")
    return 0


if __name__ == "__main__":
    sys.exit(main())

<!--
title: '🩺 COMMUNITY HEALTH DEFAULTS'
description: 'How this repository serves account-wide default community health files to every repository on the account.'
tags: [community-health, defaults, dot-github]
category: docs
-->

<!-- markdownlint-disable MD041 -->

<div align="center">

# 🩺 COMMUNITY HEALTH DEFAULTS

<a name="top"></a>

**Account-wide defaults for contribution, governance, security, and support.**

_Write it once. Inherit it everywhere._

</div>

---

## 💡 What This Repository Is

GitHub gives a repository named **`.github`** a special job: any file it holds from a fixed,
documented list is served as the **default** for every other repository on this account that does
not ship its own copy.

Nothing here is application code, and nothing here builds. Apart from this README and the
`LICENSE`, every file in this repository exists to be served to other repositories, so a new
repository starts with a real code of conduct, a real security policy, and working issue forms on
day one, without copying a single file.

> [!IMPORTANT]
> **A repository's own file always wins.** These are fallbacks, not mandates. Drop a
> `CONTRIBUTING.md` into any repository and it immediately overrides the one here, for that
> repository only.

---

## 📦 What's Inside

| File                               | What it does                                                          |
| :--------------------------------- | :-------------------------------------------------------------------- |
| `CODE_OF_CONDUCT.md`               | Behavioral standards and the enforcement ladder                       |
| `CONTRIBUTING.md`                  | Branching, commits, tests, coding style, and the pull request process |
| `GOVERNANCE.md`                    | Who decides what, and how access survives any one person leaving      |
| `SECURITY.md`                      | How to report a vulnerability privately, and what to expect back      |
| `SUPPORT.md`                       | Which channel answers which kind of question                          |
| `.github/FUNDING.yml`              | The Sponsor button                                                    |
| `.github/pull_request_template.md` | Prefills every new pull request description                           |
| `.github/ISSUE_TEMPLATE/`          | Structured issue forms, plus the chooser config (`config.yml`)        |
| `.github/DISCUSSION_TEMPLATE/`     | Category forms for Discussions                                        |

That is the complete supported set: GitHub serves these file types as defaults and no others.
Apart from this README, the `LICENSE`, and the tooling that checks the files above, the repository
holds nothing else on purpose.

---

## ⚙️ How Inheritance Works

Three rules govern everything here:

1. **This repository must stay public.** Defaults are not served from a private `.github`
   repository, not even to private repositories.
2. **Files must live on the default branch.** A file on a feature branch is inert.
3. **Local beats default.** For the Markdown documents this is decided file by file: a repository
   can ship its own `SECURITY.md` and still inherit everything else. The forms are decided per
   _directory_: a repository that ships a single issue form of its own stops inheriting the whole
   set, not just the form it replaced.

Issue and discussion forms are path-locked and only work from `.github/ISSUE_TEMPLATE/` and
`.github/DISCUSSION_TEMPLATE/`. The five Markdown documents may sit at the repository root, in
`.github/`, or in `docs/`; they are kept at the root here for readability.

---

## 🚫 What Does _Not_ Inherit

GitHub serves **only** the documents listed above as defaults. Two files here are not among them:

- `LICENSE`, explicitly unsupported as a default; every repository needs its own
- `README.md`, including this one

Both stay because they govern and explain the rest, not because they travel. Everything else in
the repository inherits, which is the whole reason it is here.

---

## 🏷️ Labels

The forms here apply the **shared taxonomy** from
[`tannergolden/standards`](https://github.com/tannergolden/standards): prefixed names such as
`type: bug` and `status: needs triage`, which sort predictably and keep what a thing _is_ separate
from the stage it is at. All sixteen forms declare a `type:` and `status: needs triage` at creation,
and the two whose subject already implies an area declare that too: `area: ui/ux` for the
Accessibility Report, `area: dx` for the tooling and setup category. The `area:` names offered as
checkboxes in the other forms come from the same vocabulary but are read by a human at triage rather
than applied automatically.

That taxonomy is **not** part of a repository's stock label set. A repository provisions it by
running **🎯 Apply Standards** once, which syncs `data/labels.yml` over the API, create-or-update
and never pruning, so labels added by hand survive. Until that runs, a form naming a label the
repository does not have still files the issue normally; it simply arrives without that label and
gets triaged by hand.

The stock labels a new repository is born with keep working alongside the taxonomy, and two of them
carry platform behavior worth keeping: `good first issue` feeds GitHub's contributor discovery and
the repository's `/contribute` page, and `help wanted` feeds community-discovery search.

---

## 🛠️ Working On These Files

Changes here reach every repository on the account the moment they merge, so treat them as
production documents.

GitHub drops a malformed form **silently**: no error, no notification, just a chooser that quietly
stops offering it. Nothing else here builds or tests, so one command stands in for both:

```bash
python3 scripts/validate-templates.py
```

It checks what GitHub will not tell you about — that every form uses the `.yml` extension GitHub
documents, that every discussion form is named for a real category slug, that no form claims the
Polls category (which does not support forms at all), that the forms cross-reference each other by
the right name, and that links are not pinned to a branch name. It runs as the `lint` stage of
`.github/workflows/checks.yml`, alongside `markdownlint`, on every push. Both need to pass.

The workflows here are triggers; the logic they call is published once in
[tannergolden/standards](https://github.com/tannergolden/standards) and shared by every repository
on the account. None of them is served to any other repository: GitHub inherits community health
files, not workflows.

| File                       | Calls                                                            |
| :------------------------- | :--------------------------------------------------------------- |
| `checks.yml`               | Lint, secret scanning, CodeQL and workflow lint, on every push   |
| `governance.yml`           | Pull request title and DCO sign-off validation                   |
| `dependabot-automerge.yml` | Approves and queues Dependabot's patch and minor updates         |

There is deliberately no CI-failure escalation stub: it opens an issue when a gate fails, and
Issues are disabled on this repository, which is the same reason `governance.yml` installs only
the pull request job. A red gate here is read in the Actions tab.

`.github/dependabot.yml` keeps the pinned actions current, grouped into one pull request a month,
because a pin nobody moves holds one revision forever. The job ids `ci`, `secrets` and `pr` are
fixed: branch protection names a check `<job id> / <job name>`, so renaming one leaves protection
waiting on a check that never reports.

The house rules the checker cannot enforce:

- Keep the language **project-agnostic**. These render inside repositories with different stacks,
  audiences, and maturity levels.
- Use **absolute links**. A relative link resolves against the _consuming_ repository, where the
  target usually does not exist.
- **Promise nothing a repository might not have.** Hedge references to Makefiles, CI gates, and
  Discussions categories; a default renders everywhere, including where those are absent.
- Prefer **additive** edits. Tightening a rule here tightens it everywhere at once.

---

## 🧭 For Repository Owners

Inherit the defaults and write nothing; that is the intended path. Override only when a repository
genuinely differs: a different disclosure process, a different contribution workflow, a different
support channel. When you do override, copy the file into that repository and edit it there.

---

<div align="center">

**Sensible defaults, everywhere, by default.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by [@tannergolden](https://github.com/tannergolden). Distributed under the MIT License.

</div>

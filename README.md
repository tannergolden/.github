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
Apart from this README and the `LICENSE`, the repository holds nothing else on purpose.

---

## ⚙️ How Inheritance Works

Three rules govern everything here:

1. **This repository must stay public.** Defaults are not served from a private `.github`
   repository, not even to private repositories.
2. **Files must live on the default branch.** A file on a feature branch is inert.
3. **Local beats default, per file.** Inheritance is decided file by file: a repository can ship
   its own `SECURITY.md` and still inherit everything else.

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

This account deliberately uses **GitHub's stock labels**: `bug`, `documentation`, `duplicate`,
`enhancement`, `good first issue`, `help wanted`, `invalid`, `question`, and `wontfix`, at their
default colors and descriptions. Every new repository is born with exactly this set, and the issue
and discussion forms above apply only these names, so automatic labeling works in every repository
with nothing to install, clone, or sync.

Stock names also carry the platform behavior that matters: `good first issue` feeds GitHub's
contributor discovery and the repository's `/contribute` page, and `help wanted` feeds
community-discovery search.

---

## 🛠️ Working On These Files

Changes here reach every repository on the account the moment they merge, so treat them as
production documents:

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

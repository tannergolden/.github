<!--
title: '🩺 COMMUNITY HEALTH DEFAULTS'
description: 'How this repository serves account-wide default community health files to every repository on the account.'
type: index
keywords: [dot-github]
-->

<!-- markdownlint-disable MD041 -->

<div align="center">

# 🩺 COMMUNITY HEALTH DEFAULTS

<a name="top"></a>

**Account-wide defaults for contribution, governance, security, and support.**

_Write it once. Inherit it everywhere._

</div>

---

## 💡 What It Is

GitHub gives a repository named **`.github`** a special job: any file it holds from a fixed,
documented list is served as the **default** for every other repository on this account that does
not ship its own copy. So a new repository starts with a real code of conduct, a real security
policy and working issue forms on day one, without copying a single file.

- **Status**: Active. Changes here reach every repository on the account the moment they merge.

---

## 🚀 Quick Start

Inherit the defaults and write nothing: that is the intended path. **A repository's own file always
wins**, so when one genuinely differs (a different disclosure process, contribution workflow or
support channel), copy the file into that repository and edit it there.

---

## 📖 Using It

### ⚙️ How Inheritance Works

1. **This repository must stay public.** Defaults are not served from a private `.github`, not
   even to private repositories.
2. **Files must live on the default branch.** A file on any other branch is inert.
3. **Local beats default.** A Markdown document is decided file by file. The forms are decided per
   directory: a repository that ships one issue form of its own stops inheriting the whole set.

GitHub serves nothing else from a personal account's `.github`: not the `LICENSE`, not this
README, not workflows, and not `AGENTS.md`. Every repository carries its own licence and its own
`AGENTS.md`, and calls the shared workflows in
[tannergolden/standards](https://github.com/tannergolden/standards).

### 🛠️ Working On These Files

GitHub drops a malformed form **silently**, so one command checks what it will not tell you about,
and runs as the `lint` stage of `.github/workflows/checks.yml` beside `markdownlint`:

```bash
python3 .github/scripts/validate-templates.py
```

Keep the documents project-agnostic, use **absolute links** (a relative link resolves against the
consuming repository), promise nothing a repository might not have, and prefer additive edits.
The forms apply the standards' label taxonomy, which a repository gets by running
**🎯 Apply Standards** once.

`apply-standards.yml` is the one workflow here that reaches past this repository: dispatched from
the Actions tab, it applies the standards' settings, and the branch and tag rulesets if asked, to
every repository named in its form, with the `ADMIN_TOKEN` secret stored here. It previews by
default and changes nothing until it runs with dry-run off.
[`.github/workflows/README.md`](.github/workflows/README.md) logs every workflow here.

---

## 📦 What's Inside

| File                               | What it does                                                           |
| :--------------------------------- | :--------------------------------------------------------------------- |
| `CODE_OF_CONDUCT.md`               | Behavioral standards and the enforcement ladder                        |
| `CONTRIBUTING.md`                  | Branching, commits, tests, the AI policy, and the pull request process |
| `GOVERNANCE.md`                    | Who decides what, and how access survives any one person leaving       |
| `SECURITY.md`                      | How to report a vulnerability privately, and what to expect back       |
| `SUPPORT.md`                       | Which channel answers which kind of question                           |
| `.github/FUNDING.yml`              | The Sponsor button                                                     |
| `.github/pull_request_template.md` | Prefills every new pull request description                            |
| `.github/ISSUE_TEMPLATE/`          | Structured issue forms, plus the chooser config (`config.yml`)         |
| `.github/DISCUSSION_TEMPLATE/`     | Category forms for Discussions                                         |

That is the complete supported set. Beyond it the repository holds only this README, the
`LICENSE`, its own `AGENTS.md`, each folder's README, and the tooling that checks the files above.

---

## 🤝 Getting Involved

- **Questions**: [`SUPPORT.md`](SUPPORT.md) says where to ask.
- **A change**: [`CONTRIBUTING.md`](CONTRIBUTING.md) explains how, following the
  [standards](https://github.com/tannergolden/standards/blob/HEAD/docs/README.md) by link,
  and every contribution follows the [code of conduct](CODE_OF_CONDUCT.md).
- **Who decides**: [`GOVERNANCE.md`](GOVERNANCE.md) names the maintainers.

---

## 🛡️ Security

Report a vulnerability privately, never in an issue: [`SECURITY.md`](SECURITY.md) says how, and
how fast a fix follows.

---

## ⚖️ Licence

The community health defaults are released under the terms in [LICENSE](/LICENSE).

---

<div align="center">

**Sensible defaults, everywhere, by default.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by [@tannergolden](https://github.com/tannergolden). Distributed under the terms in [LICENSE](/LICENSE).

</div>

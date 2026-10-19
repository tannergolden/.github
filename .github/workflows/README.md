<!--
title: '⚙️ WORKFLOWS'
description: 'The three workflows this repository runs on itself, each a stub calling tannergolden/standards.'
type: index
keywords: [github-actions, workflows, ci]
-->

<!-- markdownlint-disable MD041 -->

<div align="center">

# ⚙️ WORKFLOWS

<a name="top"></a>

**The checks this repository runs on itself.**

_Triggers here, logic in the standards._

</div>

---

## 💡 What This Folder Is For

Each workflow here is a trigger stub: the logic it calls is published once in
[tannergolden/standards](https://github.com/tannergolden/standards) and shared by every repository
on the account. None of them is served to any other repository, since GitHub inherits community
health files, not workflows. `checks.yml` runs the [validator](../scripts/validate-templates.py) and
markdownlint as its lint stage, so a malformed form fails a check instead of vanishing from a
chooser.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log fields=name,on -->

| Entry                                                  | Name                | Triggers                                                              | Purpose                                                                                           |
| :----------------------------------------------------- | :------------------ | :-------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------ |
| [`checks.yml`](checks.yml)                             | Checks              | `push`, `pull_request`, `schedule` (`0 3 * * 1`), `workflow_dispatch` | The gates for this repository, all called from tannergolden/standards.                            |
| [`dependabot-automerge.yml`](dependabot-automerge.yml) | Automate Dependabot | `pull_request`                                                        | Approves and queues Dependabot's patch and minor updates for the two workflows in this directory. |
| [`governance.yml`](governance.yml)                     | Governance          | `pull_request_target`                                                 | Pull request validation, called from tannergolden/standards.                                      |
| [`README.md`](README.md)                               | -                   | -                                                                     | This file.                                                                                        |

<!-- AUTO-INDEX:END -->

This log is drawn from each workflow's own `name:` and triggers. Redraw this log in the same commit
as a change to this folder, from a checkout of tannergolden/standards at `v1`:

```bash
python3 <standards>/.github/scripts/update-doc-indexes.py --tree --write
```

---

<div align="center">

**Checked on every push, served to every repository.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by [@tannergolden](https://github.com/tannergolden). Distributed under the MIT License.

</div>

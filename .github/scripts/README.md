<!--
title: '🧰 SCRIPTS'
description: 'The validator for every form this repository serves, since GitHub drops a malformed one silently.'
type: index
keywords: [validation, forms, python]
-->

<!-- markdownlint-disable MD041 -->

<div align="center">

# 🧰 SCRIPTS

<a name="top"></a>

**What fails loudly when GitHub would fail silently.**

_One command stands in for a test suite._

</div>

---

## 💡 What This Folder Is For

GitHub drops a malformed form without an error anywhere, so
[`validate-templates.py`](validate-templates.py) checks what it will not tell you: every form's
extension and name, every discussion form's category slug, the forms' cross-references, and links
that would break on a default-branch rename. Run it before a push:

```bash
python3 -m pip install 'pyyaml==6.0.2'
python3 .github/scripts/validate-templates.py
```

It is the first half of the lint stage in [`checks.yml`](../workflows/checks.yml), and
markdownlint is the second.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                                            | Purpose                                                        |
| :----------------------------------------------- | :------------------------------------------------------------- |
| [`README.md`](README.md)                         | This file.                                                     |
| [`validate-templates.py`](validate-templates.py) | Validate the community health defaults this repository serves. |

<!-- AUTO-INDEX:END -->

This log is drawn from each script's docstring. Redraw this log in the same commit as a change to
this folder, from a checkout of tannergolden/standards at `v1`:

```bash
python3 <standards>/.github/scripts/update-doc-indexes.py --tree --write
```

---

<div align="center">

**Loud where GitHub is silent.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by [@tannergolden](https://github.com/tannergolden). Distributed under the MIT License.

</div>

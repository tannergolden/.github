<!--
title: '📥 ISSUE FORMS'
description: 'The issue forms every repository on the account inherits until it ships its own, and their chooser.'
type: index
keywords: [issues, forms, community-health]
-->

<!-- markdownlint-disable MD041 -->

<div align="center">

# 📥 ISSUE FORMS

<a name="top"></a>

**The forms a reporter picks from, in every repository without its own.**

_Inherited as a set, overridden as a set._

</div>

---

## 💡 What This Folder Is For

These forms are the account-wide defaults: every repository that ships no `.github/ISSUE_TEMPLATE/`
of its own offers them in its chooser. Overriding is all or nothing, so a repository with a single
form or config file of its own stops inheriting the whole folder. [`config.yml`](config.yml) turns
blank issues off and routes security reports to private channels, and every form's file name is
kebab-case, as the [validator](../scripts/validate-templates.py) checks.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log fields=name -->

| Entry                                                  | Name                           | Purpose                                                                                                                                    |
| :----------------------------------------------------- | :----------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| [`accessibility-report.yml`](accessibility-report.yml) | &#x267F; Accessibility Report  | &#x26D1;&#xFE0F; Report accessibility issues to improve compliance and inclusive User Experience (UX).                                     |
| [`bug-report.yml`](bug-report.yml)                     | &#x1F41B; Bug Report           | &#x1F41E; Report a defect, regression, or unexpected behavior so we can reproduce and fix it quickly.                                      |
| [`config.yml`](config.yml)                             | -                              | Steer reporters into the right form, and keep vulnerability reports PRIVATE.                                                               |
| [`documentation-report.yml`](documentation-report.yml) | &#x1F4DA; Documentation Report | &#x1F4D6; Report documentation gaps, inaccuracies, outdated sections, or clarity issues so we can correct and improve them.                |
| [`feature-request.yml`](feature-request.yml)           | &#x2728; Feature Request       | &#x1FA84; Propose new functionality or enhancements with clear acceptance criteria, rationale, and success metrics.                        |
| [`feedback-report.yml`](feedback-report.yml)           | &#x1F4DD; Feedback Report      | &#x1F4A1; Share feedback, suggestions, or usability insights to help us improve the project.                                               |
| [`performance-report.yml`](performance-report.yml)     | &#x1F680; Performance Report   | &#x26A1;&#xFE0F; Report slow pages, high latency, memory spikes, or inefficiencies so we can measure, reproduce, and optimize performance. |
| [`README.md`](README.md)                               | -                              | This file.                                                                                                                                 |

<!-- AUTO-INDEX:END -->

This log is drawn from each form's own `name:` and `description:`. Redraw this log in the same
commit as a change to this folder, from a checkout of tannergolden/standards at `v1`:

```bash
python3 <standards>/.github/scripts/update-doc-indexes.py --tree --write
```

> [!IMPORTANT]
> **Never give this README YAML front matter.** GitHub lists a Markdown file in this folder as a
> template only when it opens with front matter naming it. This one opens with an HTML comment
> instead, which is why no chooser ever shows it, and why the validator passes over it.

---

<div align="center">

**Every report arrives on a form.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by [@tannergolden](https://github.com/tannergolden). Distributed under the MIT License.

</div>

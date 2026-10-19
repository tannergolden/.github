<!--
title: '💬 DISCUSSION FORMS'
description: 'The discussion forms every repository inherits, each named for the category slug it binds to.'
type: index
keywords: [discussions, forms, community-health]
-->

<!-- markdownlint-disable MD041 -->

<div align="center">

# 💬 DISCUSSION FORMS

<a name="top"></a>

**One form per Discussions category, named for its slug.**

_A form binds only where its category exists._

</div>

---

## 💡 What This Folder Is For

A discussion form binds to the category whose slug is its file name, in every repository that ships
no `.github/DISCUSSION_TEMPLATE/` of its own. Stock categories exist wherever Discussions is on;
custom ones, such as `roadmap`, bind only where a repository has created them. Polls take no form at
all, and the [validator](../scripts/validate-templates.py) refuses one, along with any slug it was not
told to expect.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                                                            | Purpose                                                                                                                                          |
| :--------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------- |
| [`accessibility.yml`](accessibility.yml)                         | Accessibility feedback - contrast, keyboard navigation, focus order, screen readers.                                                             |
| [`announcements.yml`](announcements.yml)                         | Official updates such as releases, deprecations, and roadmap notes.                                                                              |
| [`general.yml`](general.yml)                                     | General discussion, introductions, meetups, and topics that don&#x2019;t fit other categories.                                                   |
| [`ideas.yml`](ideas.yml)                                         | Brainstorm features or improvements before opening a formal Feature Request.                                                                     |
| [`internationalization-i18n.yml`](internationalization-i18n.yml) | Translation and localization topics, language-specific feedback, and locale issues.                                                              |
| [`q-a.yml`](q-a.yml)                                             | Ask &#x201C;how do I&#x2026;?&#x201D; questions and get help from maintainers and the community.                                                 |
| [`README.md`](README.md)                                         | This file.                                                                                                                                       |
| [`roadmap.yml`](roadmap.yml)                                     | High-level plans and milestones. Link to Issues and Pull Requests for tracking.                                                                  |
| [`show-and-tell.yml`](show-and-tell.yml)                         | Share demos, prototypes, case studies, success stories, and lessons learned.                                                                     |
| [`tooling-setup.yml`](tooling-setup.yml)                         | Developer environment topics - IDEs, Node.js versions, package managers, linters, CI runners, containers/devcontainers, and local configuration. |

<!-- AUTO-INDEX:END -->

This log is drawn from the prose each form shows above its fields. Redraw this log in the same
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

**One category, one form.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by [@tannergolden](https://github.com/tannergolden). Distributed under the MIT License.

</div>

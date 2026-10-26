<!--
title: '💬 PROMPTS'
description: 'Prompts for working on these community health defaults with an AI agent: copy one, fill it in, paste it.'
type: reference
keywords: [prompts, ai-agents]
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 💬 PROMPTS

<a name="top"></a>

**Prompts for working in this repository with an AI agent.**

_Written for this repository. Copied whole._

</div>

---

> [!TIP]
> **Write this repository's own prompts here**, under sections of your own:
> prompts that only make sense in it, such as ones for using it, making
> changes to it or understanding how it works. Give each a `###` heading, a
> **Use when** line and one `text` block. Prompts that work in any repository,
> and how to write a good one, are in the
> [universal prompts](https://github.com/tannergolden/intelligence/blob/HEAD/docs/Prompts.md).
> 🔁 Intelligence Sync added this page, and never changes it.

**Find a prompt.** Each runs as it is, except those marked ✏️, which ask for your details.

- **Forms:** [Add Or Change An Issue Form](#add-or-change-an-issue-form) ✏️,
  [Add Or Change A Discussion Form](#add-or-change-a-discussion-form) ✏️
- **Documents:** [Change A Default Document](#change-a-default-document) ✏️,
  [Change The AI Policy](#change-the-ai-policy) ✏️,
  [Change The Pull Request Template](#change-the-pull-request-template) ✏️
- **Reach:** [Find Who A Change Here Reaches](#find-who-a-change-here-reaches) ✏️,
  [Check What Apply Standards Would Change](#check-what-apply-standards-would-change) ✏️

---

## 📋 Forms

### Add Or Change An Issue Form

**Use when** you want a new issue form in every repository that inherits these defaults, or a change to
one of them. **Fill in** `{{FORM_CHANGE}}`, the form to add or change, and what it should ask.

```text
<context>
The change: {{FORM_CHANGE}}.
Every form in .github/ISSUE_TEMPLATE/ is offered by every repository on the account that ships no form folder of its own, the moment it merges, and GitHub drops a malformed form with no error anywhere. .github/scripts/validate-templates.py is the one check that fails loudly: its docstring and AGENTS.md set the rules a form keeps, and the README's Labels section says which labels a form may apply.
</context>

<task>
Write or change the form, and update everything that names or counts the forms: config.yml where the chooser needs it, every form that points at this one, the routing table in SUPPORT.md, the README, and the folder's file log.
</task>

<constraints>
- Name the file in kebab-case with the .yml extension, apply labels only from the shared type:, status: and area: taxonomy, and give a required dropdown an escape hatch, such as Other, unless the validator lists it as closed.
- Write for any repository: no branch name, stack or tool of this account's, and a hedge on anything a repository may lack.
- If the form would make sense in one repository only, stop and tell me: that repository ships its own folder, and then inherits none of these.
- If any detail above is still a placeholder in double braces, ask me for it before you start.
</constraints>

<done_when>
- python3 .github/scripts/validate-templates.py and npx --yes markdownlint-cli2 pass, and the file log is redrawn with the standards' update-doc-indexes.py.
- You report each file you changed, and what a reporter now sees in the chooser.
</done_when>
```

### Add Or Change A Discussion Form

**Use when** you want a form for a Discussions category in every repository that inherits these
defaults, or a change to one. **Fill in** `{{CATEGORY}}`, the category's slug, and what its form should
ask.

```text
<context>
The category: {{CATEGORY}}.
A discussion form in .github/DISCUSSION_TEMPLATE/ binds to the category whose slug is its file name. Stock categories exist wherever Discussions is on, a custom one binds only where a repository has created it, and polls take no form at all. .github/scripts/validate-templates.py lists the stock slugs and, in DECLARED_CATEGORY_SLUGS, every slug this account serves, and refuses a form for any other.
</context>

<task>
Write or change the form. For a new slug, add it to DECLARED_CATEGORY_SLUGS as stock or custom, and update the folder's README, its file log, and anything else that lists the categories, such as SUPPORT.md.
</task>

<constraints>
- Name the file for the category's exact slug, with the .yml extension, and never write a form for polls.
- For a custom slug, tell me which repositories you know to have the category: the form binds nowhere else.
- Apply labels only from the shared type:, status: and area: taxonomy, and write for any repository.
- If any detail above is still a placeholder in double braces, ask me for it before you start.
</constraints>

<done_when>
- python3 .github/scripts/validate-templates.py and npx --yes markdownlint-cli2 pass, and the file log is redrawn.
- You report each file you changed, and whether the category is stock or custom.
</done_when>
```

---

## 📄 Documents

### Change A Default Document

**Use when** you want to change the code of conduct, the contributing guide, the governance, the
security policy or the support guide that every repository without its own copy shows. **Fill in**
`{{CHANGE}}`, the document and what should change.

```text
<context>
The change: {{CHANGE}}.
The five documents at the root are served to every repository on the account that has no copy of its own, the moment the change merges, and a repository's own copy always wins. AGENTS.md says how they are written: in project-agnostic words, with absolute links at blob/HEAD/, promising nothing a repository might lack, and by additive edits, since a rule tightened here tightens everywhere.
</context>

<task>
Make the change, and every edit it needs elsewhere in this repository, such as another document that quotes or links the part you changed.
</task>

<constraints>
- Keep each document's hidden frontmatter, masthead, section rules and footer, and wrap its prose within 120 columns.
- If the change tightens a rule, drops a promise or changes a process, such as how a vulnerability is reported, say what it changes for a repository and its contributors, and wait for my yes before you make it.
- If any detail above is still a placeholder in double braces, ask me for it before you start.
</constraints>

<done_when>
- python3 .github/scripts/validate-templates.py and npx --yes markdownlint-cli2 pass.
- You report each line that changed, before and after, and, where you can read them, the repositories that will not show it because they keep their own copy.
</done_when>
```

### Change The AI Policy

**Use when** you want to change what the AI policy in `CONTRIBUTING.md` asks of people and agents,
which every agent on the account reads before its first commit. **Fill in** `{{CHANGE}}`, what should
change, and why.

```text
<context>
The change: {{CHANGE}}.
The AI-Assisted Contributions section of CONTRIBUTING.md is the AI policy of every repository that has no contributing guide of its own. The universal rules every agent follows have it read that policy before its first commit or post, publish nothing where it bars AI, and disclose AI help where it says nothing, so a change here changes what every agent does on the account. The pull request template's AI box points at it.
</context>

<task>
Propose the new wording first, with what each agent and each person would do differently under it, and wait for my yes. Then change the section, and everything that quotes or links it, such as the pull request template's comment and box.
</task>

<constraints>
- Keep it consistent with the universal rules in AGENTS.md: a policy that contradicts one leaves agents to guess, so name any conflict to me rather than write it.
- Keep its example trailers in their text block, and every heading anchor something links to, such as #-ai-assisted-contributions.
- If any detail above is still a placeholder in double braces, ask me for it before you start.
</constraints>

<done_when>
- python3 .github/scripts/validate-templates.py and npx --yes markdownlint-cli2 pass.
- You report the policy before and after, and what changes for agents and for people.
</done_when>
```

### Change The Pull Request Template

**Use when** you want every new pull request on the account, in each repository without a template of
its own, to open with different sections or questions. **Fill in** `{{CHANGE}}`, what should change.

```text
<context>
The change: {{CHANGE}}.
.github/pull_request_template.md prefills the description of every pull request in each repository that ships no template of its own. Unlike the documents at the root it carries no frontmatter, masthead or footer, and its opening comment tells the author how to fill it in. Agents that open pull requests follow its sections, so a section added or renamed changes every pull request they write.
</context>

<task>
Change the template, keeping each section one an author of any project can fill in, and update everything that names its sections or its boxes, such as the AI policy in CONTRIBUTING.md.
</task>

<constraints>
- Add no frontmatter, masthead or footer: it is the one file here that carries none.
- Keep the AI assistance box, which the AI policy asks every author to tick.
- Write for any repository: no branch name, stack or tool of this account's, and a hedge on anything a repository may lack, such as a changelog.
- If any detail above is still a placeholder in double braces, ask me for it before you start.
</constraints>

<done_when>
- python3 .github/scripts/validate-templates.py and npx --yes markdownlint-cli2 pass.
- You report the template before and after, as an author sees it in a new pull request.
</done_when>
```

---

## 🌐 Reach

### Find Who A Change Here Reaches

**Use when** a change here is about to merge, and you want to know which repositories will show it and
which will not, because they keep a copy of their own. **Fill in** `{{CHANGE}}`, the files that change,
or `this branch`.

```text
<context>
The change: {{CHANGE}}.
A repository shows this repository's file only where it has none of its own. For the documents that is decided file by file, wherever GitHub looks for them: the root, .github/ or docs/. For the forms it is decided folder by folder, so one form or config.yml of a repository's own stops it inheriting the whole folder. The README's How Inheritance Works sets this out.
</context>

<task>
For each repository on the account you can read, find which of the changed files it inherits and which it overrides with a copy of its own, and for each copy, how it differs from what changes here.
</task>

<constraints>
- Change nothing in any repository: read their trees, from checkouts or through GitHub.
- A private repository's name goes in your report to me only, never in a file, commit, pull request or comment here, since this repository is public.
- If you cannot read a repository, list it as unknown rather than guessing.
- If any detail above is still a placeholder in double braces, ask me for it before you start.
</constraints>

<output>
A table of each repository: each changed file, inherited or overridden, and how each copy differs. Then the repositories you could not read, and any copy that looks better as the default.
</output>
```

### Check What Apply Standards Would Change

**Use when** you are about to run Apply Standards from here, and want to know first what it would write
to each repository. **Fill in** `{{REPOSITORIES}}`, the repositories to check, or `the default list`.

```text
<context>
The repositories: {{REPOSITORIES}}.
.github/workflows/apply-standards.yml writes the standards' repository settings, and the rulesets when asked, to each repository its form names, with this repository's ADMIN_TOKEN. Its dry run is on by default and shows each repository's plan in its job's summary. The values are data/repository-settings.json and data/rulesets/ in tannergolden/standards, whose docs/operations/Repository-Settings.md says what each is for. This repository's runs are public, so a private repository is never named in the form: it runs its own stub.
</context>

<task>
Compare each repository's settings and rulesets with the standards' values, through read-only GitHub API calls if you can, and list what a run would change. Then give me the exact inputs for a dry run, and what to check in its summaries.
</task>

<constraints>
- Read only: make no call that writes, and never dispatch the workflow; starting it, dry or not, is mine.
- Leave a private repository out of the inputs you give me, and tell me to apply the standards from its own stub.
- If you cannot read a setting, list it with where I check it, rather than assume either way.
- If any detail above is still a placeholder in double braces, ask me for it before you start.
</constraints>

<output>
For each repository: each setting and rule a run would change, from what to what, and those you could not read. Then the inputs for the dry run, settings before rulesets, and what to check in each job's summary before a real run.
</output>
```

---

<div align="center">

**A better prompt in, better work out.**

[↑ Back to Top](#top)

</div>

<!--
title: '🏛️ PROJECT GOVERNANCE'
description: 'The default charter for decision-making, maintainer roles, and access continuity across this account.'
tags: [governance, maintainers, access-continuity]
category: community
-->

<!-- markdownlint-disable MD041 -->

<div align="center">

# 🏛️ PROJECT GOVERNANCE

<a name="top"></a>

**How these projects are led, who decides what, and how access and quality survive any single person leaving.**

_Decisions in the open. Access that outlives individuals._

</div>

---

> [!NOTE]
> This is the **default governance charter** for repositories owned by
> [@tannergolden](https://github.com/tannergolden). It applies to any repository that does not
> publish its own `GOVERNANCE.md`. Where a repository ships its own charter, that charter wins.

---

## 🎯 Governance Model

These projects use a **lightweight maintainer model**. A small group of **Maintainers** holds merge
and administrative authority; everyone else contributes through pull requests. Decisions are made
in the open on issues and pull requests, and authority rests with documented standards rather
than with any individual's preference.

- **Standards over opinions.** When a person and a documented standard disagree, the standard wins
  until the standard is changed by pull request.
- **Lazy consensus.** A proposal open for review for at least 72 hours with no unresolved
  objection from a Maintainer may be merged once CI is green. Substantive disagreements are resolved by discussion; if consensus
  fails, a majority of Maintainers decides.
- **Everything is a change request.** Governance itself is edited the same way as code: by pull
  request to this file.

---

## 👥 Roles & Responsibilities

| Role                   | Who they are                             | Responsibilities                                                                              |
| :--------------------- | :--------------------------------------- | :-------------------------------------------------------------------------------------------- |
| **Maintainer**         | Named in the repository's `CODEOWNERS`   | Review and merge pull requests, cut releases, steward security response, administer settings. |
| **Contributor**        | Anyone who opens a pull request or issue | Follow the contributing guidelines; respond to review feedback.                               |
| **Security responder** | A Maintainer on rotation                 | Triage private reports per the [security policy](https://github.com/tannergolden/.github/blob/HEAD/SECURITY.md) within the stated timelines. |

Maintainers are added by consensus of the existing Maintainers after a sustained record of quality
contributions, and are recorded in `CODEOWNERS`. Once populated, that file is the single source of
truth for who currently holds authority.

---

## 🔑 Access Continuity & Bus Factor

Projects are designed so that losing any single person does the least possible harm:

- **Administrative reality.** A repository owned by a personal account has exactly one
  administrator: the owner. A project that outgrows that model is transferred to an organization,
  where administrative access can genuinely be held by two or more people.
- **No credentials live only in one head.** Release signing, publishing, and service tokens must
  be documented in a maintainer runbook and recoverable without any one person, never tied solely
  to one individual's account.
- **Succession plan.** GitHub's account successor setting designates who may manage public
  repositories if the owner dies; day to day, Maintainers appoint replacements by updating
  `CODEOWNERS`. Because every standard, workflow, and guardrail is committed to the repository, a
  new Maintainer can take over from the documentation alone.

> [!IMPORTANT]
> **Two-factor authentication is required** for every account with commit or admin access. Prefer a
> security key or authenticator app over SMS. This is a standing requirement, not a suggestion.

---

## 🧑‍⚖️ Change Review Standard

Quality is enforced by process, not trust:

- **Every change lands by pull request.** Long-lived branches are protected against direct
  pushes wherever the repository has configured branch protection, and required status checks
  must be green to merge.
- **Independent review is the goal state.** Once a project has two or more Maintainers, **at least
  half of all non-trivial merged changes should be reviewed by someone other than the author**.
  Solo-maintainer repositories run without a required approval; CI still gates every merge, and the
  required-approval setting is enabled the moment a second Maintainer exists.
- **Review looks for correctness, security, and standards alignment**, not style preferences the
  formatter already settles.

---

## 🌱 Onboarding New Contributors

- Start with the
  [Contributing Guidelines](https://github.com/tannergolden/.github/blob/HEAD/CONTRIBUTING.md).
- Good entry points are issues labeled **`good first issue`** and **`help wanted`**: small,
  well-scoped tasks that need no deep context.
- Ask questions via
  [Support](https://github.com/tannergolden/.github/blob/HEAD/SUPPORT.md).

---

<div align="center">

**Led in the open. Built to outlast any single maintainer.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by [@tannergolden](https://github.com/tannergolden).

</div>

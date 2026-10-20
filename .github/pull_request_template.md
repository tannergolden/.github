<!--
This template becomes the body of your pull request. Fill in every section
(pull requests with an empty description may be closed); delete a line that
truly does not apply or mark it N/A.
- Title: Conventional Commit - <type>(<scope>): summary. Squash merges
  typically take it as the commit subject and it can feed release notes,
  so make it accurate.
- Branch: a short-lived <type>/<topic> (feat/*, fix/*, docs/*) into the
  repository's default branch.
- Scope: one intent, under 300 changed lines and at most 10 files.
- AI help is welcome on the terms of the AI policy:
  https://github.com/tannergolden/.github/blob/HEAD/CONTRIBUTING.md#-ai-assisted-contributions
- Open as a Draft for early feedback; mark Ready for Review once CI is green.
- Never paste secrets into code, logs, or screenshots.
-->

<!-- markdownlint-disable MD041 -->

## 📝 Summary

- **What changed** (2-4 sentences):
- **Why** (the problem it solves; link the issue / ADR / discussion):

## 🎯 Type

- [ ] ✨ Feature
- [ ] 🐞 Bug fix
- [ ] ♻️ Refactor
- [ ] ⚡️ Performance
- [ ] 🔒 Security
- [ ] 🧪 Tests only
- [ ] 📚 Docs
- [ ] ⚙️ Build / CI
- [ ] 🧹 Chore / Maintenance
- [ ] 💥 Breaking change <!-- a breaking change makes Risk & Rollback below mandatory -->

## 🔗 Linked issues

- Closes #
- Refs #

## ✅ Validation

- [ ] Local gates green (e.g. `make lint && make test && make build`, or this repository's equivalent)
- **Tests** (required for behavior changes; say what each new test pins down, and add a regression test for bug fixes):
- **Coverage**: Unit / Integration / E2E / N/A (delete those that do not apply)
- **Manual steps** a reviewer can follow to reproduce the result:
  1. [step]
  2. [step]
- **Evidence** for UI or behavior changes (before -> after screenshots, recordings,
  or logs; redact secrets; add alt text on images):

## 💥 Risk & Rollback

- **Blast radius / breaking impact** (migration steps if any):
- **Risk level**: Low / Medium / High
- **Rollback plan** (revert PR, disable flag, restore config):

## 🧭 Rollout _(if applicable)_

- **Feature flag** (name + default):
- **Dependencies** (linked PRs, migrations, config toggles):

## 🤖 AI assistance

- [ ] No AI assistance
- [ ] AI-assisted: I read and stand behind every change, and each commit the AI shaped is co-authored
- **What the AI did** (what it wrote, changed, or checked):

## 📚 Docs & release notes

- [ ] Docs updated (link) or N/A:
- **Release note** (one user-facing sentence):

## ✅ Author checklist

- [ ] One intent, sized for review
- [ ] Conventional Commit **title**; commits authored and **signed off** (`git commit -s`) by me, never by an AI
- [ ] Local gates green
- [ ] Tests added or updated for logic changes; documented above
- [ ] No secrets committed; scanner alerts resolved
- [ ] Docs updated when behavior or setup changed
- [ ] I read this repository's root `AGENTS.md`, and any AI-assisted work followed it
- [ ] Targeting the default branch; ready to **squash merge** on green CI

<!--
Reviewer rubric:
- Blocking: Correctness (edge cases + requirement met), Security (secrets,
  least privilege), Testability (coverage matches intent).
- High: Readability. Medium: Parity with established patterns.
- Merge needs the repository's required status checks green.
- Tag feedback by intent: [BLOCKER] / [SUGGESTION] / [NIT] / [QUESTION].
-->

<!--
To credit co-authors, add "Co-authored-by: Full Name <email>" trailers (one
per line, real values) to the merge commit message when squash-merging. An AI
that shaped the change is credited the same way, never as the author.
Listing them here helps whoever merges copy them over:
Co-authored-by: Name <email@example.com>
-->

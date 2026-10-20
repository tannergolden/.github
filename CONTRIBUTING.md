<!--
title: '🤝 CONTRIBUTING GUIDELINES'
description: 'The default contribution workflow, commit standard, and pull request process for repositories owned by @tannergolden.'
type: guide
keywords: [pull-requests, conventional-commits, code-quality]
-->

<!-- markdownlint-disable MD041 -->

<div align="center">

# 🤝 CONTRIBUTING GUIDELINES

<a name="top"></a>

**Accelerating the engineering ecosystem through structured and safe contributions.**

_Small diffs. Green gates. Shared standards._

</div>

---

> [!NOTE]
> This is the **default contributing guide** for repositories owned by
> [@tannergolden](https://github.com/tannergolden). It applies to any repository that does not
> publish its own `CONTRIBUTING.md`. Where a repository ships its own guide, that guide wins.

---

> [!IMPORTANT]
> **Read the repository's root `AGENTS.md` first.** Every repository on this account has one: the
> universal rules AI coding agents follow there, then the repository's own rules. It is written for
> agents and worth a person's two minutes too. Using AI? The
> [AI policy](#-ai-assisted-contributions) below says how.

---

## 🎯 Our Philosophy

We value **small, frequent, and high-quality** contributions that adhere to established patterns.
Every change should move the project closer to being more stable, secure, and maintainable. We do
not accept "code dumps". Every line should be justified and tested.

---

## 🏗️ Getting Started

### 1. Prepare Your Environment

- Read the repository's root `AGENTS.md`, then its `README.md`.
- Fork the repository (external contributors) or branch from it (maintainers).
- Install dependencies using the repository's documented setup command. Most projects here
  standardize on a single entry point:

  ```bash
  make setup
  ```

  If the repository has no `Makefile`, follow the setup steps in its `README.md`.

> [!TIP]
> **New here?** Start with issues labeled **`good first issue`** or **`help wanted`**: small,
> well-scoped tasks that need no deep context.

### 2. Branching

- **Target branch:** open pull requests against the repository's default branch unless its README
  says otherwise. Production/release branches are promoted to, never committed to directly.
- **Naming convention:** `<type>/<topic>`, where the type is one of the commit types below:
  - `feat/short-description`
  - `fix/issue-description`
  - `docs/what-changed`

---

## 🧱 Development Standards

### Commit Messages

We use **[Conventional Commits](https://www.conventionalcommits.org/)** (`type(scope): summary`).
Where a repository automates releases, this format is what its tooling reads to generate changelogs
and determine version numbers, so treat it as load-bearing rather than cosmetic.

- **Format:** `type(scope): summary`
- **Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`,
  `revert`, `security`
- **Body:** say why the change was made, not only what it does.
- **Trailers:** any `Co-Authored-By:` lines, then your `Signed-off-by:` as the last line (see
  [AI-Assisted Contributions](#-ai-assisted-contributions) and the
  [DCO sign-off](#1-opening-the-pr) below).

### Code Quality Checklist

- **Linting**: code must pass the linter before submission (`make lint` where available).
- **Testing**: logic changes require tests (`make test` where available).
- **Documentation**: update the docs when your change affects behavior or setup.

### Test Policy (required)

This is a **mandated policy**, not a preference:

- **Every change that adds or changes functionality MUST add or update tests** covering the new
  behavior. A pull request that changes logic without touching tests will be asked to add them.
- **Document the tests you add** in the pull request description. Say what behavior each new test
  pins down, so reviewers can confirm coverage matches intent.
- **Bug fixes get a regression test** that fails before the fix and passes after.
- A green suite is part of the zero-failure CI gate below.

### Coding Style

- **Formatting**: the repository's formatter is the authority; run it before pushing.
- **Naming**: files `kebab-case`, classes/components `PascalCase`, variables/functions
  `camelCase`, constants `UPPER_SNAKE_CASE`.
- **TypeScript** (when used): `strict: true`; avoid `any` (prefer `unknown` with narrowing);
  explicit return types on exported APIs.
- **Logic**: prefer `async`/`await` over `.then()`; throw typed errors and catch at the boundary;
  favor pure functions and immutability; use guard clauses instead of deep nesting.

### Testing Standards

- **Location**: co-locate unit tests (`foo.test.*`) next to source; keep end-to-end and
  integration suites under `tests/`.
- **Mocking**: always mock network and API calls; isolate pure logic from heavy dependencies.
- **Structure**: descriptive assertions, e.g. `it("should <behavior> when <condition>", …)`.
- **Gate**: no filler assertions; every logic change earns a meaningful test.

### Workflow (CI) Authoring

- **Naming**: `kebab-case.yml` files with explicit `on:` triggers.
- **Security**: pin third-party actions to a full commit SHA or a stable tag; declare a top-level
  `permissions: {}` and grant scopes per job; never print secrets.
- **Reliability**: set `timeout-minutes` on every job, use `concurrency` groups, and move logic
  longer than a few lines into a script rather than inline YAML.

---

## 🤖 AI-Assisted Contributions

This is the AI policy for every repository that uses this guide. An AI agent reads it before its
first commit or post in a repository; a person using one should read it too.

**AI-assisted contributions are welcome when a person takes responsibility for them.** The rules
that follow from that:

- **A person owns the change.** Whoever opens the pull request has read what the AI produced,
  stands behind it, and answers for it in review. The AI is a tool that person used, not the
  contributor.
- **The person is the author and signs off.** Every commit is authored with that person's own git
  identity, never an AI's, and ends with that person's `Signed-off-by:`. The sign-off certifies the
  Developer Certificate of Origin, which only a person can do. An agent that finds
  `git config user.email` unset, or set to an AI, asks whose identity to use rather than guessing.
- **The AI is credited as a co-author.** Each commit an AI shaped carries a `Co-Authored-By:`
  trailer naming the model and its vendor's no-reply address, above the sign-off. A commit the
  person wrote alone carries none.
- **The pull request says what the AI did.** Tick the AI assistance box in the pull request
  template and say, in a sentence or two, what the AI wrote, changed, or checked.
- **Agents read `AGENTS.md` before anything else and follow it.** Its rules apply to every agent
  working in the repository, alongside this guide.

A commit an AI helped with ends like this:

```text
Co-Authored-By: <model> <vendor no-reply address>
Signed-off-by: Your Name <you@example.com>
```

---

## 🌿 The Pull Request Process

### 1. Opening the PR

- Target the default branch.
- Keep each pull request to **one intent**, under 300 changed lines and at most 10 files.
- Complete the pull request template in full; pull requests with an empty description may be closed.
- **Sign off your commits (DCO).** Adding a `Signed-off-by` line certifies the
  [Developer Certificate of Origin](https://developercertificate.org/), meaning you wrote the
  change or have the right to submit it. Git does it for you:

  ```bash
  git commit -s -m "feat(scope): summary"
  ```

  This appends `Signed-off-by: Your Name <you@example.com>` from your git identity.

### 2. CI Gating

- Pull requests run the repository's CI gates: typically linting, tests, build verification, and
  security analysis.
- **Zero-failure policy**: all checks must be green before review begins.

### 3. Review Etiquette

- Expect a maintainer review before merge. Single-maintainer repositories may run without a
  required approval; CI still gates every merge.
- Be responsive to feedback.
- Use clear feedback prefixes: `[BLOCKER]`, `[SUGGESTION]`, `[NIT]`.

---

## 🔗 See also

- [Code of Conduct](https://github.com/tannergolden/.github/blob/HEAD/CODE_OF_CONDUCT.md)
- [Security Policy](https://github.com/tannergolden/.github/blob/HEAD/SECURITY.md)
- [Support](https://github.com/tannergolden/.github/blob/HEAD/SUPPORT.md)
- [Governance](https://github.com/tannergolden/.github/blob/HEAD/GOVERNANCE.md)
- [Universal rules for AI coding agents](https://github.com/tannergolden/intelligence), which
  every repository's `AGENTS.md` carries
- [Engineering standards](https://github.com/tannergolden/standards/blob/HEAD/docs/README.md)

---

<div align="center">

**Structured contributions. Predictable growth.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by [@tannergolden](https://github.com/tannergolden).

</div>

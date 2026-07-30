<!--
title: '🤝 CONTRIBUTING GUIDELINES'
description: 'The default contribution workflow, commit standard, and pull request process for repositories owned by @tannergolden.'
tags: [contributing, pull-requests, conventional-commits, code-quality]
category: community
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

## 🎯 Our Philosophy

We value **small, frequent, and high-quality** contributions that adhere to established patterns.
Every change should move the project closer to being more stable, secure, and maintainable. We do
not accept "code dumps". Every line should be justified and tested.

---

## 🏗️ Getting Started

### 1. Prepare Your Environment

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
- **Naming convention:** use a descriptive prefix:
  - `feat/short-description`
  - `fix/issue-description`
  - `docs/what-changed`

---

## 🧱 Development Standards

### Commit Messages

We use **[Conventional Commits](https://www.conventionalcommits.org/)** (`type(scope): summary`).
Release tooling reads these messages to generate changelogs and determine version numbers, so the
format is load-bearing rather than cosmetic.

- **Format:** `type(scope): summary`
- **Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`,
  `revert`, `security`

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

## 🌿 The Pull Request Process

### 1. Opening the PR

- Target the default branch.
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

---

<div align="center">

**Structured contributions. Predictable growth.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by [@tannergolden](https://github.com/tannergolden). Distributed under the MIT License.

</div>

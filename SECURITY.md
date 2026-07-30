<!--
title: '🛡️ SECURITY POLICY'
description: 'The default private vulnerability reporting process, response targets, and baseline protections for this account.'
tags: [security, vulnerability-reporting, responsible-disclosure]
category: security
-->

<!-- markdownlint-disable MD041 -->

<div align="center">

# 🛡️ SECURITY POLICY

<a name="top"></a>

**A transparent, responsible process for finding and fixing vulnerabilities.**

_Report privately. Patch quickly. Disclose responsibly._

</div>

---

> [!NOTE]
> This is the **default security policy** for repositories owned by
> [@tannergolden](https://github.com/tannergolden). It applies to any repository that does not
> publish its own `SECURITY.md`. Where a repository ships its own policy, that policy wins.

---

## 💡 Overview

Security is treated as a shared responsibility: repositories here ship hardened defaults, and
every project remains responsible for its own security posture.

> [!IMPORTANT]
> If you believe you have found a security vulnerability, please follow the process below.
> **Do not open a public issue.** A public report discloses the vulnerability to everyone,
> including people who would exploit it, before a fix exists.

---

## ✅ Supported Versions

Unless a repository states otherwise, **only the latest release receives security patches**, and
fixes land on the default branch first. Older tags and branches are provided as-is.

---

## 🛡️ Reporting a Vulnerability

### 1. Submit the Report

Use **GitHub's private vulnerability reporting**: open the affected repository's **Security** tab
and click **Report a vulnerability**. This keeps the report private between you and the
maintainers, and no email is required.

If private reporting is not enabled on that repository, submit a private vulnerability report
against this repository instead:
[Report a vulnerability](https://github.com/tannergolden/.github/security/advisories/new), naming
the affected project in the report.

### 2. Required Information

Please provide a factual summary to assist triage:

- A description of the vulnerability and the component it affects.
- Steps to reproduce, ideally from a clean clone.
- The potential impact, and any known mitigations or workarounds.

### 3. Response Timeline

- **Acknowledgment**: expected within **24 hours**.
- **Status update**: a preliminary assessment or plan within **7 days**.

These are targets for a best-effort maintained project, not a contractual SLA.

### 4. Credit for Reporters

We **credit every reporter** who responsibly discloses a valid vulnerability. Unless you ask to
remain anonymous, your name or handle is acknowledged in the security advisory and in the release
notes for the fix. Recognition is the least we owe the people who keep the community safe, so tell us
how you would like to be credited when you report.

---

## 🚫 Please Do Not

- Open a public issue, discussion, or pull request describing the vulnerability.
- Test against infrastructure you do not own, or in ways that degrade service for others.
- Access, modify, or exfiltrate data that is not yours.

Good-faith researchers who follow this policy will not face legal action or referral to law
enforcement.

---

## ⚙️ Baseline Protections

Repositories here generally enable:

- **Secret scanning**: automated detection of committed credentials.
- **Dependency updates**: scheduled dependency checks with automated pull requests for known
  security advisories.
- **Static analysis**: code scanning for common vulnerable patterns.
- **Dependency review**: flags vulnerable packages introduced by a pull request.

Individual repositories may enable more. Check the repository's Security tab for what is active
there.

---

<div align="center">

**Proactive security. Responsible disclosure.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by [@tannergolden](https://github.com/tannergolden).

</div>

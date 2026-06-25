# ROADMAP.md – Transaction Tracker

## Overview
The **Transaction Tracker** library provides a lightweight, extensible API for detecting, diagnosing, and recommending resolutions for transaction‑related issues in any system (e‑commerce, fintech, ERP, etc.). This roadmap outlines the concrete milestones needed to ship a market‑validated MVP and then iteratively expand the product into a full‑featured, enterprise‑grade solution.

---

## 📅 Milestones & Timeline

| Milestone | Target Date | Scope | MVP‑Critical? |
|-----------|-------------|-------|---------------|
| **MVP – Core Engine** | **2026‑07‑31** | • `TransactionTracker` class<br>• `add_transaction` API<br>• `detect_issues` (rule‑based detection)<br>• `diagnose_issue` (basic root‑cause mapping)<br>• `get_recommended_resolution` (static suggestions)<br>• Unit‑test coverage ≥ 80%<br>• CI pipeline with static analysis | **Yes** |
| **v1 – Extensibility & Observability** | 2026‑10‑15 | • Plugin system for custom detection rules<br>• Metrics export (Prometheus) & logging (structured JSON)<br>• Configurable severity levels & alert thresholds<br>• Documentation site (MkDocs) + API reference<br>• Performance benchmark suite | No |
| **v2 – AI‑Powered Diagnosis** | 2027‑02‑28 | • Integration with vLLM for LLM‑based issue explanation<br>• Context‑aware resolution suggestions (using transaction history)<br>• Adaptive learning: feedback loop to improve rule set<br>• Multi‑tenant support & RBAC<br>• Export to common incident‑management tools (PagerDuty, Opsgenie) | No |
| **v3 – Enterprise Suite** | 2027‑07‑31 | • Distributed deployment (Docker, Helm chart)<br>• High‑availability clustering & state replication<br>• SLA dashboards & SLA‑driven alerting<br>• Compliance templates (PCI‑DSS, GDPR)<br>• Marketplace for third‑party rule packs | No |

---

## 🚀 MVP – Core Engine (Must‑Have for Launch)

| Feature | Description | Acceptance Criteria |
|---------|-------------|----------------------|
| **Transaction Model** | Simple immutable data class (`transaction_id`, `timestamp`, `amount`, `status`, `metadata`). | Can be instantiated from dict/JSON; validated fields raise clear errors. |
| **`add_transaction`** | In‑memory store with optional persistence hook. | Stores transaction; duplicate IDs are rejected with `TransactionExistsError`. |
| **Rule‑Based Detection** | Built‑in rule set (e.g., duplicate IDs, out‑of‑order timestamps, amount spikes, status regressions). | `detect_issues()` returns a list of `Issue` objects with `code`, `severity`, `transaction_id`. |
| **Diagnosis Engine** | Maps each `Issue.code` to a static root‑cause description. | `diagnose_issue(issue)` returns a non‑empty string explaining the cause. |
| **Resolution Recommendations** | Pre‑defined remediation steps per issue type. | `get_recommended_resolution(issue)` returns actionable steps (e.g., “re‑process transaction”, “alert ops”). |
| **Testing & CI** | PyTest suite, coverage ≥ 80%, GitHub Actions pipeline with linting (ruff) and type‑checking (mypy). | All tests pass on every push; coverage badge updates automatically. |
| **Packaging** | Publishable wheel on PyPI, semantic versioning (`0.1.0`). | `pip install transaction-tracker` works on Python 3.9+. |
| **Documentation** | README with quick‑start, API reference generated via `pdoc`. | New user can run the example in the README without errors. |

---

## 🌱 v1 – Extensibility & Observability

| Theme | Key Deliverables |
|-------|------------------|
| **Plugin Architecture** | `register_rule(plugin_callable)` API; sandboxed execution; discovery via entry‑points. |
| **Metrics & Logging** | Export `transaction_tracker_detected_issues_total`, latency histograms; structured JSON logs with correlation IDs. |
| **Configurable Severity** | YAML/JSON config to map rule codes to `LOW/MEDIUM/HIGH` and alert thresholds. |
| **Docs & Site** | MkDocs site with versioned docs, API reference, and “How to write a plugin” guide. |
| **Performance Benchmarks** | Baseline < 5 ms per 1 k transactions; report generated on each release. |

---

## 🤖 v2 – AI‑Powered Diagnosis

| Theme | Key Deliverables |
|-------|------------------|
| **LLM Integration** | Wrapper around **vLLM** to generate natural‑language explanations for complex issues. |
| **Context‑Aware Recommendations** | Use transaction history embeddings (via `instr-resp` dataset) to suggest tailored fixes. |
| **Feedback Loop** | `feedback(issue_id, was_resolved)` endpoint that updates a lightweight model for rule weighting. |
| **Multi‑Tenant & RBAC** | Namespace isolation, API keys, role‑based permissions (viewer/editor/admin). |
| **Ops Integration** | Webhooks / outbound adapters for PagerDuty, Opsgenie, Slack. |

---

## 🏢 v3 – Enterprise Suite

| Theme | Key Deliverables |
|-------|------------------|
| **Distributed Deployment** | Docker image, Helm chart, Helm values for scaling, persistence (Redis/Postgres). |
| **HA & Replication** | Leader‑follower replication, automatic failover, state sync. |
| **SLA Dashboards** | Grafana dashboards showing detection latency, issue resolution time, uptime. |
| **Compliance Packs** | Pre‑built rule sets for PCI‑DSS, GDPR, and other regulatory frameworks. |
| **Marketplace** | Public repo of community‑contributed rule plugins, with rating & vetting workflow. |

---

## 📌 Success Metrics

| Metric | Target (by release) |
|--------|---------------------|
| **Adoption** | 50+ paying customers within 6 months of MVP launch. |
| **Detection Accuracy** | ≥ 95 % true‑positive rate on benchmark transaction logs. |
| **Mean Time to Resolution (MTTR)** | Reduce MTTR by 30 % vs. baseline for v2 customers. |
| **Customer NPS** | ≥ 70 after v2 rollout. |
| **Revenue** | $150k ARR by end of 2027‑02 (post‑v2). |

---

## 📚 References & Resources

- **Chain Playbook (2026‑06‑21)** – execution guidelines for each milestone.  
- **C. Frameworks** – vLLM (`vllm-project/vllm`) for LLM inference, SGLang for structured generation.  
- **Datasets** – `auto`, `instr-resp`, `messages`, `query-resp` (available in the BRAIN vector store) for training/validation of AI components.  
- **Existing Portfolio** – Ensure no overlap with `iceoryx2` IPC library; focus remains on transaction‑level analytics.  

--- 

*Prepared by the Product & Engineering Lead, Axentx OS – Transaction Tracker*

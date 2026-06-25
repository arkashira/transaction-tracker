# REQUIREMENTS.md

## Overview
The **Transaction Tracker** library provides a lightweight, programmatic way to ingest financial transaction records, automatically detect anomalies, diagnose root causes, and surface actionable remediation recommendations. It is intended for integration into fintech back‑ends, payment gateways, and accounting SaaS platforms that require real‑time or batch‑mode transaction health monitoring.

---

## 1. Functional Requirements

| ID | Description |
|----|-------------|
| **FR‑1** | **API Surface** – Expose a public class `TransactionTracker` with the following methods: <br>• `add_transaction(transaction: Transaction) -> None` <br>• `detect_issues() -> List[Issue]` <br>• `diagnose_issue(issue_id: str) -> Diagnosis` <br>• `get_recommended_resolution(issue_id: str) -> Resolution` |
| **FR‑2** | **Transaction Model** – Define an immutable `Transaction` data class containing at least: <br>• `id: str` (unique) <br>• `timestamp: datetime` (UTC) <br>• `amount: Decimal` (positive for credit, negative for debit) <br>• `currency: str` (ISO‑4217) <br>• `account_id: str` <br>• `metadata: Mapping[str, Any]` (optional free‑form fields) |
| **FR‑3** | **Issue Model** – Define an `Issue` data class with: <br>• `id: str` (UUID) <br>• `type: IssueType` (enumerated, e.g., `DUPLICATE`, `OUT_OF_ORDER`, `ANOMALOUS_AMOUNT`, `STALLED`) <br>• `affected_transaction_ids: List[str]` <br>• `detected_at: datetime` |
| **FR‑4** | **Diagnosis Model** – Define a `Diagnosis` data class containing: <br>• `issue_id: str` <br>• `root_cause: str` (human‑readable) <br>• `confidence: float` (0‑1) <br>• `evidence: List[str]` (excerpts of data that support the diagnosis) |
| **FR‑5** | **Resolution Model** – Define a `Resolution` data class with: <br>• `issue_id: str` <br>• `action: str` (e.g., `REVERSE`, `FLAG_FOR_REVIEW`, `IGNORE`) <br>• `instructions: str` (step‑by‑step guidance) |
| **FR‑6** | **Detection Rules** – Implement built‑in detection heuristics covering at minimum: <br>• Duplicate transaction IDs (within a configurable time window) <br>• Out‑of‑order timestamps for the same `account_id` <br>• Amount spikes using statistical outlier detection (median absolute deviation) <br>• Stalled processing (no new transactions for a configurable interval) |
| **FR‑7** | **Extensibility** – Allow users to register custom detection callbacks via `register_detector(name: str, func: Callable[[List[Transaction]], List[Issue]])`. Custom detectors must integrate seamlessly with the core pipeline. |
| **FR‑8** | **Persistence (Optional)** – Provide an in‑memory default store but expose an abstract `TransactionStore` interface so downstream systems can plug in DB‑backed implementations (e.g., PostgreSQL, Redis). |
| **FR‑9** | **Thread‑Safety** – All public methods must be safe to call from multiple threads concurrently. |
| **FR‑10** | **Logging** – Emit structured logs (JSON) for key events: transaction addition, issue detection, diagnosis, and resolution recommendation. Log level configurable at runtime. |
| **FR‑11** | **Versioning** – Expose `__version__` following Semantic Versioning (MAJOR.MINOR.PATCH). |
| **FR‑12** | **Packaging** – Distribute as a pip‑installable wheel compatible with Python 3.9‑3.12, with type hints and a `py.typed` marker. |

---

## 2. Non‑Functional Requirements

| ID | Requirement |
|----|-------------|
| **NFR‑1** | **Performance** – Detect issues on a batch of up to **10,000** transactions in **≤ 150 ms** on a single‑core 2.5 GHz CPU. |
| **NFR‑2** | **Scalability** – The library must support streaming mode where transactions are processed incrementally; memory footprint must not exceed **O(N)** where *N* is the number of unique `account_id`s retained for out‑of‑order checks (configurable default 100,000). |
| **NFR‑3** | **Security** – All public APIs must validate input types and reject malformed data with explicit exceptions (`InvalidTransactionError`, `InvalidIssueError`). No external network calls are permitted. |
| **NFR‑4** | **Reliability** – The library must guarantee **no loss** of added transactions even under concurrent access; internal queues must be lock‑free where possible. |
| **NFR‑5** | **Observability** – Provide a Prometheus‑compatible metrics endpoint (optional) exposing counters: `transactions_added_total`, `issues_detected_total`, `diagnoses_generated_total`, and latency histograms for each pipeline stage. |
| **NFR‑6** | **Documentation** – Auto‑generated API reference via `mkdocs` and a README with usage examples covering both batch and streaming modes. |
| **NFR‑7** | **Testing** – Achieve **≥ 90 %** statement coverage with unit tests, plus integration tests for custom detector registration and persistence plug‑ins. |
| **NFR‑8** | **Compatibility** – Must run on Linux, macOS, and Windows without native dependencies; pure‑Python implementation preferred, but optional C extensions must fall back gracefully. |
| **NFR‑9** | **Internationalization** – All user‑facing strings (diagnoses, resolutions) must be externalizable for future i18n; default language English. |
| **NFR‑10** | **License** – Distributed under the **Apache‑2.0** license, compatible with downstream commercial use. |

---

## 3. Constraints

1. **No External Services** – The library must operate fully offline; any ML‑based heuristics must be pre‑trained and bundled or derived from deterministic statistical methods.
2. **Dependency Policy** – Only depend on actively maintained packages with permissive licenses (e.g., `pandas`, `numpy`, `prometheus_client`). Total runtime dependency weight must stay under **15 MB**.
3. **Version Compatibility** – Must maintain backward compatibility for the public API across minor releases (MAJOR version bump only for breaking changes).
4. **Resource Limits** – Must not exceed **200 MB** RAM when processing the maximum batch size defined in NFR‑1 on a typical cloud VM (2 vCPU, 4 GB RAM).

---

## 4. Assumptions

| ID | Assumption |
|----|------------|
| **A‑1** | Consumers will provide timestamps in UTC; the library does not perform timezone conversion. |
| **A‑2** | Transaction IDs are globally unique; duplicate detection is based on exact string match. |
| **A‑3** | Currency codes follow ISO‑4217; conversion or exchange‑rate handling is out of scope. |
| **A‑4** | Users requiring persistent storage will implement `TransactionStore`; the default in‑memory store is sufficient for most unit‑test and demo scenarios. |
| **A‑5** | The statistical outlier detection parameters (e.g., MAD multiplier) are configurable via a `TrackerConfig` object. |
| **A‑6** | The library will be used as a dependency, not as a standalone service; therefore, no HTTP server is provided except optional metrics exposition. |
| **A‑7** | The target audience has Python development experience and can install binary wheels; building from source is supported but not required. |

---

## 5. Acceptance Criteria

- All functional requirements FR‑1 – FR‑12 are implemented and pass unit/integration tests.
- Non‑functional thresholds NFR‑1 – NFR‑10 are validated via benchmark and CI pipelines.
- Documentation builds without errors and includes a “Getting Started” guide.
- The package publishes to the internal PyPI registry with the correct version tag and license metadata.

--- 

*Prepared by: Senior Product/Engineering Lead*  
*Date: 2026‑06‑25*

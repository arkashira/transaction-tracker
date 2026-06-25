# STORIES.md

## Overview
The **Transaction Tracker** library helps developers detect, diagnose, and resolve transaction‑related problems (e.g., deadlocks, timeouts, data inconsistencies) in their applications.  
The backlog below is organized into **Epics** that map to the core workflow:

1. **Core Tracking & Detection** – basic API, data model, and issue detection.  
2. **Diagnosis & Recommendation** – turn raw detection data into actionable insights.  
3. **Observability & Integration** – logging, metrics, and easy integration with existing codebases.  
4. **Configuration & Extensibility** – custom rules, plug‑in support, and runtime configurability.  
5. **Quality & Documentation** – tests, CI, and user documentation.

Stories are ordered to deliver a **Minimum Viable Product (MVP)** that provides a usable library with reliable detection and clear guidance for developers.

---

## EPIC 1 – Core Tracking & Detection

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 1 | **As a developer, I want to instantiate a `TransactionTracker` so that I can start tracking transactions in my app.** | - `TransactionTracker()` can be created with no arguments.<br>- Constructor accepts optional config object (future‑proof).<br>- Instance exposes `add_transaction`, `detect_issues` methods. |
| 2 | **As a developer, I want to add a transaction record with its metadata so that the tracker has the data needed for analysis.** | - `add_transaction(id: str, start_ts: datetime, end_ts: datetime, status: Enum, payload: dict)` stores the record.<br>- Duplicate `id` raises a clear `TransactionExistsError`.<br>- Invalid timestamps raise `InvalidTimestampError`. |
| 3 | **As a developer, I want the tracker to automatically flag transactions that exceed a configurable latency threshold so that I can spot slow operations.** | - Default latency threshold = 2 seconds (configurable).<br>- `detect_issues()` returns a list containing an `Issue` object with type `LATENCY_EXCEEDED` for each offending transaction.<br>- Issue includes `transaction_id`, `observed_latency`, `threshold`. |
| 4 | **As a developer, I want the tracker to detect overlapping transactions that share the same resource ID so that I can identify potential deadlocks.** | - `add_transaction` can include optional `resource_ids: List[str]`.<br>- `detect_issues()` returns `Issue` type `RESOURCE_CONTENTION` when two or more active transactions overlap on any resource.<br>- Overlap detection respects start/end timestamps. |
| 5 | **As a developer, I want a deterministic `detect_issues` call that does not mutate internal state so that I can run it repeatedly in tests.** | - Calling `detect_issues()` multiple times without new data yields identical results.<br>- No transaction records are removed or altered by detection. |

---

## EPIC 2 – Diagnosis & Recommendation

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 6 | **As a developer, I want to retrieve a human‑readable diagnosis for a specific issue so that I understand why it happened.** | - `diagnose_issue(issue_id: str)` returns a string explanation.<br>- Explanation includes root cause (e.g., “Latency exceeded 2 s”) and affected transaction details. |
| 7 | **As a developer, I want the library to suggest a concrete resolution for each diagnosed issue so that I can act quickly.** | - `get_recommended_resolution(issue_id: str)` returns a list of actionable steps (e.g., “Increase DB connection pool size”, “Add index on column X”).<br>- Recommendations are tied to issue type and include optional code snippets. |
| 8 | **As a developer, I want to batch‑diagnose all detected issues so that I can get a single report for a run.** | - `diagnose_all()` returns a dict `{issue_id: {diagnosis, recommendation}}` for every issue returned by the latest `detect_issues()` call.<br>- The method is O(n) in the number of issues. |

---

## EPIC 3 – Observability & Integration

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 9 | **As a DevOps engineer, I want the tracker to emit structured logs for every detected issue so that they can be ingested by log aggregators.** | - Uses Python `logging` module with JSON formatter.<br>- Log entry includes `timestamp`, `issue_id`, `type`, `severity`, `transaction_id`. |
| 10 | **As a site reliability engineer, I want the tracker to expose Prometheus metrics for issue counts and latency statistics so that I can monitor health in dashboards.** | - Metrics: `transaction_tracker_issues_total{type="latency_exceeded"}`, `transaction_tracker_average_latency_seconds`.<br>- Exported via `start_http_server(port)` from `prometheus_client`. |
| 11 | **As a developer, I want a context‑manager wrapper that automatically records start/end timestamps so that I can instrument code with minimal boilerplate.** | - `with tracker.track(id, resource_ids=…) as tx:` automatically calls `add_transaction` on exit.<br>- Handles exceptions: if exception occurs, status set to `FAILED`. |
| 12 | **As a developer, I want the library to be installable via pip and importable as `transaction_tracker` so that integration is straightforward.** | - `setup.py`/`pyproject.toml` builds a wheel.<br>- `pip install transaction-tracker` works on Python 3.9+. |
| 13 | **As a developer, I want type hints and docstrings for all public methods so that IDEs provide autocomplete and my team can generate API docs.** | - All public functions/classes are annotated with `typing`.<br>- Docstrings follow Google style and include examples. |

---

## EPIC 4 – Configuration & Extensibility

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 14 | **As a power user, I want to supply custom detection rules (e.g., custom latency thresholds per transaction type) so that the tracker fits my domain.** | - `TransactionTracker(config: TrackerConfig)` where `TrackerConfig` can include per‑type thresholds.<br>- Custom rule objects implement `detect(transactions) -> List[Issue]` and can be registered via `register_rule(rule)`. |
| 15 | **As a developer, I want to plug in my own recommendation engine so that the library can leverage proprietary knowledge bases.** | - `set_recommendation_provider(provider: RecommendationProvider)` where provider implements `recommend(issue) -> List[str]`.<br>- Default provider supplies generic suggestions. |

---

## EPIC 5 – Quality & Documentation

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 16 | **As a QA engineer, I want a comprehensive test suite with unit and integration tests covering >90 % of the codebase so that regressions are caught early.** | - `pytest` suite with coverage report ≥ 90 %.<br>- CI pipeline runs tests on Linux, macOS, Windows. |
| 17 | **As a new user, I want a quick‑start guide in the README that shows how to add a transaction and detect issues in under 5 minutes.** | - README contains a “Getting Started” section with a runnable code snippet.<br>- Example produces at least one latency issue. |
| 18 | **As a maintainer, I want automated release notes generated from merged PR titles so that version bumps are transparent.** | - GitHub Action uses `release-drafter` to draft notes on each merge to `main`. |

---

## MVP Scope (Stories 1‑9)

To ship the first production‑ready version we will implement:

1. Core tracking & detection (Stories 1‑5).  
2. Diagnosis & recommendation for individual issues (Stories 6‑8).  
3. Basic observability: logging and pip‑installable package (Stories 9‑12).  

Stories 13‑18 will be delivered in subsequent sprints to improve developer experience, extensibility, and operational maturity.

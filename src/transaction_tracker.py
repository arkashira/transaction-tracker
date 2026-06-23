import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

@dataclass
class Transaction:
    id: int
    timestamp: datetime
    amount: float
    status: str

class TransactionTracker:
    def __init__(self):
        self.transactions: List[Transaction] = []

    def add_transaction(self, transaction: Transaction):
        """Add a transaction to the internal list."""
        self.transactions.append(transaction)

    def detect_issues(self) -> List[Transaction]:
        """
        Return a list of transactions that have a non‑success status and are older
        than 5 minutes (i.e., the issue has persisted long enough to be considered
        actionable).
        """
        issues = []
        now = datetime.now()
        for transaction in self.transactions:
            if transaction.status != "success" and transaction.timestamp + timedelta(minutes=5) < now:
                issues.append(transaction)
        return issues

    def diagnose_issue(self, transaction: Transaction) -> str:
        """
        Diagnose a transaction based on its amount.

        - Amount **greater than or equal to** 1000 is considered a high‑value issue.
        - Anything lower is a low‑value issue.
        """
        if transaction.amount >= 1000:
            return "High value transaction issue"
        else:
            return "Low value transaction issue"

    def resolve_issue(self, transaction: Transaction) -> str:
        """
        Provide a resolution recommendation based on the diagnosis.

        - High‑value issues require manual review.
        - Low‑value issues can be handled automatically.
        """
        diagnosis = self.diagnose_issue(transaction)
        if diagnosis == "High value transaction issue":
            return "Manual review required"
        else:
            return "Automated resolution applied"

    def get_recommended_resolution(self, transaction: Transaction) -> str:
        """Convenience wrapper that returns the resolution for a given transaction."""
        return self.resolve_issue(transaction)

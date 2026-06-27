import json
from dataclasses import dataclass
from typing import List

@dataclass
class Transaction:
    id: int
    status: str
    issue: str

class TransactionTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def get_transactions(self, status: str = None, issue: str = None):
        filtered_transactions = self.transactions.copy()
        if status:
            filtered_transactions = [t for t in filtered_transactions if t.status == status]
        if issue:
            filtered_transactions = [t for t in filtered_transactions if t.issue == issue]
        return filtered_transactions

    def sort_transactions(self, key: str):
        return sorted(self.transactions, key=lambda x: getattr(x, key))

    def resolve_issue(self, transaction_id: int, resolution: str):
        for transaction in self.transactions:
            if transaction.id == transaction_id:
                transaction.issue = resolution
                return
        raise ValueError("Transaction not found")

    def to_json(self):
        return json.dumps([t.__dict__ for t in self.transactions])

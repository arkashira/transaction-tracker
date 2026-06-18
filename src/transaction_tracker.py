import json
from dataclasses import dataclass
from enum import Enum
from typing import List

class TransactionStatus(Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"

@dataclass
class Transaction:
    id: int
    status: TransactionStatus
    amount: float

class AutomatedTroubleshootingModule:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def identify_and_resolve_common_issues(self):
        resolved_transactions = []
        for transaction in self.transactions:
            if transaction.status == TransactionStatus.PENDING:
                # Simulate resolving pending transactions
                transaction.status = TransactionStatus.SUCCESS
                resolved_transactions.append(transaction)
        return resolved_transactions

    def provide_real_time_status_updates(self):
        updates = []
        for transaction in self.transactions:
            updates.append({
                "id": transaction.id,
                "status": transaction.status.value
            })
        return updates

    def send_notifications(self, transactions: List[Transaction]):
        notifications = []
        for transaction in transactions:
            notifications.append({
                "id": transaction.id,
                "status": transaction.status.value
            })
        return notifications

import json
from dataclasses import dataclass
from enum import Enum
from typing import List

class TransactionStatus(Enum):
    PENDING = 1
    SUCCESS = 2
    FAILED = 3

@dataclass
class Transaction:
    id: int
    status: TransactionStatus

class AutomatedTroubleshootingModule:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def identify_and_resolve_common_issues(self):
        resolved_transactions = []
        for transaction in self.transactions:
            if transaction.status == TransactionStatus.PENDING:
                # Simulate resolution of common issues
                transaction.status = TransactionStatus.SUCCESS
                resolved_transactions.append(transaction)
        return resolved_transactions

    def provide_real_time_status_updates(self):
        updates = []
        for transaction in self.transactions:
            updates.append({"id": transaction.id, "status": transaction.status.name})
        return updates

    def send_notifications(self, updates: List[dict]):
        # Simulate sending notifications
        print("Sending notifications:")
        for update in updates:
            print(f"Transaction {update['id']} is {update['status']}")

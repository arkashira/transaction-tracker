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
    amount: float

class TransactionTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def get_transaction_status(self, transaction_id: int) -> TransactionStatus:
        for transaction in self.transactions:
            if transaction.id == transaction_id:
                return transaction.status
        return None

    def automate_troubleshooting(self, transaction_id: int) -> str:
        transaction_status = self.get_transaction_status(transaction_id)
        if transaction_status == TransactionStatus.FAILED:
            return "Troubleshooting initiated for transaction {}".format(transaction_id)
        else:
            return "No troubleshooting needed for transaction {}".format(transaction_id)

    def provide_real_time_status_update(self, transaction_id: int) -> str:
        transaction_status = self.get_transaction_status(transaction_id)
        if transaction_status:
            return "Transaction {} status: {}".format(transaction_id, transaction_status.name)
        else:
            return "Transaction {} not found".format(transaction_id)

    def send_notification(self, transaction_id: int, message: str) -> None:
        print("Notification sent for transaction {}: {}".format(transaction_id, message))

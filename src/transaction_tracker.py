import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

@dataclass
class Transaction:
    id: int
    status: str
    timestamp: datetime

class TransactionTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def get_transaction_status(self, transaction_id: int):
        for transaction in self.transactions:
            if transaction.id == transaction_id:
                return transaction.status
        return None

    def get_delayed_transactions(self):
        delayed_transactions = []
        for transaction in self.transactions:
            if transaction.status == "delayed":
                delayed_transactions.append(transaction)
        return delayed_transactions

    def get_failed_transactions(self):
        failed_transactions = []
        for transaction in self.transactions:
            if transaction.status == "failed":
                failed_transactions.append(transaction)
        return failed_transactions

    def send_notifications(self):
        delayed_transactions = self.get_delayed_transactions()
        failed_transactions = self.get_failed_transactions()
        notifications = []
        for transaction in delayed_transactions + failed_transactions:
            notification = {
                "transaction_id": transaction.id,
                "status": transaction.status,
                "timestamp": transaction.timestamp.isoformat()
            }
            notifications.append(notification)
        return notifications

    def get_transaction_history(self):
        return self.transactions

    def get_real_time_status_updates(self):
        return [transaction.status for transaction in self.transactions]

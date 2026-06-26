import json
from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Transaction:
    id: int
    timestamp: datetime
    merchant_id: int
    status: str

class TransactionTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def get_transactions(self, start_date: datetime = None, end_date: datetime = None, merchant_id: int = None, status: str = None):
        filtered_transactions = self.transactions.copy()
        if start_date:
            filtered_transactions = [t for t in filtered_transactions if t.timestamp >= start_date]
        if end_date:
            filtered_transactions = [t for t in filtered_transactions if t.timestamp <= end_date]
        if merchant_id:
            filtered_transactions = [t for t in filtered_transactions if t.merchant_id == merchant_id]
        if status:
            filtered_transactions = [t for t in filtered_transactions if t.status == status]
        return filtered_transactions

    def get_failed_transactions(self):
        return [t for t in self.transactions if t.status == 'Failed']

def color_code_status(status: str):
    if status == 'Failed':
        return '\033[91m' + status + '\033[0m'
    else:
        return status

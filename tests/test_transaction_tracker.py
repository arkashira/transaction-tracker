import pytest
from datetime import datetime, timedelta
from transaction_tracker import Transaction, TransactionTracker, color_code_status

@pytest.fixture
def transaction_tracker():
    return TransactionTracker()

def test_add_transaction(transaction_tracker):
    transaction = Transaction(1, datetime.now(), 1, 'Pending')
    transaction_tracker.add_transaction(transaction)
    assert len(transaction_tracker.transactions) == 1

def test_get_transactions(transaction_tracker):
    transaction1 = Transaction(1, datetime.now(), 1, 'Pending')
    transaction2 = Transaction(2, datetime.now() + timedelta(seconds=1), 1, 'Success')
    transaction_tracker.add_transaction(transaction1)
    transaction_tracker.add_transaction(transaction2)
    transactions = transaction_tracker.get_transactions()
    assert len(transactions) == 2

def test_get_transactions_with_filter(transaction_tracker):
    transaction1 = Transaction(1, datetime.now(), 1, 'Pending')
    transaction2 = Transaction(2, datetime.now() + timedelta(seconds=1), 2, 'Success')
    transaction_tracker.add_transaction(transaction1)
    transaction_tracker.add_transaction(transaction2)
    transactions = transaction_tracker.get_transactions(merchant_id=1)
    assert len(transactions) == 1

def test_get_failed_transactions(transaction_tracker):
    transaction1 = Transaction(1, datetime.now(), 1, 'Failed')
    transaction2 = Transaction(2, datetime.now() + timedelta(seconds=1), 1, 'Success')
    transaction_tracker.add_transaction(transaction1)
    transaction_tracker.add_transaction(transaction2)
    failed_transactions = transaction_tracker.get_failed_transactions()
    assert len(failed_transactions) == 1

def test_color_code_status():
    assert color_code_status('Failed') == '\x1b[91mFailed\x1b[0m'
    assert color_code_status('Success') == 'Success'

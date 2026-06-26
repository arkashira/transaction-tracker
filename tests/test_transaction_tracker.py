from transaction_tracker import Transaction, TransactionTracker
import pytest
from datetime import datetime, timedelta

def test_add_transaction():
    tracker = TransactionTracker()
    transaction = Transaction(1, "pending", datetime.now())
    tracker.add_transaction(transaction)
    assert tracker.get_transaction_status(1) == "pending"

def test_get_transaction_status():
    tracker = TransactionTracker()
    transaction = Transaction(1, "pending", datetime.now())
    tracker.add_transaction(transaction)
    assert tracker.get_transaction_status(1) == "pending"
    assert tracker.get_transaction_status(2) is None

def test_get_delayed_transactions():
    tracker = TransactionTracker()
    transaction1 = Transaction(1, "delayed", datetime.now())
    transaction2 = Transaction(2, "pending", datetime.now())
    tracker.add_transaction(transaction1)
    tracker.add_transaction(transaction2)
    delayed_transactions = tracker.get_delayed_transactions()
    assert len(delayed_transactions) == 1
    assert delayed_transactions[0].id == 1

def test_get_failed_transactions():
    tracker = TransactionTracker()
    transaction1 = Transaction(1, "failed", datetime.now())
    transaction2 = Transaction(2, "pending", datetime.now())
    tracker.add_transaction(transaction1)
    tracker.add_transaction(transaction2)
    failed_transactions = tracker.get_failed_transactions()
    assert len(failed_transactions) == 1
    assert failed_transactions[0].id == 1

def test_send_notifications():
    tracker = TransactionTracker()
    transaction1 = Transaction(1, "delayed", datetime.now())
    transaction2 = Transaction(2, "failed", datetime.now())
    tracker.add_transaction(transaction1)
    tracker.add_transaction(transaction2)
    notifications = tracker.send_notifications()
    assert len(notifications) == 2
    assert notifications[0]["transaction_id"] == 1
    assert notifications[1]["transaction_id"] == 2

def test_get_transaction_history():
    tracker = TransactionTracker()
    transaction1 = Transaction(1, "pending", datetime.now())
    transaction2 = Transaction(2, "delayed", datetime.now())
    tracker.add_transaction(transaction1)
    tracker.add_transaction(transaction2)
    history = tracker.get_transaction_history()
    assert len(history) == 2
    assert history[0].id == 1
    assert history[1].id == 2

def test_get_real_time_status_updates():
    tracker = TransactionTracker()
    transaction1 = Transaction(1, "pending", datetime.now())
    transaction2 = Transaction(2, "delayed", datetime.now())
    tracker.add_transaction(transaction1)
    tracker.add_transaction(transaction2)
    status_updates = tracker.get_real_time_status_updates()
    assert len(status_updates) == 2
    assert status_updates[0] == "pending"
    assert status_updates[1] == "delayed"

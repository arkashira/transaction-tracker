import json
from transaction_tracker import Transaction, TransactionTracker

def test_add_transaction():
    tracker = TransactionTracker()
    transaction = Transaction(1, "pending", "none")
    tracker.add_transaction(transaction)
    assert len(tracker.get_transactions()) == 1

def test_get_transactions():
    tracker = TransactionTracker()
    transaction1 = Transaction(1, "pending", "none")
    transaction2 = Transaction(2, "failed", "error")
    tracker.add_transaction(transaction1)
    tracker.add_transaction(transaction2)
    assert len(tracker.get_transactions(status="pending")) == 1
    assert len(tracker.get_transactions(issue="error")) == 1

def test_sort_transactions():
    tracker = TransactionTracker()
    transaction1 = Transaction(1, "pending", "none")
    transaction2 = Transaction(2, "failed", "error")
    tracker.add_transaction(transaction1)
    tracker.add_transaction(transaction2)
    sorted_transactions = tracker.sort_transactions("id")
    assert sorted_transactions[0].id == 1

def test_resolve_issue():
    tracker = TransactionTracker()
    transaction = Transaction(1, "pending", "error")
    tracker.add_transaction(transaction)
    tracker.resolve_issue(1, "resolved")
    assert tracker.get_transactions()[0].issue == "resolved"

def test_to_json():
    tracker = TransactionTracker()
    transaction = Transaction(1, "pending", "none")
    tracker.add_transaction(transaction)
    json_data = tracker.to_json()
    assert json.loads(json_data)[0]["id"] == 1

def test_resolve_issue_not_found():
    tracker = TransactionTracker()
    transaction = Transaction(1, "pending", "error")
    tracker.add_transaction(transaction)
    try:
        tracker.resolve_issue(2, "resolved")
        assert False
    except ValueError:
        assert True

from transaction_tracker import Transaction, TransactionTracker
import pytest
from datetime import datetime, timedelta

def test_add_transaction():
    tracker = TransactionTracker()
    transaction = Transaction(1, datetime.now(), 100.0, "success")
    tracker.add_transaction(transaction)
    assert len(tracker.transactions) == 1

def test_detect_issues():
    tracker = TransactionTracker()
    transaction1 = Transaction(1, datetime.now() - timedelta(minutes=10), 100.0, "failed")
    transaction2 = Transaction(2, datetime.now(), 100.0, "success")
    tracker.add_transaction(transaction1)
    tracker.add_transaction(transaction2)
    issues = tracker.detect_issues()
    assert len(issues) == 1
    assert issues[0].id == 1

def test_diagnose_issue():
    tracker = TransactionTracker()
    transaction = Transaction(1, datetime.now(), 1000.0, "failed")
    diagnosis = tracker.diagnose_issue(transaction)
    assert diagnosis == "High value transaction issue"

def test_resolve_issue():
    tracker = TransactionTracker()
    transaction = Transaction(1, datetime.now(), 1000.0, "failed")
    resolution = tracker.resolve_issue(transaction)
    assert resolution == "Manual review required"

def test_get_recommended_resolution():
    tracker = TransactionTracker()
    transaction = Transaction(1, datetime.now(), 100.0, "failed")
    resolution = tracker.get_recommended_resolution(transaction)
    assert resolution == "Automated resolution applied"

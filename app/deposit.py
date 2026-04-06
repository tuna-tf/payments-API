# app/deposit.py

def deposit(balance: float, amount: float) -> float:
    """Return a new balance after depositing amount."""
    if amount <= 0:
        raise ValueError("Deposit amount must be positive")
    return balance + amount
# app/withdraw.py

def withdraw(balance: float, amount: float) -> float:
    """Return a new balance after withdrawing amount."""
    if amount <= 0:
        raise ValueError("Withdraw amount must be positive")
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount
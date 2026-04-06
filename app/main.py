from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .deposit import deposit
from .withdraw import withdraw
from .database import get_connection

app = FastAPI()

class Item(BaseModel):
    amount: float

"""// | read balance"""
@app.get("/")
async def read_balance(userID: int):
    conn = await get_connection()

    try:
        balance = await conn.fetchval(
            "SELECT balance FROM users WHERE userID = $1",
            userID,
        )

        if balance is None:
            raise HTTPException(status_code=404, detail="User not found")

        return {"balance": balance}
    finally:
        await conn.close()

"""// | deposit"""
@app.put("/items/{userID}/deposit")
async def deposit_money(userID: int, item: Item):
    conn = await get_connection()

    try:
        balance = await conn.fetchval(
            "SELECT balance FROM users WHERE userID = $1",
            userID,
        )

        if balance is None:
            raise HTTPException(status_code=404, detail="User not found")

        try:
            new_balance = deposit(balance, item.amount)
        except ValueError as error:
            raise HTTPException(status_code=400, detail=str(error)) from error

        await conn.execute(
            "UPDATE users SET balance = $1 WHERE userID = $2",
            new_balance,
            userID,
        )
    finally:
        await conn.close()

    return {"deposit_balance": new_balance}

"""// | withdraw"""
@app.put("/items/{userID}/withdraw")
async def withdraw_money(userID: int, item: Item):
    conn = await get_connection()

    try:
        balance = await conn.fetchval(
            "SELECT balance FROM users WHERE userID = $1",
            userID,
        )

        if balance is None:
            raise HTTPException(status_code=404, detail="User not found")

        try:
            new_balance = withdraw(balance, item.amount)
        except ValueError as error:
            raise HTTPException(status_code=400, detail=str(error)) from error

        await conn.execute(
            "UPDATE users SET balance = $1 WHERE userID = $2",
            new_balance,
            userID,
        )
    finally:
        await conn.close()

    return {"withdraw_value": new_balance}


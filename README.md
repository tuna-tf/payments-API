# Simple Payment API

A simple payment API built with FastAPI that lets you:

- make a deposit with a `PUT` request
- make a withdraw with a `PUT` request
- view a user's balance with a `GET` request

## Endpoints

- `GET /?userID={userID}`: View the user's current balance
- `PUT /items/{userID}/deposit`: Deposit money into the user's account
- `PUT /items/{userID}/withdraw`: Withdraw money from the user's account

## Tools Used

- Web: FastAPI
- Server: uvicorn
- DB: PostgreSQL

## Python Packages Used

- `fastapi`
- `uvicorn[standard]`
- `sqlalchemy`
- `asyncpg`
- `pydantic`

## Run the API

```bash
uvicorn app.main:app --reload
```

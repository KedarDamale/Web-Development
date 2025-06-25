"""

In **FastAPI**, understanding **sync** vs **async** is **crucial for writing efficient and scalable APIs**. These two terms refer to **how your Python code is executed** — synchronously (blocking) or asynchronously (non-blocking). Let’s go into *extreme detail* so you understand what’s really happening.

---

## 🔁 1. **What is Synchronous (sync) Execution?**

**Sync functions** are regular Python functions defined using `def`. They **block** the execution until the task is completed.

### ✅ Characteristics:

* Executes code **line by line**, **waiting** for each line to finish.
* Suitable for **CPU-bound** tasks.
* Uses **Python’s default execution model**.
* Works well with **I/O operations** that are fast or minimal (e.g., in-memory DB).

### ⏳ Blocking Example:

```python
from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/sync-task")
def sync_task():
    time.sleep(5)  # Blocks the entire thread
    return {"message": "Finished sync task"}
```

* `time.sleep(5)` halts the process for 5 seconds.
* During this time, the **worker thread is locked**, and **no other request can be processed** by that thread.

---

## 🔄 2. **What is Asynchronous (async) Execution?**

**Async functions** are defined using `async def`. They allow **non-blocking I/O operations** using Python's `asyncio` library.

### ✅ Characteristics:

* Use `await` to **pause execution** and **yield control** to the event loop.
* Suitable for **I/O-bound tasks** like DB calls, API calls, file access.
* More efficient for **high-concurrency applications**.
* FastAPI is built to **fully support async I/O** out of the box.

### ⏱️ Non-blocking Example:

```python
from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/async-task")
async def async_task():
    await asyncio.sleep(5)  # Non-blocking sleep
    return {"message": "Finished async task"}
```

* `await asyncio.sleep(5)` tells the event loop to pause and resume later.
* **Other tasks can run in the meantime.**

---

## 🔍 3. **FastAPI’s Concurrency Model**

FastAPI uses **ASGI (Asynchronous Server Gateway Interface)** via **Uvicorn** (or Hypercorn), which allows handling **many requests concurrently** using `async` functions.

FastAPI doesn’t force you to use `async`, but **using it properly makes your app scalable**.

| Feature             | Sync (`def`)     | Async (`async def`)               |
| ------------------- | ---------------- | --------------------------------- |
| Blocking            | Yes              | No (with `await`)                 |
| I/O operations      | Slows the thread | Other tasks continue              |
| Concurrency         | Poor             | Excellent                         |
| CPU-intensive tasks | Good             | Bad (should not block event loop) |
| Syntax              | `def`            | `async def` and `await`           |

---

## 🧠 4. **When to Use Sync vs Async in FastAPI**

### ✅ Use `async def` when:

* You’re making **HTTP requests to external APIs**
* Accessing **databases** with async libraries (e.g., `databases`, `asyncpg`)
* Using `asyncio.sleep`, file I/O, or socket I/O

### ❌ Do **NOT** use `async def` when:

* Your function is **CPU-bound** (e.g., large calculations, image processing)
* You're using **sync-only libraries** (e.g., standard `sqlite3`, `psycopg2`, `requests`)

Because `async` functions shouldn't block — blocking inside `async def` defeats the purpose and **will freeze the event loop**.

---

## 🔧 5. **Mixing Sync and Async Code**

FastAPI allows both, but there are important things to remember:

```python
@app.get("/mix-sync")
def sync_handler():
    # Can call only other sync code
    ...

@app.get("/mix-async")
async def async_handler():
    # Can call async code using await
    ...
```

You **can call sync code from async**, but doing blocking I/O inside `async def` is a **bad practice**.

### ❌ Bad:

```python
import time

@app.get("/bad")
async def bad_handler():
    time.sleep(5)  # BAD: this blocks event loop
    return {"msg": "Blocked!"}
```

### ✅ Good:

```python
import asyncio

@app.get("/good")
async def good_handler():
    await asyncio.sleep(5)  # OK: event loop keeps running
    return {"msg": "Non-blocking"}
```

---

## 🧵 6. **How FastAPI Handles Concurrency**

FastAPI under the hood uses **Starlette**, which uses an **event loop (from asyncio)** and **a pool of worker threads** (like in `ThreadPoolExecutor`) for sync functions.

* If your endpoint is sync (`def`), FastAPI runs it in a **threadpool** so that it doesn’t block the event loop.
* If it’s `async def`, it runs **directly on the event loop**.

This flexibility allows you to migrate **slowly** from sync to async.

---

## 💡 Real-world Analogy

Think of a restaurant:

* **Sync** = The chef waits for the rice to boil for 15 mins before starting anything else.
* **Async** = The chef puts the rice on the stove, sets a timer, and **cooks something else in parallel**.

---

## 🧪 Summary

| Aspect            | `def` Sync              | `async def` Async             |
| ----------------- | ----------------------- | ----------------------------- |
| Definition        | `def func():`           | `async def func():`           |
| Blocking          | Yes                     | No (if used with `await`)     |
| Concurrency       | Low                     | High                          |
| Used for          | CPU-bound, simple APIs  | I/O-bound, high concurrency   |
| Libraries support | Most libraries are sync | Limited async library support |
| Performance       | Poor under load         | Excellent under load          |

---

If you want, I can also give you:

* Benchmarks showing sync vs async performance
* Real FastAPI project with both sync and async APIs
* How to use async DBs like `Tortoise ORM`, `SQLModel`, `Databases`

Let me know.

"""

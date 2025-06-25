"""
API routing in python


* What routes are
* How routing works in FastAPI
* How to use `APIRouter` for modular code
* Path vs query params
* Route dependencies
* Advanced techniques (prefixes, tags, versioning)

---

## 🔷 1. What is a Route in FastAPI?

A **route** in FastAPI connects a **URL path** and **HTTP method** (GET/POST/etc.) to a **Python function (view handler)**.

Example:

```python
@app.get("/hello")
def say_hello():
    return {"msg": "Hello!"}
```

* When someone visits `/hello`, FastAPI calls `say_hello()`
* The result is returned as a JSON response

---

## 🔷 2. Basic Routes with HTTP Methods

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # GET request to "/"
def read_root():
    return {"message": "Welcome"}

@app.post("/create")  # POST request to "/create"
def create_item(data: dict):
    return {"status": "Created", "data": data}

@app.put("/update/{item_id}")
def update(item_id: int, data: dict):
    return {"id": item_id, "updated": data}

@app.delete("/delete/{item_id}")
def delete(item_id: int):
    return {"deleted_id": item_id}
```

* `@app.get` → Read
* `@app.post` → Create
* `@app.put` / `@app.patch` → Update
* `@app.delete` → Delete

---

## 🔷 3. Path Parameters (Dynamic URLs)

Used to capture variables in the URL:

```python
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
```

FastAPI automatically:

* Parses `item_id` as `int`
* Validates the type
* Shows in the docs

---

## 🔷 4. Query Parameters

```python
@app.get("/search")
def search(q: str, limit: int = 10):
    return {"query": q, "limit": limit}
```

* Accessed as: `GET /search?q=books&limit=5`
* `q` is **required**
* `limit` has default of 10 → optional

---

## 🔷 5. Request Body + Path Params + Query Params

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/{item_id}")
def update_item(item_id: int, item: Item, notify: bool = False):
    return {"item_id": item_id, "item": item.dict(), "notify": notify}
```

Example:

```http
POST /items/42?notify=true
Body:
{
  "name": "Phone",
  "price": 999.99
}
```

---

## 🔷 6. Organizing Routes with `APIRouter`

Split big apps into multiple route files.

### 📁 Structure:

```
project/
├── main.py
├── routers/
│   ├── users.py
│   └── items.py
```

### `routers/users.py`

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users():
    return ["User1", "User2"]
```

### `main.py`

```python
from fastapi import FastAPI
from routers import users

app = FastAPI()

app.include_router(users.router)
```

---

## 🔷 7. Router Prefixes and Tags

### Prefix

```python
router = APIRouter(prefix="/users")
```

Then `/users` is prepended to all endpoints.

### Tags

```python
router = APIRouter(
    prefix="/users",
    tags=["Users"]
)
```

Adds a **section in Swagger UI** for users.

---

## 🔷 8. Route Versioning (Optional but Powerful)

```python
app.include_router(users.router, prefix="/api/v1")
```

✅ Allows backward compatibility:

* `/api/v1/users`
* `/api/v2/users`

---

## 🔷 9. Dependencies with Routes

You can add dependencies for:

* Auth checks
* DB connections
* Shared logic

```python
from fastapi import Depends

def verify_token(token: str):
    if token != "secure123":
        raise HTTPException(status_code=401, detail="Unauthorized")

@app.get("/secure", dependencies=[Depends(verify_token)])
def secure_data():
    return {"secret": "data"}
```

---

## 🔷 10. Summary: Golden Routing Rules

| Feature               | When to Use                                           |
| --------------------- | ----------------------------------------------------- |
| Basic `@app.get/post` | Small apps                                            |
| `APIRouter`           | Modular, maintainable apps                            |
| `prefix`, `tags`      | Group endpoints by feature (like `users`, `products`) |
| `response_model`      | Ensure correct and safe output format                 |
| Dependencies          | Auth, DB sessions, validation                         |
| Path + Query + Body   | Combine all types of inputs                           |
| Versioning            | When your API might change in the future              |

---

## ✅ Example Project Routing

```python
# main.py
from fastapi import FastAPI
from routers import users, items

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(items.router, prefix="/items", tags=["Items"])
```

```python
# routers/users.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_users():
    return ["user1", "user2"]

@router.get("/{user_id}")
def get_user(user_id: int):
    return {"id": user_id}
```

---

Do you want me to help you **convert your current project to use `APIRouter`** structure or add things like **authentication** or **middleware** in routing?

"""
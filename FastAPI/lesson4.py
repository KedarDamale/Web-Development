"""
Debugging not just in fastapi but in all programming

when you hover over the number on the left side of code a red dot becomes visible if you click on the dot it will stay permanent untill you click that off again
meaning of that dot is that dot is now the end line of the program means the program execution will stop at that dot and will not contunue further 
which helps in debugging

fastapi also provides default debugging at terminal , on docs and rdocs
"""













"""
FastAPI comes with **built-in, auto-generated interactive API documentation** that makes it extremely easy to:

* Understand available endpoints
* Test API routes directly from the browser
* View request/response formats and schemas
* See HTTP methods, query/path parameters, request bodies, etc.

---

## 🔥 FastAPI Docs Overview

### ✅ FastAPI generates **2 documentation UIs** out-of-the-box:

| Docs Type      | URL                           | Description                                |
| -------------- | ----------------------------- | ------------------------------------------ |
| **Swagger UI** | `http://127.0.0.1:8000/docs`  | Interactive API testing tool (default UI)  |
| **ReDoc**      | `http://127.0.0.1:8000/redoc` | Clean, structured documentation-style view |

---

## 🧪 Example FastAPI App

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def greet(name: str = "Guest"):
    return {"message": f"Hello, {name}!"}
```

### 🔗 Go to: `http://127.0.0.1:8000/docs`

You'll see:

* A GET endpoint `/hello`
* A query parameter `name`
* A textbox to enter a value and test the endpoint live
* A "Try it out" button, and a response section

---

## 🛠️ Swagger UI Features (`/docs`)

### 📌 What You Can Do:

* Test endpoints with different parameters
* See generated request and response schemas
* View example curl commands
* Get instant feedback from API calls
* View required and optional fields
* See HTTP status codes returned
* See all routes grouped by tags (if used)

---

## 📘 ReDoc Features (`/redoc`)

* Cleaner UI for documentation
* Focused on readability, great for publishing docs
* Less interactive (can’t test API calls directly)
* Sections are expandable and nicely structured

---

## 💡 How Are These Docs Generated?

FastAPI uses:

* The **OpenAPI (Swagger) specification** under the hood
* **Pydantic models** and **Python type hints** to automatically build:

  * Schema definitions
  * Example inputs/outputs
  * Parameter types, constraints, and requirements

---

## 📂 Example with More Details

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("/create-user")
def create_user(user: User):
    return {"message": f"User {user.name} created!"}
```

### 🔗 Now check `/docs`:

* Method: POST `/create-user`

* Body schema auto-detected as:

  ```json
  {
    "name": "string",
    "age": 0,
    "email": "string"
  }
  ```

* You can **"Try it out"**, fill in JSON, and hit "Execute"

* FastAPI will:

  * Validate types using `Pydantic`
  * Return appropriate HTTP responses

---

## ⚙️ Customizing Docs

You can change title, description, version, etc. of the docs UI:

```python
app = FastAPI(
    title="My Awesome API",
    description="This API manages users and items",
    version="1.0.0"
)
```

You can also **disable docs or change the URLs**:

```python
app = FastAPI(
    docs_url="/documentation",   # Swagger UI moved here
    redoc_url=None               # Disable ReDoc
)
```

---

## ✅ Summary

| Feature                 | Swagger UI (`/docs`) | ReDoc (`/redoc`) |
| ----------------------- | -------------------- | ---------------- |
| Interactive testing     | ✅ Yes                | ❌ No             |
| Clean documentation     | ✅ Decent             | ✅ Very clean     |
| Generated automatically | ✅ Yes                | ✅ Yes            |
| Powered by              | OpenAPI + Swagger UI | OpenAPI + ReDoc  |

---

## 🧠 When to Use What

| Use Case                                          | Recommendation                   |
| ------------------------------------------------- | -------------------------------- |
| Debugging and testing during development          | Use `/docs`                      |
| Publishing clean, readable API reference          | Use `/redoc`                     |
| Need to customize or hide docs (e.g., production) | Use `docs_url=None`, or add auth |

---

Let me know if you want:

* A custom OpenAPI schema override
* To include example responses and metadata in docs
* To protect the docs behind a login or API key

"""
"""
Query Parameters in FastAPI

🔹 Path Parameters (Required):
- Are part of the URL path and are mandatory.
- Example: /blog/{id} → /blog/13

🔹 Query Parameters (Optional):
- Appear after a '?' in the URL.
- Example: /blog?id=13
- You can skip them or provide defaults in the function signature.
- They are commonly used for filters, pagination, searching, etc.

Syntax in URL:
    /endpoint?key=value&key2=value2

FastAPI automatically detects query parameters based on whether
they're used in the function signature but not in the path.
"""

from fastapi import FastAPI

app = FastAPI()

# --------------------------
# Example 1: Basic Query Parameter with Default
# --------------------------
@app.get('/')
def get_blogs(id: str = "Guest"):
    return {"message": f"Hello {id}!"}

"""
Try:
- http://127.0.0.1:8000/                   → Hello Guest!
- http://127.0.0.1:8000/?id=Kedar          → Hello Kedar!
"""

# --------------------------
# Example 2: Multiple Query Parameters with Type Hints
# --------------------------
@app.get("/sum")
def add(a: int = 0, b: int = 0):
    return {"result": a + b}

"""
Try:
- http://127.0.0.1:8000/sum?a=45&b=45      → {"result": 90}
- http://127.0.0.1:8000/sum?a=100          → {"result": 100} (b uses default 0)
- http://127.0.0.1:8000/sum                → {"result": 0}
Note:
- Default values make the parameters optional.
- If no default is given, they behave like required params.
"""

# --------------------------
# Example 3: Optional Search Query
# --------------------------
@app.get("/search")
def search(q: str = None):
    if q:
        return {"results": [f"Result for '{q}'"]}
    return {"results": ["Default search results"]}

"""
Try:
- http://127.0.0.1:8000/search?q=python     → Result for 'python'
- http://127.0.0.1:8000/search              → Default search results
"""


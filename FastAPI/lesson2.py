# Creating different routes using FastAPI

from fastapi import FastAPI

# Creating the FastAPI application instance
app = FastAPI()

# Root route - GET method at '/'
@app.get('/')
def hello():
    return {'msg': 'Hello Kedar'}  # This will be returned when we hit http://127.0.0.1:8000/

"""
Output:

{
  "msg": "Hello Kedar"
}
"""

# About route - GET method at '/about'
@app.get('/about')  # This will be returned when we hit http://127.0.0.1:8000/about
def about():
    return {'msg': 'This is the About page'}

"""
Output:

{
  "msg": "This is the About page"
}

If the user hits an endpoint that doesn't exist, FastAPI will automatically return:

{
  "detail": "Not Found"
}
"""

# -----------------------------------------------
# 📘 How FastAPI Works Under the Hood (Internals)
# -----------------------------------------------

"""
🧠 Under-the-Hood Mechanics of FastAPI:

1. 📥 HTTP Request Handling:
   - FastAPI is built on top of **Starlette**, an ASGI (Asynchronous Server Gateway Interface) framework.
   - It listens for incoming HTTP requests like GET, POST, PUT, DELETE etc.

2. 🧭 Routing:
   - Each decorator like @app.get('/about') registers a route and binds it to a Python function.
   - When the server receives a request (e.g., to "/about"):
     a. It matches the route and HTTP method (GET here).
     b. It calls the associated function (`about()`).
     c. It converts the returned dictionary into JSON using the built-in `json` encoder.

3. 🧾 Response Format:
   - You should always return **JSON-serializable data** (typically dictionaries in Python).
   - FastAPI automatically sets the proper content type: `application/json`.

4. 🚫 Automatic 404:
   - If the path or method doesn’t match any defined route, FastAPI returns:
     {
       "detail": "Not Found"
     }

5. 🧪 Auto-Generated Docs:
   - FastAPI provides 2 built-in interactive API UIs:
     - Swagger UI:   http://127.0.0.1:8000/docs
     - ReDoc:        http://127.0.0.1:8000/redoc
   - These are powered by the OpenAPI schema it generates from your routes and type hints.

6. ⚡ Performance:
   - FastAPI uses async I/O under the hood via ASGI + Starlette + Uvicorn.
   - This allows it to handle thousands of concurrent requests efficiently.

"""

# --------------------------
# ✅ How to Run This App:
# --------------------------
"""
1. Save this file as main.py or lesson1.py

2. Open terminal and navigate to its directory:
   cd path/to/your/folder

3. Run with Uvicorn:
   uvicorn main:app --reload

   - `main` is the filename (without .py)
   - `app` is the FastAPI object
   - `--reload` auto-reloads the server when code changes

4. Open browser and test:
   - http://127.0.0.1:8000/         → Hello route
   - http://127.0.0.1:8000/about    → About route
   - http://127.0.0.1:8000/xyz      → Will return 404
   - http://127.0.0.1:8000/docs     → Swagger UI
   - http://127.0.0.1:8000/redoc    → ReDoc UI
"""

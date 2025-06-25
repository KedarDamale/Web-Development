"""
FastAPI is a modern, fast (high-performance)  
web framework for building APIs with Python 3.7+,
based on standard Python type hints.

It is designed for building RESTful APIs 
and is known for being extremely fast, 
efficient, and easy to use.

It is built on Starlette (for web handling) 
and Pydantic (for data validation).

It provides full support for async/await, 
making it excellent for high-concurrency applications.

It uses Python type hints for automatic validation 
and editor support.

It automatically generates interactive API docs 
using Swagger UI and ReDoc.
(These work similarly to Postman, allowing you to test endpoints directly in the browser.)

# Installation

pip install fastapi
pip install uvicorn[standard]
"""

from fastapi import FastAPI

# Creating the FastAPI app object
app = FastAPI()

# This works but is not recommended:
# @app.get('/')
# def hello():
#     return 'Kedar Damale'  # ❌ Not JSON — FastAPI expects dict or JSON-serializable objects

@app.get('/')  # app is our FastAPI object, get() is the HTTP method (called as operation in fastapi), and '/' is 
               #the path in some other tech this same is called as route or endpoint that the frontend or client hits to access this resource
               #decorator is called as path operator decorator
def hello(): #path operation function
    return {"data": "Kedar Damale"}  # ✅ Recommended: returns a dictionary (which FastAPI converts to JSON)

"""
This is the minimum code required for a FastAPI app:

1. Import the FastAPI class.
2. Create an instance of FastAPI.
3. Use decorators like @app.get(path) to define routes (endpoints).
4. Define a function below the decorator that handles that route.

# To start the FastAPI app:
# uvicorn filename:fastapi_instance_name --reload
# --reload enables auto-restart on code changes (useful during development).
"""

"""
In this case:

Assume the file is named lesson1.py

> cd FastAPI         # ✅ Change directory to where lesson1.py is located

> uvicorn lesson1:app --reload

# 'lesson1' = filename (without the .py extension)
# 'app'     = FastAPI instance name (the object created from FastAPI())
"""

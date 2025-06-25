# Request body is the JSOM message that we recieve from user and response body is the ine give nby server
# 
# 
# Importing FastAPI class from the fastapi module to create the API app instance
from fastapi import FastAPI
from typing import Optional

# Creating an instance of the FastAPI class
app = FastAPI()

# Importing BaseModel from pydantic for creating data models (schemas)
from pydantic import BaseModel

# Defining a Pydantic model 'User' to validate the request body structure
class User(BaseModel):#taking inheritance of pydantic basemodel
    login: str      # login must be a string
    password: str   # password must also be a string
    #if you want something optional withing basemodel then you have to imnport optionsl from typing
    xyz:Optional[bool] #or we can just set it to None
    
    #pydantic supportd int float str bool None (Optional[...]) list[x] (list of x type elements) tuple[x,y] (tuple of x and y datatypes) set[x] dict[str, int] str is key and int is value
    #there are many more librarries like typing but these are the basic ones

# Simulating a simple in-memory user database using a dictionary
users_db = {
    "kedard": {"password": "1234"},
    "johnd": {"password": "abcd"},
    "1": {"password": "abcd"},
    "2": {"password": "abcd"},
    "3": {"password": "abcd"}
}

# -------------------------------
# READ OPERATION: User validation
# -------------------------------
# Defining a GET route that validates a user's login using path parameters
@app.get('/validate_user/{login}/{password}')
def validate_user(login: str, password: str):  # Path parameters captured from URL
    if login in users_db:  # Check if login exists in the users_db dictionary
        # If user exists, check if password matches the stored password
        if users_db.get(login).get('password') == password:
            print(f'{login} logged in')  # Print to server logs for confirmation
            return {"User logged in"}   # Respond with success message
        else:
            return {'password doesnt match!'}  # Incorrect password case
    else:
        return {'User is not in db'}  # Username not found case

# -------------------------------
# CREATE OPERATION: Add new user
# -------------------------------
# POST method used to create new resources (users) on the server
@app.post('/create_user')
def create_user(u: User):  # `u` is automatically parsed from request body using the User Pydantic model
    if u.login in users_db:
        return {'User already exists'}  # Check for uniqueness of login
    else:
        users_db[u.login] = {"password": u.password}  # Add new user to the dictionary
        print(users_db)  # Log the updated users_db
        return {
            "msg": "User created successfully",
            "user": u  # Return the user object as confirmation
        }

# -------------------------------
# UPDATE OPERATION: Modify user
# -------------------------------
# PUT method is used for full update of a resource
@app.put('/update_user')
def update_user(u: User):  # Accepts request body in form of User model
    if u.login in users_db:
        users_db[u.login] = {"password": u.password}  # Overwrite the existing user password
        print(users_db)  # Log updated state
        return {"msg": "User updated successfully", "user": u}
    else:
        return {'This user doesnt exists'}  # Can't update a user that doesn't exist

# -------------------------------
# DELETE OPERATION: Remove user
# -------------------------------
# DELETE method is used to delete a resource
@app.delete('/delete_user')
def delete_user(login: str):  # Takes login as a query parameter (?login=username)
    if login not in users_db:
        return {'The user doesnt exist to delete'}  # Cannot delete what doesn't exist
    else:
        del users_db[login]  # Remove user from dictionary
        print(users_db)  # Log current state of users_db
        return {'The user deleted successfully'}


"""
Creating a user from react will look something like this

import React, { useState } from 'react';
import axios from 'axios';

function CreateUser() {
  const [login, setLogin] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleCreateUser = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/create_user', {
        login: login,
        password: password
      });

      setMessage(response.data.msg || JSON.stringify(response.data));
    } catch (error) {
      if (error.response) {
        setMessage(JSON.stringify(error.response.data));  // API error
      } else {
        setMessage('Error connecting to server');
      }
    }
  };

  return (
    <div>
      <h2>Create User</h2>
      <input
        type="text"
        placeholder="Login"
        value={login}
        onChange={e => setLogin(e.target.value)}
      />
      <br />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={e => setPassword(e.target.value)}
      />
      <br />
      <button onClick={handleCreateUser}>Create</button>
      <p>{message}</p>
    </div>
  );
}

export default CreateUser;


"""


"""



## 🔍 **Why Use Request Body Instead of Path Params?**

Path parameters (e.g., `/user/kedar/1234`) and request bodies (e.g., POSTing JSON like `{ "login": "kedar", "password": "1234" }`) **serve different purposes**. You don’t choose randomly. It depends on:

* **Type of HTTP Method**
* **Amount and sensitivity of data**
* **REST API design standards**

---

## ✅ 1. **HTTP Method Semantics**

| Method | Should Have Path Params?    | Should Have Body? | Typical Use   |
| ------ | --------------------------- | ----------------- | ------------- |
| GET    | ✅ Yes (to specify resource) | ❌ No              | Fetching data |
| POST   | ❌ Not typically             | ✅ Yes             | Creating data |
| PUT    | ✅ Yes (resource ID)         | ✅ Yes             | Updating data |
| DELETE | ✅ Yes (resource ID)         | ❌ Sometimes       | Deleting data |

### 📌 FastAPI automatically rejects a body in GET requests (as per HTTP spec).

---

## ✅ 2. **Data Sensitivity and Security**

Sending sensitive data like **passwords** in:

* `❌ Path Parameters`: `/validate_user/kedar/1234` → visible in browser history, logs, proxies, etc.
* `✅ Request Body`: `{ "login": "kedar", "password": "1234" }` → sent in encrypted HTTP body (via HTTPS), not visible in URL

🔐 **Never send passwords or sensitive data in URL path or query params.**

---

## ✅ 3. **RESTful Design Convention**

**REST API design** follows clear structure:

| Resource Type   | URL Path Example   | Method | Request Body? |
| --------------- | ------------------ | ------ | ------------- |
| Create new user | `/users`           | POST   | ✅ Yes         |
| Get a user      | `/users/{user_id}` | GET    | ❌ No          |
| Update user     | `/users/{user_id}` | PUT    | ✅ Yes         |
| Delete user     | `/users/{user_id}` | DELETE | ❌ No          |

So for creating a user:

```http
POST /users
Content-Type: application/json
{
  "login": "kedar",
  "password": "1234"
}
```

---

## ✅ 4. **Data Size and Structure**

Path params are meant for **short, simple identifiers** like:

```http
/users/123
/products/sku-4422
```

Whereas request bodies support:

* Complex JSON objects
* Nested structures
* Arbitrary fields

📦 You can’t send:

```json
{
  "user": {
    "name": "kedar",
    "password": "1234",
    "address": {
      "city": "Pune",
      "pincode": 411038
    }
  }
}
```

...in a URL path or query.

---

## ✅ 5. **Cleanliness and Maintainability**

Path parameter approach for creation:

```
POST /create_user/kedar/1234
```

Problems:

* Not RESTful
* Clumsy with optional params (what if more fields added later?)
* Breaks easily when field order changes
* Password is exposed in URL

---

## 🧠 Summary: When to Use What

| Use Case                    | Use Path Params?  | Use Request Body?   |
| --------------------------- | ----------------- | ------------------- |
| Fetch single resource       | ✅ Yes             | ❌ No                |
| Create resource             | ❌ No              | ✅ Yes               |
| Send sensitive/complex data | ❌ No              | ✅ Yes               |
| Send short identifiers      | ✅ Yes             | ❌ No                |
| Clean & RESTful design      | ✅ For resource ID | ✅ For data payloads |

---

## 🚫 Real-World Problem if You Use Path Instead of Body

Imagine:

```http
POST /create_user/kedar/1234
```

* Search engines may index it.
* Browser stores in history.
* Server logs show the password.
* Changing the payload structure means breaking the route.
* It violates HTTP method meaning — POST is meant to use body.

---

### ✅ Correct Approach (What You Did):

```http
POST /create_user
Body:
{
  "login": "kedar",
  "password": "1234"
}
```

This is secure, RESTful, scalable, and maintainable.

---

Let me know if you want me to show:

* How query parameters differ
* API testing with Postman or Swagger
* Or secure this endpoint with hashing/authentication
"""
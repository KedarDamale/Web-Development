"""

🔷 What is a Schema in FastAPI?
A Schema in FastAPI is a Pydantic model. It's used to define the shape and type of the data your API expects in requests or returns in responses.

Schemas serve three main purposes:

Validation: Ensures the incoming data is of correct types/constraints.

Serialization/Deserialization: Converts JSON to Python and back.

Documentation: Auto-generates OpenAPI docs in /docs.


basic schema for request body

from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int


optional fields and default values

from typing import Optional

class User(BaseModel):
    name: str
    email: str
    age: Optional[int] = None
    is_active: bool = True  # default value
    
nested schemas act as a nested dict in json
    
class Address(BaseModel):
    city: str
    pincode: int

class User(BaseModel):
    name: str
    email: str
    address: Address
    

"""
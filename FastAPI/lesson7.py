from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Internal data model
class InternalUser(BaseModel):
    id: int
    name: str
    email: str
    password: str

# Safe response schema
class PublicUser(BaseModel):
    id: int
    name: str
    email: str

@app.get("/user", response_model=PublicUser)#response_model is a keyword
def get_user():
    user = InternalUser(id=1, name="Kedar", email="kedar@example.com", password="secret")
    return user #this will return user but it will remove passwrod as reponse model= public user doesnt contain passwrod

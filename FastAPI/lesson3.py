#path parameters in fastapi


from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def hello():
    return {'data':'Hi kedar'}

@app.get('/{name}')
def hello(name):
    return {'data':f"Hi {name}"}

data={
    '1':{'data':'Hello from id1','comments':'This is id1 comment'},
    '2':{'data':'Hello from id2','comments':'This is id2 comment'},
    '3':{'data':'Hello from id3','comments':'This is id3 comment'}
}

@app.get('/{id}/data')
def fetch_data_from_id(id):
    return data.get(id).get('data')


@app.get('/{id}/comments')
def fetch_comments_from_id(id):
    return data.get(id).get('comments')


#the probelm is we cant control the datatype
#for eg.

@app.get('/add/{num1}/{num2}')
def add(num1,num2):
    return num1+num2 #this wil return "3445" whic hmeans its processing parameters in default id which is string

# to solve this we will use type hints which dont enforce types in vanilla python but they do in fastapi

@app.get('/addint/{num1}/{num2}')
def add(num1:int,num2:int):# FastAPI converts path parameters to int if specified, this parameter casting works exactly like int() and all so i
                            #something that cant be converted to something it will trow erre e.g int('5') will be 5 but int('abc') will throw error 
                            #just like that 
    return num1+num2 #now this will return 79


"""
- Static routes: Do not rely on parameters.
  Example: GET '/' or '/about'

- Dynamic routes: Include parameters that change the output.
  Example: GET '/{name}' or '/{id}/data'

FastAPI matches routes **top to bottom**, so order matters.

❗ Route Matching Rule:
If both these routes exist:
    @app.get("/blog/undefined")
    @app.get("/blog/{id}")

And you visit: /blog/undefined
→ FastAPI will match "/blog/{id}" first (because it appears earlier),
  treating 'undefined' as a path parameter — even if 'undefined' is not valid.
→ This causes bugs and unexpected behavior.

✅ Solution:
- Always put more specific/static routes above dynamic ones.
- Order matters in FastAPI.

"""
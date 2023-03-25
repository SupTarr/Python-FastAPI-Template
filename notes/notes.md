# Python API Development - Comprehensive Course for Beginners

---

## Section 2: Setup & installation

### 2.1: Virtual environment on windows

**venv** is a Python module that creates a unique environment for each task or project.

```cmd
py -3 -m venv venv
```

```cmd
venv\Scripts\activate.bat
```

(venv) C:\Users\tatas\Desktop\SupTarr\Workspace\Python-APIs-Template>

---

## Section 3: FastAPI

```cmd
uvicorn app.main:app --reload
```

This command makes **FastAPI** always watch some changing of codes.

```python
from fastapi import FastAPI

app = FastAPI()

# @ (Decorator): add path("/") with HTTP request methods(GET)
@app.get("/")
# Function definition (name it as you want)
async def root():
    return {"message": "Hello World"}
```

```python
from fastapi import FastAPI

app = FastAPI()

## Path Operation Order
@app.get("/")
async def root():
    return {"This will appear as a result"}

@app.get("/")
def get_posts():
    return {"You have never get this"}
```

### HTTP Post Requests

```python
from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.post("/posts")
## Change JSON Body to dictionary
def create_post(post: dict = Body(...)):
    print(post)
    return {"new_post": {"title": post["title"], "content": post["content"]}}
```

### Schema Validation with Pydantic

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

## Schema to fix keys and types
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.post("/posts")
def create_post(post: Post):
    print(post)
    return {"new_post": {"title": post.title, "content": post.content}}
```

### CRUD Operations

- **Create** (POST): `@app.post("/posts")`
- **Read** (GET):
  - `@app.get("/posts/{id}")`
  - `@app.get("/posts")`
- **Update** (PUT/PATCH): `@app.put("/posts/{id}")`
- **Delete** (DELETE): `@app.delete("/posts/{id}")`

### HTTP Status

```python
from fastapi import FastAPI, status, HTTPException
from random import randrange

app = FastAPI()

# 201 Created: The request succeeded, and a new resource was created as a result.
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 100000)
    my_posts.append(post_dict)
    print(my_posts)
    return {"data": post_dict}

# 404 Not Found: The server cannot find the requested resource.
@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} was not found",
        )
    return {"data": post}
```

---

## Section 4: SQL

[Link to section 4](4_SQL.md)

---

## Section 6: ORMs

### ORMs VS Schema models (Pydantic models)

**ORMs** (Object-Relational Mappers) are software tools or frameworks that facilitate the communication between *object-oriented programming languages* and *relational databases*.

**Pydantic models** can be used to define the *shape of data* that should be stored in a database or used in any other part of an application.

**SQLAlchemy models** are used to define the *structure* (column) of a database table and its *relationships* to other tables.

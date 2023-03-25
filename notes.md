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

### SQL commands

| id: Serial + Primary Key | name: Character varying(50) | price: Numeric(10, 2) | is_sale: Boolean | inventory: Integer | created_at: Timestamp |
| :----------------------: | :-------------------------: | :-------------------: | :--------------: | :----------------: | :-------------------: |
|            1             |         "Product A"         |         49.99         |       true       |        100         | "2022-03-23 12:00:00" |
|            2             |         "Product B"         |         19.99         |      false       |         50         | "2022-03-22 10:30:00" |
|            3             |         "Product C"         |         89.99         |       true       |         25         | "2022-03-20 14:15:00" |
|            4             |         "Product D"         |         59.99         |      false       |         75         | "2022-03-18 16:45:00" |

#### SELECT ... FROM

```SQL
SELECT * FROM products;
-- SELECT all-columns FROM table-name
```

```SQL
SELECT id, name, is_sale FROM products;
-- SELECT some-columns FROM table-name
```

#### SELECT ... AS FROM

```SQL
SELECT id AS product_id FROM products;
-- SELECT column AS new-column-name FROM table-name
```

#### WHERE

```SQL
SELECT * FROM products WHERE id = 10;
SELECT * FROM products WHERE inventory = 0;
SELECT * FROM products WHERE price > 50;
-- SELECT * FROM table-name WHERE condition
```

```SQL
SELECT * FROM products WHERE inventory != 0;
SELECT * FROM products WHERE inventory <> 0;
-- SELECT * FROM table-name WHERE not-equal

SELECT * FROM products WHERE inventory <> 0 AND price > 20;
SELECT * FROM products WHERE inventory <> 0 OR price < 20;
```

#### WHERE + IN

```SQL
SELECT * FROM products WHERE id IN (1, 2, 3);
```

#### WHERE + LIKE

```SQL
SELECT * FROM products WHERE name LIKE 'TV%';
-- SELECT * FROM table-name WHERE {condition of name that start with TV}

SELECT * FROM products WHERE name LIKE '%e';
-- SELECT * FROM table-name WHERE {condition of name that end with TV}

SELECT * FROM products WHERE name LIKE '%en%';
-- SELECT * FROM table-name WHERE {condition of name that contain TV}
```

#### ORDER BY

```SQL
SELECT * FROM products ORDER BY price ASC;
SELECT * FROM products ORDER BY price DESC;

SELECT * FROM products ORDER BY inventory DESC, price;

SELECT * FROM products WHERE price > 20 ORDER BY created_at DESC;
```

#### LIMIT + OFFSET

```SQL
SELECT * FROM products LIMIT 10;
SELECT * FROM products WHERE price > 10 LIMIT 3;
SELECT * FROM products ORDER BY id LIMIT 5 OFFSET 2;
-- OFFSET is useful for pagination.
```

#### INSERT

```SQL
INSERT INTO products (name, price, is_sale, inventory, created_at)
VALUES
  ('Product A', 49.99, true, 100, '2022-03-23 12:00:00'),
  ('Product B', 19.99, false, 50, '2022-03-22 10:30:00'),
  ('Product C', 89.99, true, 25, '2022-03-20 14:15:00'),
  ('Product D', 59.99, false, 75, '2022-03-18 16:45:00')
RETURNING *;
```

#### UPDATE

```SQL
UPDATE products SET name = 'Product E', price = 50.99 WHERE id = 10 RETURNING *;
```

#### DELETE

```SQL
DELETE FROM products WHERE id = 10 RETURNING *;
```

---

## Section 6: ORMs

### ORMs VS Schema models (Pydantic models)

**ORMs** (Object-Relational Mappers) are software tools or frameworks that facilitate the communication between _object-oriented programming languages_ and _relational databases_.

**Pydantic models** can be used to define the _shape of data_ that should be stored in a database or used in any other part of an application.

**SQLAlchemy models** are used to define the _structure_ (column) of a database table and its _relationships_ to other tables.

---

## Section 8: Authentication and Users

### JWT Token

**JWT** (JSON Web Token) is a standardized format for _transmitting data_ between two parties in a secure and compact manner.

A JWT token consists of three parts: a header, a payload, and a signature.

1. The **header** contains information about the _algorithm_ used to generate the signature.
2. The **payload** contains the _data_ (from Front-end) being transmitted.
3. The **signature** is created by combining the _header_ and _payload_, along with a _secret key_, and then applying a hashing algorithm to produce a unique string of characters.

# Learning Notes

This file is just to add notes and background about the technologies used in this repo

<!-- TOC -->

* [Learning Notes](#learning-notes)
    * [Project Roadmap](#project-roadmap)
    * [To learn](#to-learn)
    * [FastAPI](#fastapi)
    * [SQLAlchemy](#sqlalchemy)
    * [API/HTTP Request Methods](#apihttp-request-methods)
        * [HTTP POST request](#http-post-request)
        * [HTTP GET request](#http-get-request)
        * [HTTP PUT request](#http-put-request)
        * [HTTP HEAD request](#http-head-request)
        * [HTTP PATCH request](#http-patch-request)
        * [HTTP DELETE request](#http-delete-request)
    * [YAML](#yaml)
        * [What it tries to solve](#what-it-tries-to-solve)
        * [Rules](#rules)
    * [Docker](#docker)
        * [Concepts](#concepts)
        * [Dockerfile vs. docker-compose](#dockerfile-vs-docker-compose)
            * [Dockerfile](#dockerfile)
            * [docker-compose](#docker-compose)
        * [For my app](#for-my-app)
            * [1. Create a Dockerfile](#1-create-a-dockerfile)
            * [2. Create the docker-compose.yaml](#2-create-the-docker-composeyaml)
            * [3. Start up the container](#3-start-up-the-container)

<!-- TOC -->

## Project Roadmap

<details open>

- [x] Set up DB
- [x] First endpoint to add users
- [x] Dockerize my API
    - [x] Use `requirements.txt`
- [x] Connect to cloud SQL (Azure)
- [ ] Add automated testing
    - [ ] Unit tests
    - [ ] Feature tests (Cucumber / Gherkin)
- [ ] Enrich add users endpoint to
  optionally [include skills](https://fastapi.tiangolo.com/tutorial/sql-databases/#__tabbed_1_3)
- [ ] Feature: load data from:
    - [ ] A file
    - [ ] Others? (TBD)
- [ ] Feature: upload files (Cover letters/Resumes)
- [ ] Feature: Create stuff from templates (TBD, the Consumer might a better place for it)
- [ ] Add endpoint to PULL data from the DB
- [ ] Kubernetize my API
- [ ] Basic Kafka
    - [ ] Produce messages from the API
    - [ ] Consume messages
- [ ] Consumer
    - [ ] Validate incoming messages
    - [ ] Enrich data using the API (if applicable)
    - [ ] Create and store PDF's based on templates
- [ ] Break the API and the Kafka consumer into separate projects
- [ ] Implement secure Kafka
- [ ] Put this in the cloud
    - [ ] Is there a free version of Azure/GCP/etc ? (maybe RedHat?)
    - [ ] Put K8S modules in the cloud
    - [ ] Move the MySQL DB to the cloud
    - [ ] Store PDF documents in the cloud
    - [ ] Store templates (HTML?) in the cloud

</details>

## To learn

<details>

- [ ] Check exactly what FastAPI is
- [ ] How does FastAPI compares to other solutions
- [ ] What exactly is `uvicorn`? is it just for Dev? is it only for FastAPI?
- [ ] WSGI vs ASGI
- [ ] Learn about API keys
- [ ] Learn about pydantic and other alternatives
- [ ] Also learn about GraphQL
    - [ ] How does it compare to REST for ease of implementation?
    - [ ] How does it compare to REST in other areas (e.g. performance)
- [ ] Add/use `requirements.txt` in my application
- [ ] What is the `__init__.py` (in the Python package folder) used for?
- [ ] Flask vs Uvicorn
- [ ] Learn what each section of `docker-compose.yaml` does

</details>

## FastAPI

<details>

- it is a framework to build RESTful API's
- It uses Pydantic intrinsically to validate, serialize and deserialize data
    - Pydantic is a data validation library for Python.
    - Pydantic is among the fastest data validation libraries for Python.
    - Pydantic provides type hints for schema validation and serialization through type annotations.
- Starlette
    - is a lightweight ASGI framework/toolkit, to support async functionality in Python.
    - great performance by independent benchmarks, which is inherited by FastAPI.
- Uvicorn
    - Uvicorn is a minimal low-level server/application web server for async frameworks
    - following the ASGI specification
- Automatically generate OpenAPI documentation
- Can run on Gunicorn (WSGI) and ASGI servers such as Uvicorn and Hypercorn, making it a good choice for production
  environments

</details>

## SQLAlchemy

<details>

- `declarative_base()` is a factory function that constructs a base class for declarative class definitions (which is
  assigned to the Base variable)
- The Declarative system is the typically used system provided by the SQLAlchemy ORM in order to define classes mapped
  to relational database tables.
    - However, as noted in Classical Mappings, Declarative is in fact a series of extensions that ride on top of the
      SQLAlchemy mapper() construct.
- To link a pydantic model to a SQLAlchemy model (table) we declare an inner `Config` class inside the pydantic model
    - In the `Config` class We set the value `orm_mode = True` to let pydantic know this is an ORM (duh!)
    - Pydantic's `orm_mode` will tell the Pydantic model to read the data even if it is not a dict, but an ORM model
    - This way, instead of only trying to get the id value from a dict, as in `id = data["id"]` it will also
      try `id = data.id`
- SQLAlchemy and many others are by default "lazy loading".
    - That means, they don't fetch the data for relationships (e.g. `User`-->`Skill`) unless you try to access the
      attribute that would contain that data.
    -

</details>

## API/HTTP Request Methods

<details>

These are the basic ones, see below for further reference:

- [https://www.freecodecamp.org/news/http-request-methods-explained/]
- [https://www.w3schools.com/tags/ref_httpmethods.asp]

### HTTP POST request

- We use POST to create a new resource.
- A POST request requires a body in which you define the data of the entity to be created.
- A successful POST request would be a 200 response code.
- No restrictions on data length

### HTTP GET request

- We use GET to read or retrieve a resource.
- A successful GET returns a response containing the information you requested.
- **Data sent is visible as part of the URL**
- should never be used when dealing with sensitive data

### HTTP PUT request

- We use PUT to modify (`insert`/`update`) a resource.
- PUT updates the entire resource with data that is passed in the body payload.
- If there is no resource that matches the request, it will create a new resource.
- It is idempotent: calling the same PUT request multiple times will always produce the same result. In contrast,
  calling a POST request repeatedly have side effects of creating the same resource multiple times.

### HTTP HEAD request

- HEAD is almost identical to GET, but without the response body.
- In other words, if GET /users returns a list of users, then HEAD /users will make the same request but will not return
  the list of users.
- useful for checking what a GET request will return before actually making a GET request
    - a HEAD request can read the Content-Length header to check the size of the file, without actually downloading the
      file.

### HTTP PATCH request

- We use PATCH to modify a part of a resource.
- With PATCH, you only need to pass in the data that you want to update.

### HTTP DELETE request

- It is used to, well.... delete data

</details>

## YAML

<details>

### What it tries to solve

- Set of standards to transfer data regardless of language (Python, Java, etc)
- Competes with JSON and XML, but simpler (in theory)

### Rules

```yaml
# This is a comment
# In general, lowercase is encouraged
# YAML is simply a key:value pair
course:
  # Notice the indentation for sub-elements!
  course_name: "Python rules"
  course_name2: Python rules # No quotes is still acceptable
  version: 1.1
  year: 2023
  price: &price 1000  # Notice the ampersand!! this indicates a re-usable variable
  is_public: true
  release_date: 2023-12-15 14:09:00 # Notice ISO-ish
  pre-enroll: null # null isused for ... well, nulls
  tags: # This is one way to declare an array (notice indentation + dashes)
    - python
    - web development
    - mysql
  teachers: [ "hugo", "paco", "luis" ]  # Another way for an array
  # Notice the following syntax, it declares an array of objects (compare to JSON [{},{}] )
  teacher_details:
    - name: "hugo"
      email: "hugo@gmail.com"
      role: "admin"
    - name: "paco"
      email: "paco@gmail.com"
      role: "servant"
    # Yet another way to write objects / dicts
    - { name: "luis",email: "luis@gmail.com",role: "runner" }
  short_desc: > # This is a multi-line string, when read, tabs and line breaks are removed
    mi mama
    me mima mucho
  long_desc: | # Another multiline but all indentation and linebreaks are KEPT
    mi mama
      me mima mucho
  process_payment: *price  # Notice the reference to the variable we declared above ^^
  parent_var: &parent # Again, declaring a variable
    one: two
  child_var:
    three: four
    <<: *parent  # This includes all sub-elements in parent, in the child variable 

```

</details>

## Docker

<details>

### Concepts

- dockerfile
    - blueprint for building images
        - more like a set of instructions IMO
- image
    - template for running containers
- container
    - The actual running code

### Dockerfile vs. docker-compose

- A `Dockerfile` describes how to build a Docker **image**, while Docker Compose is a command for running a Docker
  **container**.
- `docker-compose` is a tool for defining and running multi-container applications
- Use a Dockerfile to **define** your app’s environment, so it can be reproduced anywhere.
- Define the services of your app in docker-compose.yml, so you can run them together in an isolated environment.
- Use `docker compose up` and `docker compose command` to start and run your entire app.

#### Dockerfile

- Uses docker build commands, which use a “context,”
- Context: the set of files located in the specified PATH or URL
- The build process can refer to any of the files in the context
- the URL parameter can refer to
    - Git repositories,
    - pre-packaged tarball contexts
    - or plain text files
- A Docker image consists of read-only layers, each of which represents a Dockerfile instruction.
- The layers are stacked and each one is a delta of the changes from the previous layer
- In the following Example
    - FROM creates a layer from the ubuntu:18.04 Docker image.
    - COPY adds files from your Docker client’s current directory.
    - RUN builds your application with make.
    - CMD specifies what command to run within the container.

```dockerfile
FROM ubuntu:18.04
COPY . /app
RUN make /app
CMD python /app/app.py
```

- Trivia: you can have multiple `FROM` sections to pull assorted functionality from different places:

```dockerfile
FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install -y odbcinst
RUN apt install -y unixodbc-dev
RUN apt-get install -y unixodbc

FROM Python:3.11
COPY . /app
RUN make /app
CMD python /app/app.py
```

- `requirements.txt`
    - You can make this one generic, i.e. don't specify a version, let `pip` decide

#### docker-compose

- "Adds" a new **writable** layer on top of the image
- All changes made to the running container, such as writing/modifying/deleting files, are done in this writable
  container layer

### For my app

#### 1. Create a Dockerfile

Remember: this is about creating the **image**

```dockerfile
# We copy the kernel functionality here. I'm using Python but it can be Devian, Ubuntu, ETC
FROM python:3.11

# Name the working dir
WORKDIR /app

# Copy "local" files to the container (in the `/app` folder)
# Sample:
COPY ./api/ ./api/
COPY ./requirements.txt .

# Install requirements in the container
RUN pip install --upgrade pip
# PRE-REQUISITE: Don't forget to refresh your requirements by doing : `pip freeze > requirements.txt`
RUN pip install -r ./requirements.txt
```

#### 2. Create the docker-compose.yaml

Note how you could spin up multiple container (in different ports) for escalabitily here

```yaml
version: "3"
services:
  # each service that could be executed from docker-compose goes here
  # note that the name can be anything (I just named it api)
  api:
    build: . # # config to build my image goes here... maybe? TODO: Investigate further
    expose:
      - 8000
    ports: # Port for my API
      - "8000:8000"
    restart: "always"
```

#### 3. Start up the container

```commandline
docker-compose up api
```

</details>

## General: What to set up for blank project

<details open>

### How to prepare ahead of the Intuit interview?

- [ ] Determine the minimum viable product "frame"
  - Database connection
  - API
  - Unit tests
  - Models / logic
  - Data load
- [ ] Implement the minimum viable frame into this project
- [ ] Practice creating at least 4 blank projects "by hand"
- [ ] Do at least 4 exercises from scratch
    - [ ] Ideally, ask community for peer review
- [ ] Create slides for personal presentation and portfolio

### Basic (blank) set up

<details> 

#### n. Make sure the DB is up and running

**IMPORTANT**: Consider creating a script for it

1. From Windows, open `Services`
2. Look for `MySQLServer`
3. Hit `Start`

#### n. Create basic folder structure

**NOTE**: _italics_ mean folder, `code` means file

- _api_
    - _database_
        - _daos_
        - _table_models_
        - `database.py`
    - _models_
    - `endpoints.py`
- _tests_
    - _unit_
    - _feature_
- _data_load_ (TBC)
    - **What here?**
- `Dockerfile`
- `docker-compose.yaml`
- `README.md`
- `requirements.txt`

#### n. Add requirements

```commandline
pip freeze > requirements.txt
```

#### n. Set up minimum Docker config

`Dockerfile`:

```dockerfile
# Specify the parent image (in this case Python)
FROM python:3.8

# Name the working dir (will be set by Docker if we don't do it)
WORKDIR /app

# Copy "local" files to the container (in the `/app` folder)
# Sample:
COPY ./api/ ./api/
COPY ./requirements.txt .

# Install requirements in the container
RUN pip install --upgrade pip
# PRE-REQUISITE: Don't forget to refresh your requirements by doing : `pip freeze > requirements.txt`
RUN pip install -r ./requirements.txt
```

`docker-compose.yaml` :
```yaml
version: "3"
services:
  # each service that could be executed from docker-compose goes here
  # note that the name can be anything (I just named it api)
  api:
    build: . # config to build my image goes here... maybe? TODO: Investigate further
    expose:
      - 8000
    ports: # Port for my API
      - "8000:8000"
    restart: "always"
    command: [ "uvicorn", "api.endpoints:app", "--host=0.0.0.0", "--reload" ]
    # watch allows the app to auto-reload on code changes, very practical
    develop:
      watch:
        - action: sync+restart
          # The path to watch changes for
          path: api/
          # the target (within the container) for the path
          target: /app/api
          ignore:
            - __pycache__/
            - .env
            - .venv
            - env/
            - venv/
            - .idea/
        - action: rebuild
          path: Dockerfile
        - action: rebuild
          path: docker-compose.yaml
        - action: rebuild
          path: requirements.txt
```

#### n. Create an endpoints file

```python
from fastapi import FastAPI, Depends

from api.database.database import SessionLocal
from sqlalchemy.orm import Session
from api.models.user_model import UserModel
from api.database.daos.user_dao import UserDao

app = FastAPI()


def get_session() -> SessionLocal:
    """
    We need to have an independent database session/connection (SessionLocal) per request, 
    use the same session through all the request and then close it after the request
    is finished.

    Returns:
        SessionLocal: A DB session to be used once
    """
    # fetch session
    session = SessionLocal()
    try:
        # `yield` returns a generator for the session, aka an iterable that can only iterate once
        # In this case it returns a new Session every time is called, but forgets the previous sessions immediately
        yield session
    finally:
        session.close()
```

#### n. Checkpoint: Make sure you are doing good

1. Start up the service
```commandline
docker-compose up api
```
2. See FastAPI:
```
http://localhost:8000/docs
```

</details> <!-- Basic (Blank) set up -->

### Now for the specific project

<details>

### 2. Create new project in PyCharm

### 3. Basic set up in PyCharm

#### 3.n. Create models

- For each model identified
    - Create a class, inheriting from `BaseModel` (`from pydantic import BaseModel`)
    - Add properties straight under the class, e.g.:

```python
class UserModel(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
```

- Don't forget to add a `Config` class inside the model and set `orm_mode = True`, this tells pydantic that is a an
  Object-Relational (DB) model

#### 3.n. Database
</details> <!-- Now for the specific project -->

</details>



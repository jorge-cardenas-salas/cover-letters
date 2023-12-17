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

<details open >

- [x] Set up DB
- [x] First endpoint to add users
- [ ] Dockerize my API
    - [ ] Use `requirements.txt`
- [ ] Kubernetize my API
- [ ] Add automated testing
    - [ ] Unit tests
    - [ ] Feature tests (Cucumber / Gherkin)
- [ ] Enrich add users endpoint to
  optionally [include skills](https://fastapi.tiangolo.com/tutorial/sql-databases/#__tabbed_1_3)
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

<details open>

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

#### docker-compose

- "Adds" a new **writable** layer on top of the image
- All changes made to the running container, such as writing/modifying/deleting files, are done in this writable
  container layer

### For my app

#### 1. Create a Dockerfile

Remember: this is about creating the **image**

```dockerfile
FROM python:3.8

# Copy "local" files to the container (in the `/app` folder)
COPY ./api /api
COPY ./requirements.txt .

# Set the working dir to the root folder
WORKDIR .

# Install requirements in the container
RUN pip install --upgrade pip
# PRE-REQUISITE: Don't forget to refresh your requirements by doing : `pip freeze > requirements.txt`
RUN pip install -r ./requirements.txt

# Start uvicorn itself
# It "might" be possible to run both my API (or multiple API's) and Consumer in the same image but not recommended
CMD ["uvicorn", "api.endpoints:app", "--host=0.0.0.0", "--reload"]
```

#### 2. Create the docker-compose.yaml

Note how you could spin up multiple container (in different ports) for scalabitily here

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



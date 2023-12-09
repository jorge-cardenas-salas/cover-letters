# Learning Notes

This file is just to add notes and background about the technologies used in this repo

## To learn

- [ ] Check exactly what FastAPI is
- [ ] How does FastAPI compares to other solutions
- [ ] What exactly is `uvicorn`? is it just for Dev? is it only for FastAPI?
- [ ] WSGI vs ASGI
- [ ] Learn about API keys
- [ ] Learn about pydantic and other alternatives
- [ ] Also learn about GraphQL
    - [ ] How does it compare to REST for ease of implementation?
    - [ ] How does it compare to REST in other areas (e.g. performance)

## FastAPI

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

## API/HTTP Request Methods
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

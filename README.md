# Cover Letters Project

## Background

<details>

### Motivation

Introductory Practice Project.

### Basic Description

Will allow a candidate to create cover letters (to be attached to applications) based on the candidate's profile and the
details on the position

### Target Functionality for v0.1.0

- API
    - Basic endpoint to add a user to the system
    - Set up system (making sure it runs in Docker)
- Consumer
    - N/A (no functionality just yet)

### Target Functionality for v0.2.0

- API
    - Endpoints to:
        - Add users basic data, including optionally
            - Skills
            - Experience / role
            - Achievements
            - Additional data
        - Submit a job match
            - User id
            - Job posting data: company, recruiter, job title, skills, role
            - Match skills to the ones from the user (top 4)
                - Use fuzzy logic if possible
            - Match role to the ones from the user (only 1)
                - Use fuzzy logic if possible
            - Produce matched data to a dummy kafka topic (fully working in v2)
- Consumer
    - N/A (no functionality just yet)

### Target Functionality for v1.0.0

- API
    - Endpoints:
        - Parse user data from a file and put it in the DB
        - Take an HTML template file as a parameter and assign it to an existing user
            - It has to be tied to an existing role for the user
            - Store it in a file system
        - Parse job match from a file
            - Do the same as the job match endpoint
- Consumer
    - For each message received:
        - Pull the corresponding HTML templates
        - Replace the values in the templates and generate individual files
            - For Cover Letter
            - For Resumme

### Target Functionality for vN.N.N

**IMPORTANT**: This is internationally vague, more a brainstorm of future functionality

- Implement a UI for the matches
- Create a `PositionMatch` scheduled job that will:
    - Pull open positions using the LinkedIn API
    - Discard:
        - Over 100 applicants
        - Certain job posters (e.g. Compunnel)
        - Over 4 weeks old
        - Jobs that are already in the document (see next bullet point)
    - Create a document (markdown? google docs?) with the remaining jobs
        - Pull keywords (skills / role) and put them in the document
        - Document should be able to mark jobs as:
          - pending
          - applied
          - discarded
    - Resources:
        - [Google Search](https://www.google.com/search?q=does+linkedin+have+a+public+ap)
        - [Tutorial(ish)](https://nubela.co/blog/ultimate-guide-to-linkedin-api_people-profile-api_with-python-examples/)
        - [LinkedIn: Accessing APIs](https://www.linkedin.com/help/linkedin/answer/a526048)
        - [Getting access (Microsoft)](https://learn.microsoft.com/en-us/linkedin/shared/authentication/getting-access)
        - [Apply with LinkedIn](https://learn.microsoft.com/en-us/linkedin/talent/apply-with-linkedin/apply-with-linkedin)
        - [Apply Connect](https://learn.microsoft.com/en-us/linkedin/talent/apply-connect)
- Create a `PositionApply` scheduled job that will:
    - Use the document from `PositionMatch` to pull jobs pending to apply
    - Extract keywords for the JD
    - Use the API to match jobs
      - The API will automatically generate CoverLetters and Resumes

### Practice points:

- Database:
    - Profile DB
        - People
        - skills
        - Experience
        - Achievements
        - Others
        - Templates <-- Likely not a DB BLOB but... something else
    - Applications
        - Jobs
- UI: TBD
- API / Microservices:
    - CRUD Profile
    - Create Cover Letters
    - Generate Docs
- Kafka:
- Docker:
- Kubernetes:
- Microservices:
- Cloud (?):

### Outputs

- Cover letter documents
    - One for each template and position selected

</details>

## Usage

<details>

### Necessary packages

- `pip install fastapi`
- `pip install uvicorn`
- `pip install sqlalchemy`
- `pip install pydantic`
- `pip install pytest`
- `pip install pytest-bdd`

### How to run

1. From the command line execute:
Docker-less execution:
```commandline
python -m uvicorn api.endpoints:app --reload
```
Docker execution (will auto-reload changes, so it might be a better choice):
```commandline
docker-compose watch api
```

2. To see the docs (inc all endpoints):

```
http://localhost:8000/docs
```

</details>

## Learning Points

<details>

### General notes

```commandline
python -m uvicorn cover-letters.api.endpoints:app --reload
```

In the previous line:

- `uvicorn` is the server on which the API runs
- `app` (the first one) is the name of the application file (which can have multiple endpoints of course)

#### Types of endpoint uses

- `get` post directly using the URL
- `put` uses models (see `pydantic` below) to hide the data being passed

#### pydantic

- Used to create models which can then be used in the endpoints

</details>


# Cover Letters Project

## Background
<details>

### Motivation
Introductory Practice Project.

### Basic Description
Will allow a candidate to create cover letters (to be attached to applications) based on the candidate's profile and the details on the position

### Target Functionality for v1.0.0
- The first time a user onboards to the app:
	- Cover letter template, with placeholders
		- Can be more than one (e.g. for a placement agency vs a company)
		- [Next step]: Plain text and formatted versions
	- List of skills
	- List of job experiences/responsibilities
	- List of job achievements
	- List of "others"
- To generate Cover Letters
	- Name of company, recruiter, job title
	- Select:
		- Example job experience, achievements and "others"
		- One or more skills applicable for the job
		- Template to be used (one or more)

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

### How to run
1. From the command line execute:
```commandline
python -m uvicorn cover-letters.api.endpoints:app --reload
python -m uvicorn api.endpoints:app --reload
```
2. To see the docs (inc all endpoints):
```url
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


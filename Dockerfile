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
# TODO: Still confused why we can't do this through docker-compose.yaml
CMD ["uvicorn", "api.endpoints:app", "--host=0.0.0.0", "--reload"]
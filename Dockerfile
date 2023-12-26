# Specify the parent image (in this case Python)
FROM python:3.8

# Name the working dir
WORKDIR /app

# Copy "local" files to the container (in the `/app` folder)
COPY ./api/ ./api/
COPY ./requirements.txt .

# Install requirements in the container
RUN pip install --upgrade pip
# PRE-REQUISITE: Don't forget to refresh your requirements by doing : `pip freeze > requirements.txt`
RUN pip install -r ./requirements.txt

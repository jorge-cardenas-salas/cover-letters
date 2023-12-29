# We copy the kernel functionality here. I'm using Python but it can be Devian, Ubuntu, ETC
FROM python:3.11

# Name the working dir
WORKDIR /app

# Copy "local" files to the container (in the `/app` folder)
COPY ./api/ ./api/
COPY ./tests/ ./tests/
COPY ./requirements.txt .

# Install requirements in the container
RUN pip install --upgrade pip
# PRE-REQUISITE: Don't forget to refresh your requirements by doing : `pip freeze > requirements.txt`
RUN pip install -r ./requirements.txt

# Next section to be able to connect to Azure
## Make sure we get the latest version of our requirements
RUN apt-get update
## Start with installations
RUN apt-get install -y odbcinst
## This gets the MS SQL Drivers for Debian (apparently the default for the image is Debian)
### Get the public keys to be able to pull the sources from MS
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
### Get the drivers
RUN curl https://packages.microsoft.com/config/debian/9/prod.list | tee /etc/apt/sources.list.d/mssql-release.list
RUN apt update
### Annoying, I need to accept the EULA. This was a HEADACHE to figure out
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18
RUN apt install -y unixodbc-dev
RUN apt-get install -y unixodbc

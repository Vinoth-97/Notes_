# NOTES_APP
The place where  to save the notes for future purpose with CRUD operations posted via GCP
It can be used as a reminder.

BACKEND

Python


CRUD OPERATIONS:

Accessing the API routes by appending api/users to the end of the web address, as per the REST standard, allows for basic CRUD activities.

CLOUD APP:

Google Cloud Platform


DOCKER FILE:

FROM python:3.8
 
 Set the working directory to /app
WORKDIR /app

copy the requirements file used for dependencies
COPY requirements.txt .

Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

 Run app.py when the container launches
CMD [ "python3", "main.py", "--host=0.0.0.0"]

VIEWING THE APP

IP:http://127.0.0.1:8080

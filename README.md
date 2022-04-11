### NOTES_APP
Notes_App is place where to save the notes for future purpose with CRUD operations posted via GCP

*The main aim of this project is to demonstrate **CRUD Rest API** operations using python flask.

*Hosting the Flask application in Google Cloud platform using **Docker Containerization Tools**

*Upgrading the defaults http credentials to HTTPS using cretbot

# Tools/Technologies used in this Project
1. Visual Studio Code for Python source code editing
2. Github for Cloning repository in cloud vm instance
3. Goocle Cloud platform - COMPUTE ENGINE- Creating a VM instance to run our container
4. Docker for the Containerization of our application to run on multiple devices
5. Python installed on local machine.
6. nginx to install web server
7. SQLAlchemy
## Running the Cloud instance

As of now, for demonstation purpose you can see the live site at

https://www.notes-app.shop/login

In future the VM instance might be turned off, In that case please use the following steps to recreate the site in your Cloud VM instance.

Step 1. Create a VM Instance using Google Cloud Programming
Step 2. Conntect to the Instance via SSH
Step 3.  Run the following commands

```bash
sudo apt install git
```

```bash
sudo apt install docker.io
```
To check if docker is running 

```bash
sudo systemctl status docker
```
Procedd if status is active

**The Docker tool is used for virtualization and contains the Entry point to our project**
Now builing docker using 
```bash
sudo docker build -t note app .
```
```bash
sudo docker run -d -p 81:8080 note-app:latest
```

```bash
sudo nano /etc/nginx/sites-available/default
```
To Convert Http tp Https we are going to use certbot to create a SSL Certificate
```bash
sudo apt-get install python-certbot-nginx
```

```bash
sudo certbot --nginx -d notes-app.shop -d www.notes-app.shop
```

## Running the Flask application on LocalHost

## Setup & Installtion

Please make sure you have the latest python version installed, please refer https://www.python.org/

```bash
git clone https://github.com/navinravikumar98
```

```bash
pip install -r requirements.txt
```
```bash
cd <path of the main.py file>
```
## Running The App

```bash
python main.py
```

## Viewing The App

Go to `http://127.0.0.1:8080`


### BACKEND

Implementing the python app using flask
CRUD OPERATIONS:

Accessing the API routes by appending api/users to the end of the web address, as per the REST standard, allows for basic CRUD activities.

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

### FUTURE ENHANCEMENTS
We have developed a python code to call an external restful API called https://www.tvmaze.com/api, In future we add this External api to our python program to make notes app more interactive and also uselful for finding TV show names from their titles.

Using SQL Alchemy we can call an cloud database to store even more data and increase reliability and availability.


# Book Store
This repo includes book store backend. 
# Installation

  - Copy the env.sample file to .env and add credentials.
  - Activate a new virtualenv and install the required packages using:
  - ```$ pip install -r requirements.txt```
  
# Errors and Solutions
 If you are facing the following error while installation:
 ```python setup.py egg_info" failed with error code 1```
 On Linux:
 ```sudo apt-get install libmysqlclient-dev```
 On Mac:
 ```brew install mysql```
 
# How to create database with user

  create database mydb;
  create user myuser;
  GRANT permissions ON DATABASE mydb TO myuser;
  

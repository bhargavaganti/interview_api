# Interview Api
Simple api for scheduling interview. There can be two roles that use this API, a candidate and an interviewer.

## Description
Currently project has three api:

- **Create User Api**

  - Creating user. Url : */user/create*

  - Paramters

    | Name | Type | Description | Required |
    | :---: | :---: | :---: | :---: |
    | `username` | string | Username must be unique. | * |
    | `role` | string | Roles can be **candidate** or **interviewer**. | * |
    | `name` | string | Name of the user. | * |
    
  - *Response* : status of request

- **Add Slot Api**

  - Adding available time slots of user.  Url : */availability/create*
  
  - Paramters
  
    | Name | Type | Description | Required | Default |
    | :---: | :---: | :---: | :---: | :---: |
    | `username` | string | Username of user. | * | |
    | `weeks` | string | Weeks can be  **current** or **next** separated with comma. |  | all weeks |
    | `days` | string | Days can be **mon, tue, wed, thu, fri** separated with comma. |  | all days|
    | `hours` | string | Format is **start_hour, end_hour**. Hour ranges are **9..18** |  | all working hours|
    
  - *Response* : status of request

- **Check Interview Api**

  - Checking interview for users. Url : */interview/check*
   
  - Paramters
    
    | Name | Type | Description | Required | Default |
    | :---: | :---: | :---: | :---: | :---: |
    | `users` | string | Usernames seperated with comma | * | |
    
  - *Response* : 
  
      Time slots when all users are available.
      Each time slot have **week, weekday and start/end time array** informations.
      **week** : *current* or *next*
      **days** : one of **mon, tue, wed, thu, fri**
      **start_time, end_time** : Times in 12 hour format.

- Project has util module
  - Util : Common infrastructure

## Installation

### Environment 
- Python 3.6
- PostgreSQL 10

### Install PostgreSQL
-   https://www.postgresql.org/download/

### Virtual environment (Optional)
    $ cd code  # root directory
    $ virtualenv -p python3 venv
    $ source venv/bin/activate

### Dependicies
    $ python setup.py install

### Create a DB
    $ psql
    $ CREATE ROLE chemondis WITH CREATEDB CREATEROLE LOGIN;
    $ CREATE DATABASE schedule OWNER chemondis;
    
### Create tables
    $ cd code  # root directory
    $ python manage_db.py create
    
## Running downloader service
    $ python schedule/__init__.py 
    
or

    $ interview

## Usage
-   **Create users:**
    -- http://0.0.0.0:1818/user/create?username=carl@gmail.com&role=candidate&name=Carl
    -- http://0.0.0.0:1818/user/create?username=philipp@gmail.com&role=interviewer&name=Philipp
    -- http://0.0.0.0:1818/user/create?username=sarah@gmail.com&role=interviewer&name=Sarah

-   **Add slots:**
    -- http://0.0.0.0:1818/availability/create?username=philipp@gmail.com&weeks=next&hours=9,16
    -- http://0.0.0.0:1818/availability/create?username=sarah@gmail.com&weeks=next&days=mon,wed&hours=12,18 
    -- http://0.0.0.0:1818/availability/create?username=sarah@gmail.com&weeks=next&days=tue,thu&hours=9,12 
    -- http://0.0.0.0:1818/availability/create?username=carl@gmail.com&weeks=next&hours=9,10
    -- http://0.0.0.0:1818/availability/create?username=sarah@gmail.com&weeks=next&days=wed&hours=10,12

-   **Check interview:**
    -- http://0.0.0.0:1818/interview/check?users=philipp@gmail.com,carl@gmail.com,sarah@gmail.com
    

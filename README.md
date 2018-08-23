# StackOverflow-lite

[![Coverage Status](https://coveralls.io/repos/github/joshNic/Stack0verflow-lite/badge.svg)](https: // coveralls.io/github/joshNic/Stack0verflow-lite)
[![Build Status](https://travis-ci.org/joshNic/Stack0verflow-lite.svg?branch=tests)](https: // travis-ci.org/joshNic/Stack0verflow-lite)

- StackOverflow-lite is a platform where people can ask questions and provide answers.

- This branch contains API endpoints for the above application and tests

# Tools Used
- `Python3.4` - A High Level Programming Language
- `Flask` - Python based web framework
- `Pytest` - A Python testing  framework which makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries
- `Virtualenv` - A tool to create isolated virtual environment

# Running the tests
To run tests run this command below in your terminal

```
py.test - -cov-report term - -cov = tests/
```

# Installation
**Clone this _Repository_**
```
$ https: // github.com/joshNic/-StackOverflow-lite.git
$ cd StackOverflow-lite
```
**Create virtual environment and install it**
```
$ virtualenv - -python = python3 venv
$ source / venv/bin/activate
```
**Install all the necessary _dependencies_ by**
```
$ pip install - r requirements.txt
```
**Run _app_ by**
```
$ Python run.py
$ Run the server At the terminal or console type
```
# End Points
|           End Point | Functionality |
| -------------------------------------- | ----------------------------------------- |
|     POST   api/v1/question | Post a new Question |
|     POST api/v1/question/<int: questionId > /answer | Post answer to question |
|     GET  api/v1/question/<int: questionId > |             Get a specific question |
|     GET  api/v1/questions | Get all Questions |


# End Points Reponse structure
# Get Questions Endpoint Response Structure
```
Response 200 (application/json)
{
    "questionId": 1,
    "title": "What does 404 mean",
    "body": "So i came across this and i dont know what it means"
}
```
# Get single Questions Endpoint Response Structure
```
+ Parameters
    + questionId: __(required, number) - ID of the Question in form of an integer
Response 200 (application/json)
{
    "questionId": {questionId},
    "title": "What does 404 mean",
    "body": "So i came across this and i dont know what it means"
}
```
# Post Questions Endpoint Response Structure
```
Response 201 (application/json)
body
    {
        "title": "What does 404 mean",
        "body": "So i came across this and i dont know what it means"
    }
```

# Post Answer Endpoint Response Structure
```
+ Parameters
    + questionId: __(required, number) - ID of the Question you are answering in form of an integer
Response 201 (application/json)
body
    {
        "questionId": {questionId},
        "answer_body": "So i came across this and i dont know what it means"
    }
```

# Contributors
- [Joshua Mugisha](https: // github.com/joshNic)

# Documentation
- The API is documented[HERE](https: // stackv1.docs.apiary.io/  # )

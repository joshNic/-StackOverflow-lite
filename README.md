# StackOverflow-lite
StackOverflow-lite is a platform where people can ask questions and provide answers.

- This branch contains API endpoints for the above application and tests

## Tools Used
- `Python3.4` - A High Level Programming Language
- `Flask` - Python based web framework
- `Pytest` - A Python testing  framework which makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries
- `Virtualenv` - A tool to create isolated virtual environment

## Running the tests
To run tests run this command below in your terminal

```
py.test --cov-report term --cov=tests/
```

## Installation
**Clone this _Repository_**
```
$ https://github.com/joshNic/-StackOverflow-lite.git
$ cd StackOverflow-lite
```
**Create virtual environment and install it**
```
$ virtualenv --python=python3 venv
$ source /venv/bin/activate
```
**Install all the necessary _dependencies_ by**
```
$ pip install -r requirements.txt
```
**Run _app_ by**
```
$ Python run.py
$ Run the server At the terminal or console type
```
## End Points
|           End Point                      |            Functionality                   |
|   -------------------------------------- | -----------------------------------------  |
|     POST   api/v1/question           |             Post a new Question           |
|     POST api/v1/question/<int:questionId>/answer        |         Post answer to question            |
|     GET  api/v1/question/<int:questionId>  |             Get a specific question          |
|     GET  api/v1/questions         |            Get all Questions          |


## Contributors
- [Joshua Mugisha](https://github.com/joshNic)
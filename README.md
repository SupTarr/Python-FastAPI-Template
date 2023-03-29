# Python FastAPI Template

## About The Project

This project was completed as part of `Python API Development - Comprehensive Course for Beginners` form `freeCodeCamp`. I am tasked to make full use of FastAPI and Python knowledge and its accompanying documentation to create an APIs for social media applications.

## Technologies

This project was created with:

- Python
- FastAPI
- PostgreSQL

## Installation

### Run Locally

Clone the project

```sh
git clone https://github.com/SupTarr/Python-FastAPI-Template.git
```

### Virtual environment on windows

To install `virtualenv` via pip

```cmd
py -m pip install --user virtualenv
```

To create a `virtual environment` for your project, open a new command prompt, navigate to the folder where you want to create your project and then enter the following:

```cmd
py -m virtualenv .
```

To activate the environment, run:

```cmd
.\Scripts\activate.bat
```

(Python-FastAPI-Template) C:\Users\tatas\Desktop\SupTarr\Workspace\Python-FastAPI-Template>

In the command prompt, ensure your virtual environment is active, and execute the following command:

```cmd
pip install -r requirements.txt
```

### FastAPI

```cmd
uvicorn app.main:app --reload
```

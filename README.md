

<p align="center">
<h1 align="center">django</h1>


## Table Of Contents
- [Table Of Contents](##Table-Of-Contents)
- [About The Project](##About-The-Project)
- [Setup Project](##Setup-Project)
- [Prerequisites](##Prerequisites)
- [Virtual Environment](###Virtual-Environment)
  - [Install Django](###Install-Django)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
  - [Creating A Pull Request](#creating-a-pull-request)
- [License](#license)
- [Authors](#authors)
- [Acknowledgements](#acknowledgements)

## About The Project


## Setup Project

<p>Clone the project with the url "https://github.com/pkgs4u/learn_django.git".</p>

## Prerequisites

### Virtual Environment
<p>Configure virtual environment if not.</p>

```bash
$ python -m venv venv
$ venv\Scripts\activate.bat
```

### Install Django

```bash
$ pip install django
```


### Create and run Migrations:

1) Add apps details under **_Installed_Apps_** in settings.py. Example 'products.apps.ProductsConfig'. ProductConfig is available inside apps.py under your app folder (Eg: Products folder).
2) Make sure you stop the server while you run migrations. Run this to generate migration file.
```shell
$ python manage.py makemigrations
``` 
3) A migration file will get created under the migrations folder under your app folder(Eg: Products folder).
4) Run this to execute the created migration file to create or changes in database.
```shell
$ python manage.py migrate
``` 


### Create SuperUser

```bash
$ python manage.py createsuperuser
```


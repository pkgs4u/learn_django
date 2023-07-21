

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

1) Add apps details under Installed_Apps in settings.py. Example 'products.apps.ProductsConfig'. ProductConfig is available inside apps.py under products folder.
2) Make sure you stop the server while you run migrations. Run ```bash $ python manage.py makemigrations```. A migration file will get created under the migrations folder under products folder.
3) Run ```bash $ python manage.py migrate```. This executes the migration file to create or changes in database.




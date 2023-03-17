# boardgames-django
REST API for rating boardgames made with Django

## Setup

* Create virtual environment and install project dependencies using
  [pipenv](https://pipenv.pypa.io/en/latest/install/#installing-packages-for-your-project):

  `pipenv install`
* Create `.env` file with following environment variables:
  * SECRET_KEY - generate using `django.core.management.utils.get_random_secret_key`

## Usage

* Run application:

  `pipenv run uvicorn src.main:app`

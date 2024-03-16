# Overview

An example DJango 5.0 service (DRF with tests) using postgresql that can also be run with gunicorn.

**WARNING** - This IS NOT intended to be an actual useful user service, it's just an example service using
a model that could be easily understood.

This is an extremely basic Django service using DRF to serve a simple user record.
Its main purpose is just for experimenting with Django and DRF, with a special emphasis on using
gunicorn and having other systems call this service.

## Setup of Environment

* Initialize mamba environment `mamba create -n django-user-service -c conda-forge  python=3.12`
* `mamba activate django-user-service`
* `pip install poetry`
* `poetry install --no-root`
* `python manage.py migrate`
* `python manage.py createsuperuser`
* `python manage.py runserver`
  *  Alternatively can run with gunicorn `gunicorn --bind 0.0.0.0:8000 user_service.wsgi -w 1`
* `python manage.py test`
* `mypy .`
* `black .`


## Relevant DB Queries

```sql
-- Generate some fake user records
INSERT INTO usercore_user (name, age)
SELECT
    substr(concat(md5(random()::text), md5(random()::text)), 1, (random() * 64)::integer + 1) AS name,
    random()::integer AS age
FROM generate_series(1,10000) as n
;

-- Check on the table
SELECT COUNT(*) FROM usercore_user;
```
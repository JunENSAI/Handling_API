# Handling_API

## Advices :

- Create a virtual environnement to make sure that the packages does not collapse with other dependencies

```bash
python3 -m venv name_env
```

- To activate the virtual environnement that you name :

```bash
source path/name_env/bin/activate
```
- Install the packages required for this repo :

```bash
pip install -r requirements.txt
```
---

## P3

P3 concers django as backend API so if you wanna retake from scratch you must follow those steps :

- Create a django project

```bash
django-admin startproject P3 .
```

- Create an app named as you like

```bash
python3 manage.py startapp api
```

- Register the App : open `./P3/settings` and search the lines `INSTALLED_APPS` then add two more lines :

```text
INSTALLED_APP=[

    'rest_framework',
    'api',
]
```

- Look at `django_api/views.py` and `P3/urls.py` then make migrations :

```bash
python3 manage.py migrate
```
- Run the server :

```bash
python3 manage.py runserver
```


---
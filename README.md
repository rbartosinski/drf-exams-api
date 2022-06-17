# Django REST Framework - Exams API

## 1. Installation

Clone the repository:

`git clone https://github.com/rbartosinski/drf-exams-api.git`

Create/activate the fresh Virtualenv and do the command:

`pip install -r requirements`

After correct installation of the dependencies find `manage.py` file and execute:

`python manage.py migrate`

`python manage.py createsuperuser`

`python manage.py drf_create_token <user_name_here>`

Example:

`python manage.py drf_create_token radek`

Run the development server:

`python manage.py runserver`

## 2. Model / database structure

Exam table:
```
{
    "id": 1,
    "name": "Exam math",
    "description": "My new math exam",
    "final_grade": 4,
    "owner": 1
}
```
Task table (related with the exam):
```
{
    "id": 1,
    "name": "Math task 1",
    "description": "My new math task",
    "exam": 1,
    "points": 5
}
```

## 3. Endpoints

#### *Each listed below endpoint is available for non- authenticated user using "safe" methods: GET, HEAD, OPTIONS

#### Only authenticated user can execute methods: POST, PUT, PATCH, DELETE

### Exams list / Create exam

`api/exams/`

#### Description:

Allow: GET, POST, HEAD, OPTIONS

Content-Type: application/json

Vary: Accept

#### Filters available:

Examples:
```
http://127.0.0.1:8000/api/exams/?ordering=owner
http://127.0.0.1:8000/api/exams/?ordering=-owner
http://127.0.0.1:8000/api/exams/?ordering=final_grade
http://127.0.0.1:8000/api/exams/?ordering=-final_grade
http://127.0.0.1:8000/api/exams/?ordering=name
http://127.0.0.1:8000/api/exams/?ordering=-name
```
----
### Exam details / edit / delete

`api/exams/<exam_id>/`

#### Description

Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS

Content-Type: application/json

Vary: Accept

----

### Tasks list / create task

`api/exams/<exam_id>/tasks/`

#### Description: 

Allow: GET, POST, HEAD, OPTIONS

Content-Type: application/json

Vary: Accept

----

### Task details / edit / delete

`api/exams/<exam_id>/tasks/<task_id>/`

#### Description: 

Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS

Content-Type: application/json

Vary: Accept

## 4. Authentication

Authentication can be done via DRF auth token. It has to be passed through via header:

`curl http://127.0.0.1:8000/hello/ -H 'Authorization: Token 9054f7aa9305e012b3c2300408c3dfdf390fcddf'`

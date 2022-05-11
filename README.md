# Blog

## Installation

First, clone the project:

```bash
git clone https://github.com/Rodrigovvo/blog.git
```

Create a virtualenv:

```bash
$ python -m venv env
```

Activate venv enviroment:

```bash
(windows)
myenv\Scripts\activate.bat

(linux/MacOs)
$ source env/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

For default the database used in this project is a sqLite and is already fulfilled. If you need to create a new database, after the creation run this commands:
```bash
python manage.py makemigrations
python manage.py migrate
```
For create a new superuser run this command:
```bash
python manage.py createsuperuser
```

Finaly, run the project:
```bash
python manage.py runserver
```
After all these steps, you can start testing this project. 

#### Credentials
For access the django admin controls, you can use the default admin

email: admin@admin.com
password: admin 

Or, you can use a author role user:
email: blog@email.com
password: admin 

#### Autor 
- Rodrigo Vinicius Vieira Oliveira - [@Rodrigovvo](https://github.com/Rodrigovvo) 

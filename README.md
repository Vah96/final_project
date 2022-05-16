# Aphorism

## Project installation

To install project please first clone it on your local computer. After cloning the project you will need to create a 
python environment and install requirements for that. To be sure we have known that you already downloaded needed 
(3.9.6) python stable version and have installed it on your computer.

### Setup Environment

We need package `virtualenv` for virtual environments. If you need more help or documentation this link may give some
help:
[VirtualEnv package documentation](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

Run following command to install it:

On macOS and Linux:

```
python3 -m pip install --user virtualenv
```

On Windows:

```
py -m pip install --user virtualenv
```

After package installation we need to create a virtual environment for our project. Run the following command to create
a folder with virtual environment files:

On macOS and Linux:

```
python3 -m venv env
```

On Windows:

```
py -m venv env
```

The second argument is the location to create the virtual environment. Generally, you can just create this in your
project and call it `env`.

After Environment has been created we need to activate it:

On macOS and Linux:

```
source env/bin/activate
```

On Windows:

```
.\env\Scripts\activate
```

Now we need to install requirements for our project. To do that first we need to change our directory to `final_project/`
and then run installation:

```
cd final_project/
python -m pip install -r requirements.txt
```

### Setting project for first run

After all installations we need to do migrate all project migrations.

#### Note! All commands should be run in final_project folder. Run following command if you did not do that before this step

```
cd final_project/
```

Do migrations to create clean database:

```
python manage.py migrate
```

First lets create migrations via following command. Note! Do this command if migrate shows some models 
changes with no migration file.

```
python manage.py makemigrations
```

### Admin User

For administration you need an admin user. To do that make following command and fill required fields as asked:

```
python manage.py createsuperuser
```

## Add some test users, tags and aphorism

```
python manage.py save_aphorisms
```

## Delete all frontend users

When you remove all frontend users, aphorisms that has relation with deleted user(s) will be removed 
automatically too 

```
python manage.py delete_frontend_users
```

## Delete all aphorisms

```
python manage.py delete_aphorisms
```

## Delete all tags

```
python manage.py delete_tags
```

## Run server

To run a local server use command below:

```
python manage.py runserver
```

This run a local server which will be accessible by URL [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
Admin Panel URL [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

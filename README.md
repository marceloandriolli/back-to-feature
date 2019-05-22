<img src="http://i67.tinypic.com/2q9gzlu.png" alt="" width="200" height="80">


### Introdution
Manage feature request could be a challenger, handle of stale data, keeping everything in one place, etc...
Back to the Feature is web app that make easy creates feature requests.

### Dependences ###

* Python 3.7+

Install Pyenv:
https://github.com/pyenv/pyenv#installation

Intall virtualenv for Pyenv:
https://github.com/pyenv/pyenv-virtualenv


Create and active a virtual environment.

```
pyenv install 3.7.0a3
pyenv virtualenv 3.7.0a3 venv
pyenv activate venv
```

### Setup database 

* You need to create a databaes and user in PostgreSQL:

Create database: `createdb back-to-feature-db`
Create user: `createuser -P -s deLorean_admin`

* Create environment variables:
```
cp contrib/env-sample .env
```

* Fill environment variables defined in .env file
* Generate Key for CSRF_SESSION_KEY and SECRET using contrib:
```
python contrib/secret_gen.py
```
Copy the output and past it at each keys in .env file
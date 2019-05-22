import os
from decouple import config
from dj_database_url import parse as dburl


# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Statement for enabling the development environment
DEBUG = config('DEBUG', default=False, cast=bool)

# Define the database - we are working with
# SQLite for this example

default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_DATABASE_URI = config('DATABASE_URL', default=default_dburl, cast=dburl)
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = config('CSRF_ENABLED', default=True, cast=bool)

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = config('CSRF_SESSION_KEY')

# Secret key for signing cookies
SECRET_KEY = config('SECRET_KEY')
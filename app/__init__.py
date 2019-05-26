from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('settings')

# Define the database object which is imported
# by modules and views
db = SQLAlchemy(app)

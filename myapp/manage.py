import os
from flask import Flask
from flask import request
from main.views import HomeViewAPI
from login.views import LoginViewAPI
from register.views import RegisterViewAPI

app = Flask(import_name=__name__,
            # static_url_path='',
            # static_folder='',
            # static_host='',
            # host_matching='',
            # subdomain_matching='',
            # template_folder='',
            # instance_path='',
            # instance_relative_config='',
            # root_path='',
)
DEBUG = True
app.config['ENV'] = 'development' if DEBUG else 'production'
app.config['DEBUG'] = True if DEBUG else False



app.add_url_rule('/', view_func=HomeViewAPI.as_view('home'))
app.add_url_rule('/login', view_func=LoginViewAPI.as_view('login'))
app.add_url_rule('/register', view_func=RegisterViewAPI.as_view('register'))

if __name__ == "__main__":
    app.run()
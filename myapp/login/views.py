from flask.views import MethodView
from flask import request


class LoginViewAPI(MethodView):
    def get(self, *args, **kwargs):
        return 'login page'
        
    def post(self, *args, **kwargs):
        pass
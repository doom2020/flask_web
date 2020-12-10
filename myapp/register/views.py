from flask import request
from flask.views import MethodView


class RegisterViewAPI(MethodView):
    def get(self, *args, **kwargs):
        return 'register page'
        
    def post(self, *args, **kwargs):
        pass

from flask import request
from flask.views import MethodView


class HomeViewAPI(MethodView):
    def get(self, *args, **kwargs):
        return 'home page'


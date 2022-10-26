from flask import render_template
from flask.views import MethodView


class QueryView(MethodView):
    init_every_request = False
    def get(self):
        return render_template('query.html')
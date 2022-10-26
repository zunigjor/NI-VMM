from flask.views import MethodView


class Images(MethodView):
    init_every_request = False

    def get(self):
        return "Hello from images!"

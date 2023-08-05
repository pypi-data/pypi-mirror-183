import flask

class Spinne():
    """the part you'd use to run your app :)"""
    def __init__(self, name):
        self.name = name
        self.app = flask.Flask(name)

    def run(self, host = "0.0.0.0", port = 5000):
        return self.app.run(host, port)

    def render(self, function):
        @self.app.route("/<route>")
        @self.app.route("/")
        def locate(route):
            if not route:
                return function("index")
            return function(route)

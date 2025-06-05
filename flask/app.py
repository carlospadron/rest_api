from flask import Flask

def create_app():
    app = Flask(__name__)
    app.items = {}  # in-memory storage
    import routes
    routes.init_app(app)
    return app

app = create_app()
if __name__ == '__main__':
    app.run(debug=True)
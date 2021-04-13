from flask_swagger import swagger
from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

from persons import PersonAPI

app = Flask(__name__)

app.register_blueprint(get_swaggerui_blueprint(
    '/api/docs',
    '/api/spec',
    config={
        'app_name': "My App"
    }
))


@app.route("/api/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "My API"
    return jsonify(swag)


view = PersonAPI.as_view('persons')
app.add_url_rule('/api/persons/<int:id>', view_func=view, methods=["GET"])
app.add_url_rule('/api/persons', view_func=view, methods=["POST"])

from openapi.api_definition import ApiDefinition
from Backend.backend import Backend
from flask import render_template

api = ApiDefinition(api_file= 'my_api.yaml')
app = api.connexion_app.app

@app.before_request
def get_before_request():
    backend = Backend(host='localhost', port='5432', username='postgres', password='1234', db='world')
    ApiDefinition.backend = backend


@app.route('/')
def home_page():
    return render_template('index.html')

app.jinja_env.globals.update()

app.run()
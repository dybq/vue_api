from flask import Flask, redirect, url_for
from flask_restful import Resource, Api
from mysql import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={"/api/*":{"origins": "*"}})

api = Api(app)

@app.route("/")
def index():
    return redirect('http://localhost:8080')

class GetData(Resource):
    def get(self):
        return getData('make_group', 'username', 'datetime', 'diff', 'remark')


api.add_resource(GetData, '/api/getdata')

if __name__ == '__main__':
    app.run()

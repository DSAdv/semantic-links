from flask import Flask
from flask_restful import Api

from src.resources.document import Document
from src.resources.search import Search


app = Flask(__name__)
api = Api(app=app)

api.add_resource(Document, "/doc", "/api/doc/<string:text_id>")
api.add_resource(Search, "/search", "/api/search/<string:text_id>")


if __name__ == '__main__':
    app.run(debug=True)

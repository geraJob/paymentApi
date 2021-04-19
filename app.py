from flask import Flask
from flask_cors import CORS, cross_origin
from flask_restful import Api
import os,resources
app = Flask(__name__)
api = Api(app = app)
cors = CORS(app,resource={r'/*':{'origins':'*'}})
app.config['CORS_HEADERS'] = 'Content-type'
app.secret_key= os.environ.get('secretKey',"mito")

api.add_resource(resources.Transactions,'/')

def main():
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)

if __name__ == "__main__":
    main()
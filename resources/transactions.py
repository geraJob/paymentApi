from flask import request
from flask_restful import Resource
from decorator.decorator import decorator_key
from features.gateway import gateway


class Transactions(Resource):
    @decorator_key
    def post(self):
        params = request.json
        try:
            result = gateway.transaction.create(params)
            return {
                "status":201,
                "response":result
            },200
        except Exception as e:
            return {
                'status':400,
                "response":str(e)
            }




    
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
                "status":200,
                "response":result
            },200
        except Exception as e:
            return {
                'status':404,
                "response":str(e)
            },200
    
class Refund(Resource):
    @decorator_key
    def get(self,id):
        try:
            transaction = gateway.transaction.find_by({'id':id})
            result = gateway.transaction.refund(id,
            {"amount":transaction[0]['amount']}
            )
            return {
                'status':200,
                'response':result
            },200
        except Exception as e:
            return {
                'status':404,
                'response':str(e)
            },200


class Plan(Resource):
    @decorator_key
    def post(self):
        plan = request.json
        try:
            result_plan = gateway.plan.create(plan)
            return {
                'status':200,
                'response':result_plan
            },200
        except Exception as e:
            return {
                'status':404,
                'response':str(e)
            },200 
    
    @decorator_key
    def get(self):
        try:
            result = gateway.plan.find_all()
            return {
                'status':200,
                'response':result
            },200
        except Exception as e:
            return {
                'status':404,
                'response':str(e)
            },200
    @decorator_key
    def put(self):
        update = request.json
        id = update.pop('id') 
        try:
            result = gateway.plan.update(id,update)
            return {
                'status':200,
                'response':result
            },200
        except Exception as e:
            return {
                'status':404,
                'reposnse':str(e)
            },200

            






    





    
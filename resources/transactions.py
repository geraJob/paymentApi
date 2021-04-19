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
                'status':409,
                "response":str(e)
            },200
    
    @decorator_key
    def get(self):
        try:
            result = gateway.transaction.find_all()
            return {
                'status':200,
                'response':result
            },200
        except Exception as e:
            return {
                'status':409,
                'response':str(e)
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
                'status':409,
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
                'status':409,
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
                'status':409,
                'response':str(e)
            },200
    @decorator_key
    def put(self):
        update = request.json
        id = update.pop('id') 
        if id == null:
            return {
                'status':400,
                "response":"id required"
            },200
        try:
            result = gateway.plan.update(id,update)
            return {
                'status':200,
                'response':result
            },200
        except Exception as e:
            return {
                'status':409,
                'response':str(e)
            },200

class Subscription(Resource):
    @decorator_key
    def post(self):
        subscription = request.json
        try:
            result = gateway.subscription.create(subscription)
            return {
                'status':200,
                'response':result
            },200
        except Exception as e:
            return {
                'status':409,
                'response':str(e)
            },200
    @decorator_key
    def get(self):
        try:
            result = gateway.subscription.find_all()
            return {
                'status':200,
                'response':result
            },200
        except Exception as e:
            return {
                "status":409,
                'response':result
            }


class SubscriptionById(Resource):
    @decorator_key
    def get(self,id):
        try:
            subscription = gateway.subscription.find_by({'id':id})
            return {
                'status':200,
                'response':subscription
            },200
        except Exception as e:
            return {
                'status':409,
                'response':str(e)
            },200
    
    @decorator_key
    def put(self,id):
        update = request.json
        try:
            result = gateway.subscription.update(str(id),update)
            return {
                'status':200,
                'response':result,
            },200 
        except Exception as e:
            return {
                'status':409,
                'response':str(e)
            },200
            
class SubscriptionCancel(Resource):
    @decorator_key
    def post(self,id):
        try:
            cancel_subscription = gateway.subscription.cancel(str(id))
            return {
                'status':200,
                'response':cancel_subscription
            },200
        except Exception as e:
            return {
                'status':409,
                'response':str(e)
            },200

class SubscriptionAllTransactionsById(Resource):

    @decorator_key
    def get(self,id):
        try:
            transactions = gateway.subscription.transactions(id)
            return {
                'status':200,
                'response':transactions
            },200
        except Exception as e:
            return {
                'status':409,
                'response':str(e)
            },200

class Cards(Resource):
    @decorator_key
    def post(self):
        card = request.json
        try:
            result = gateway.card.create(card)
            return {
                'status':200,
                'response':result
            },200
        except Exception as e:
            return {
                'status':409,
                'response':str(e)
            },200
    
    @decorator_key
    def get(self):
        try:
            cards = gateway.card.find_all()
            return {
                'status':200,
                'response': cards
            },200
        except Exception as e:
            return {
                'status':409,
                'response':str(e)
            },200

class CardById(Resource):
    @decorator_key
    def get(self,id):
        try:
            card = gateway.card.find_by({'id':id})
            return {
                'status':200,
                'response':card
            },200
        except Exception as e:
            return {
                'status':409,
                'response':str(e)
            },200








    





    
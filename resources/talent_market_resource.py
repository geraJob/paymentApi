from flask import request
from flask_restful import Resource
from decorator.decorator import decorator_key
from src.core.core import Core
from src.infra.models import ResultTalentMarketItem
class TalentMarket(Resource):
    @decorator_key
    def post(self):
        data = request.json
        
        try:
            talentMarket = ResultTalentMarketItem.fromData(data)
            result : ResultTalentMarketItem = Core().talent_market_usecases.createItem(talentMarket)
            return {
                'status':201,
                'response':result.toMapWithId()
            },200
        except Exception as e:
            return {
                'status':409,
                'response':str(e)
            },200

    @decorator_key
    def get(self):
        try:
            results = Core().talent_market_usecases.getAll()
            talentsMarkets = [doc.toMapWithId() for doc in results]
            return {
                'status':200,
                'response':talentsMarkets
            },200
        except Exception as e:
            return {
                'status':409,
                'response':str(e)
            },200

class TalentMarketById(Resource):
    @decorator_key
    def get(self,id):
        try:
            talentMarket : ResultTalentMarketItem= Core().talent_market_usecases.getByid(id)
            return {
                'status':200,
                'response':talentMarket.toMapWithId()
            },200
        except Exception as e:
            return {
                'status':409,
                'response':str(e)
            },200
    @decorator_key
    def put(self,id):
        data = request.json
        try:
            item = ResultTalentMarketItem.fromData(data,id=id)
            talentMarket : ResultTalentMarketItem = Core().talent_market_usecases.updateByItem(item)
            return {
                'status':201,
                'response':talentMarket.toMapWithId()
            },200
        except Exception as e:
            return {
                'status':409,
                'response':str(e)
            },200

from flask import request
from flask_restful import Resource
from decorator.decorator import decorator_key
from src.core.core import Core
from src.infra.models import ResultItemDesignWall

class DesignWallResource(Resource):
    @decorator_key
    def post(self):
        data = request.json
        try:
            designwall : ResultItemDesignWall = ResultItemDesignWall.fromData(data) 
            result_designwall : ResultItemDesignWall = Core().design_wall_usecases.createItem(designwall)
            return {
                'status':201,
                'response':result_designwall.toMapWithId()
            },200
        except Exception as e:
            return {
                'status':409,
                'response':str(e)
            },200
    @decorator_key
    def get(self):
        try:
            results  = Core().design_wall_usecases.getAll()
            resultsItemToMap = [item.toMapWithId() for item in results]
        
            return {
                    'status':200,
                    'response':resultsItemToMap
                },200
        except Exception as e:
            return {
                    'status':409,
                    'response':str(e)
                },200
       
class DesignWallById(Resource):
    @decorator_key
    def get(self,id):
        try:
            designwall : ResultItemDesignWall = Core().design_wall_usecases.getById(id)
            return {
                'status':200,
                'response':designwall.toMapWithId()
            },200
        except Exception as e:
            return {
                'status':409,
                'response':str(e)
            },200
    
    @decorator_key
    def put(self,id):
        data = request.json
        designwall : ResultItemDesignWall = ResultItemDesignWall.fromData(data)
        designwall.id = id
        try:
            designwall_result : ResultItemDesignWall = Core().design_wall_usecases.updateByItem(designwall)
            return {
                'status':201,
                'response':designwall_result.toMapWithId()
            },200
        except Exception as e:
            return {
                'status':409,
                'response':str(e)
            },200
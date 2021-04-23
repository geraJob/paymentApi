from flask import request
from flask_restful import Resource
from decorator.decorator import decorator_key
from src.core.core import Core
from src.infra.models import ResultPredefinedProject

class PrefinedProject(Resource):
    @decorator_key
    def post(self):
        data = request.json
        
        try:
            designwall : ResultPredefinedProject = ResultPredefinedProject.fromData(data) 
            result_designwall : ResultPredefinedProject = Core().predefined_project_usecases.createItem(designwall)
            designwall : ResultPredefinedProject = ResultPredefinedProject.fromData(data) 
            result_designwall : ResultPredefinedProject = Core().predefined_project_usecases.createItem(designwall)
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
            results  = Core().predefined_project_usecases.getAll()
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
       
class PredefinedProjectById(Resource):
    @decorator_key
    def get(self,id):
        try:
            designwall : ResultPredefinedProject = Core().predefined_project_usecases.getById(id)
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
        designwall : ResultPredefinedProject = ResultPredefinedProject.fromData(data)
        designwall.id = id
        try:
            designwall_result : ResultPredefinedProject = Core().predefined_project_usecases.updateByItem(designwall)
            return {
                'status':201,
                'response':designwall_result.toMapWithId()
            },200
        except Exception as e:
            return {
                'status':409,
                'response':str(e)
            },200
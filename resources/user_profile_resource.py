from flask import request
from flask_restful import Resource
from decorator.decorator import decorator_key
from src.core.core import Core
from src.infra.models.result_user_profile import ResultUserProfile
class UserProfileResource(Resource):
    @decorator_key
    def get(self,id):
        try:
            user_profile : ResultUserProfile= Core().user_profile_usecases.getById(id)
            return {
                'status':200,
                'response':user_profile.toMap()
            },200
        except Exception as e:
            return {
                'status':409,
                'response':str(e)
            },200
    
    @decorator_key
    def put(self,id):
        data = request.json
        user_profile : ResultUserProfile =  ResultUserProfile.from_to_dict(data,id)
        try:
            Core().user_profile_usecases.updateById(user_profile)
            return {
                'status':201,
                'response':"Succesfuly update"
            },200
        except Exception as e:
            return {
                'status':409,
                'response':str(e)
            },200

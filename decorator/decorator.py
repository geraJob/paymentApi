
from flask import request
import os


key_master =  os.environ.get('secretKey',"mito")
def decorator_key(func):
    def func_args(*args,**kwargs):
        key = ""
        try:
            key = request.headers['Key']
        except:
            return {"message":"key cannot be empty in headers"}, 400
        if key != key_master:
            
            return {"message": "Unauthorized"}, 401
       
        response = func(*args,**kwargs)
        return response
        
        
    return func_args


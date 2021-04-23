import os, firebase_admin
from abc import ABCMeta,abstractclassmethod
from firebase_admin import firestore,credentials
path = os.path.dirname(os.path.abspath(__file__)).replace('/features','/utils')
db = None
try:
    cred = credentials.Certificate(path+'/gerajobsfirebase.json')
    app = firebase_admin.initialize_app(credential=cred)
    db = firestore.client(app=app)
except Exception as e:
    print(str(e))


class Collection:
    @classmethod
    def add(self,data):
        pass
    @classmethod
    def where(self,*args,**kwargs):
        return Where()
    @classmethod
    def get(self):
        pass
    @classmethod
    def stream(self):
        pass
    @classmethod
    def update(self,data):
        pass
    @classmethod
    def document(self,*args,**kwargs):
        return Document()
    @classmethod
    def set(self,*args,**kwargs):
        pass

class Where:
    @classmethod
    def where(cls,*args):
        return Where()
    @classmethod
    def get(cls):
        pass
    @classmethod
    def stream(cls):
        pass

class Document:
    @classmethod
    def get(cls):
        pass
    @classmethod
    def collection(cls,*args):
        return Collection()
    @classmethod
    def update(cls):
        pass
    @classmethod
    def delete(cls):
        pass

class Firebase:
    @classmethod
    def collection(cls):
        return Collection()
    @classmethod
    def where(cls):
        return Where()
    @classmethod
    def document(cls):
        return FirebaseDb()
   
    


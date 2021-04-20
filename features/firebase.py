import os, firebase_admin

from firebase_admin import firestore,credentials
path = os.path.dirname(os.path.abspath(__file__)).replace('/features','/utils')
db = None
try:
    cred = credentials.Certificate(path+'/gerajobsfirebase.json')
    app = firebase_admin.initialize_app(credential=cred)
    db = firestore.client(app=app)
except Exception as e:
    pritn(str(e))

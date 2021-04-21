from src.infra.datasources.user_repository_datasource import UserProfileDataSource
from src.infra.models.result_user_profile import ResultUserProfile
class FirebaseDataSource(UserProfileDataSource):
    _db = None
    def __init__(self,db,**kwargs):
        self._db = db
    def getById(self,id):
        result = self._db.collection('users').document(id).get()
        user_profile = ResultUserProfile.from_to_dict(result.to_dict(),result.id)
        return user_profile
    
    def updateById(self,user_profile : ResultUserProfile):
        self._db.collection('users').document(user_profile.id).update(user_profile.toMap())
        
        

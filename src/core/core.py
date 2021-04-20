from features.firebase import db
from src.external.firebase_datasource import FirebaseDataSource
from src.infra.repositories.user_profile_repository import UserProfileRepositoryImpl
from src.domain.usecases.get_user_profile import GetUserProfileImpl
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]




class Core(object, metaclass=Singleton):
    
    def __init__(self,**kwargs):
        self.firebase_datasource = FirebaseDataSource(db)
        self.user_profile_repository = UserProfileRepositoryImpl(self.firebase_datasource)
        self.user_profile_usecases = GetUserProfileImpl(self.user_profile_repository)
        

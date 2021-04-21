from abc import ABCMeta,abstractclassmethod
from src.domain.entities.user_profile import UserProfile

class UserProfileDataSource(metaclass=ABCMeta):
    @abstractclassmethod
    def getById(self,id):
        pass
    
    @abstractclassmethod
    def updateById(self, user_profile:UserProfile):
        pass

    @abstractclassmethod
    def createById(self,user_profile):
        pass

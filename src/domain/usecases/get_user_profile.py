from abc import ABCMeta,abstractclassmethod
from src.domain.repositories.user_profile_repository import UserProfileRepository
class GetUserProfile(metaclass=ABCMeta):
    @abstractclassmethod
    def getById(self,id):
        pass
    @abstractclassmethod
    def updateById(self,user_profile):
        pass


class GetUserProfileImpl(GetUserProfile):
    repository : UserProfileRepository 
    def __init__(self,repository:UserProfileRepository,**kwargs):
        self.repository = repository

    def getById(self,id):
        return self.repository.getById(id)
    
    def updateById(self,user_profile):
        self.repository.updateById(user_profile)



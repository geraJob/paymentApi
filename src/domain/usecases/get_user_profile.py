from abc import ABCMeta,abstractclassmethod
from src.domain.repositories.user_profile_repository import UserProfileRepository
class GetUserProfile(metaclass=ABCMeta):
    @abstractclassmethod
    def getById(self,id):
        pass


class GetUserProfileImpl(GetUserProfile):
    repository : UserProfileRepository 
    def __init__(self,repository:UserProfileRepository,**kwargs):
        self.repository = repository

    def getById(self,id):
        return self.repository.getById(id)



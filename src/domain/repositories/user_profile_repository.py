from abc import ABCMeta, abstractmethod
from src.domain.entities.user_profile import UserProfile

class UserProfileRepository(metaclass=ABCMeta):
    @abstractmethod
    def getById(self,id):
        pass

    @abstractmethod
    def updateById(self,user_profile: UserProfile):
        pass

    @abstractmethod
    def createById(self,user_profile):
        pass





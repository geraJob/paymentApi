from abc import ABCMeta,abstractclassmethod

class UserProfileDataSource(metaclass=ABCMeta):
    @abstractclassmethod
    def getById(self,id):
        pass

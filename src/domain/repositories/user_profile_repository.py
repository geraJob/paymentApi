from abc import ABCMeta, abstractmethod


class UserProfileRepository(metaclass=ABCMeta):
    @abstractmethod
    def getById(self,id):
        pass





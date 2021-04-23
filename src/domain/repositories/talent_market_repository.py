from abc import ABCMeta,abstractclassmethod

class TalentMarketRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def getById(self,id):
        pass
    @abstractclassmethod
    def getAll(self):
        pass
    @abstractclassmethod
    def updateByItem(self,item):
        pass
    @abstractclassmethod
    def createItem(self,item):
        pass
from abc import ABCMeta, abstractclassmethod

class ItemDesignWallRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def getById(self,id):
        pass
    
    @abstractclassmethod
    def getAll(self):
        pass

    @abstractclassmethod
    def updateByItem(self,Item):
        pass

    @abstractclassmethod
    def create(self,id):
        pass
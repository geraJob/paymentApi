from abc import ABCMeta,abstractclassmethod
from src.domain.repositories.talent_market_repository import TalentMarketRepository

class TalentMarket(metaclass=ABCMeta):
    @abstractclassmethod
    def getByid(self,id):
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

class TalentMarketImpl(TalentMarket):
    repository: TalentMarketRepository
    def __init__(self,repository:TalentMarketRepository,**kwargs):
        self.repository = repository
    def getByid(self,id):
        return self.repository.getById(id)
    def getAll(self):
        return self.repository.getAll()
    def updateByItem(self,item):
        return self.repository.updateByItem(item)
    def createItem(self,item):
        return self.repository.createItem(item)

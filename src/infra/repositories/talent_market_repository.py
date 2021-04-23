from src.domain.repositories.talent_market_repository import TalentMarketRepository
from src.infra.datasources.talent_market_datasource import TalentMarketDataSource

class TalentMarketRepositoryImpl(TalentMarketRepository):
    datasource : TalentMarketDataSource
    def __init__(self,datasource: TalentMarketDataSource,**kwargs):
        self.datasource = datasource
    
    def getById(self,id):
        return self.datasource.getById(id)
    
    def getAll(self):
        return self.datasource.getAll()
    
    def updateByItem(self,item):
        return self.datasource.updateByItem(item)
    
    def createItem(self,item):
        return self.datasource.createItem(item)
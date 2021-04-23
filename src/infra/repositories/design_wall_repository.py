from src.domain.repositories.design_wall_repository import DesignWallRepository
from src.infra.datasources.design_wall_datasource import DesignWallDataSource

class DesignWallRepositoryImpl(DesignWallRepository):
    datasource : DesignWallDataSource
    def __init__(self,datasource:DesignWallDataSource,**kwargs):
        self.datasource = datasource
    
    def getById(self,id):
        return self.datasource.getById(id)
    
    def getAll(self):
        return self.datasource.getAll()
    
    def updateByItem(self,item):
        return self.datasource.updateByItem(item)
    
    def createItem(self,item):
        return self.datasource.createItem(item)
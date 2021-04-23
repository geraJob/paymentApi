from src.domain.repositories.predefined_project_repository import PredefinedProjectRepository
from src.infra.datasources.predefined_project_datasource import PredefinedProjectDataSource

class PredefinedProjectRepositoryImpl(PredefinedProjectRepository):
    datasource : PredefinedProjectDataSource
    def __init__(self,datasource:PredefinedProjectDataSource,**kwargs):
        self.datasource = datasource
    def getById(self,id):
        return self.datasource.getById(id)
    def getAll(self):
        return self.datasource.getAll()
    def updateByItem(self,item):
        return self.datasource.updateByItem(item)
    def createItem(self,item):
        return self.datasource.createItem(item)
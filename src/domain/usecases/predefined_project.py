from abc import ABCMeta,abstractclassmethod
from src.domain.repositories.predefined_project_repository import PredefinedProjectRepository

class PredefinedProject(metaclass =ABCMeta):
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

class PredefinedProjectImpl(PredefinedProject):
    repository: PredefinedProjectRepository
    def __init__(self,repository:PredefinedProjectRepository,**kwargs):
        self.repository = repository
    def getById(self,id):
        return self.repository.getById(id)
    def getAll(self):
        return self.repository.getAll()
    def updateByItem(self,item):
        return self.repository.updateByItem(item)
    def createItem(self,item):
        return self.repository.createItem(item)

from src.domain.repositories.user_profile_repository import UserProfileRepository
from src.infra.datasources.user_repository_datasource import UserProfileDataSource
class UserProfileRepositoryImpl(UserProfileRepository):
    datasource: UserProfileDataSource
    def __init__(self,datasource:UserProfileDataSource,**kwargs):

        self.datasource = datasource
    
    def getById(self,id):
        return self.datasource.getById(id)
    
    def updateById(self, user_profile):
        self.datasource.updateById(user_profile)
    
    def createById(self,user_profile):
        self.datasource.createById(user_profile)
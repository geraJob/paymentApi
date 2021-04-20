from src.infra.repositories.user_profile_repository import UserProfileDataSource, UserProfileRepositoryImpl
import unittest
class DataSourceMock(unittest.TestCase,UserProfileDataSource):
    def getById(self,id):
        self.assertIsNotNone(id)


datasource = DataSourceMock()
repository = UserProfileRepositoryImpl(datasource)
repository.getById("")

from src.domain.usecases.get_user_profile import GetUserProfileImpl
from src.domain.repositories.user_profile_repository import UserProfileRepository
import unittest
class RepositoryMock(unittest.TestCase,UserProfileRepository):
    def getById(self,id):
        self.assertIsNotNone(id)

repository = RepositoryMock()
usecases = GetUserProfileImpl(repository)


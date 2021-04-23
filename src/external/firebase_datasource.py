
import src.infra.datasources as datasources
import src.infra.models as models
from utils.consts import datetime_in_ms
from datetime import datetime
from features.firebase import Firebase
# User profile Firebase
class FirebaseDataSourceUserProfile(datasources.user_profile_datasource.UserProfileDataSource):
    _db:Firebase = None
    collection = 'users'
    def __init__(self,db,**kwargs):
        self._db = db
    def getById(self,id):
        result = self._db.collection(self.collection).document(id).get()
        user_profile = models.result_user_profile.ResultUserProfile.from_to_dict(result.to_dict(),result.id)
        return user_profile
    def updateById(self,user_profile : models.result_user_profile.ResultUserProfile):
        if user_profile == None:
            raise Exception('Update user profile error in database param is None')
        self._db.collection(self.collection).document(user_profile.id).update(user_profile.toMap())
    def createById(self,user_profile : models.result_user_profile.ResultUserProfile):
        if user_profile == None:
            raise Exception('Create user profile error in database param is None')
        self._db.collection(self.collection).document(user_profile.id).set(user_profile.toMap())

# Design Wall Firebase      
class FirebaseDataSourceDesignWall(datasources.design_wall_datasource.DesignWallDataSource):
    _db:Firebase = None
    collection = 'designWall'
    def __init__(self,db,**kwargs):
        self._db = db
    def getById(self,id):
        result = self._db.collection(self.collection).document(id).get()
        designWallItem = models.result_design_wall_item.ResultItemDesignWall.fromData(result.to_dict(),id=result.id)
        return designWallItem 
    def getAll(self):
        docs = self._db.collection(self.collection).stream()
        result = [ models.result_design_wall_item.ResultItemDesignWall.fromData(doc.to_dict(),id=doc.id) for doc in docs]
        return result
    def updateByItem(self,item : models.result_design_wall_item.ResultItemDesignWall):
        self._db.collection(self.collection).document(item.id).update(item.toMap())
        return item
    def createItem(self,item: models.result_design_wall_item.ResultItemDesignWall):
        item.millisecondsEpoch = datetime_in_ms()
        item.createAt = str(datetime.now())
        result = self._db.collection(self.collection).add(item.toMap())
        item.id = result[1].id
        return item

# Design Talent Market
class FirebaseDataSourceTalentMarket(datasources.talent_market_datasource.TalentMarketDataSource):
    _db:Firebase
    collection = 'talentMarket'
    def __init__(self,db:Firebase,**kwargs):
        self._db = db
    def getById(self,id):
        result = self._db.collection(self.collection).document(id).get()
        talentMarketItem = models.result_talent_market_item.ResultTalentMarketItem.fromData(result.to_dict(),id)
        return talentMarketItem
    def getAll(self):
        docs = self._db.collection(self.collection).stream()
        result = [models.result_talent_market_item.ResultTalentMarketItem.fromData(doc.to_dict(),id=doc.id) for doc in docs]
        return result
    def  updateByItem(self,item:models.result_talent_market_item.ResultTalentMarketItem):
        self._db.collection(self.collection).document(item.id).update(item.toMap())
        return item
    def createItem(self,item : models.result_talent_market_item.ResultTalentMarketItem):
        item.createAt = str(datetime.now())
        item.millisecondsEpoch = datetime_in_ms()
        result = self._db.collection(self.collection).add(item.toMap())
        item.id = result[1].id
        return item


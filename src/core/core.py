from features.firebase import db
import src.external as externals
import src.domain.usecases as usecases
import src.infra.repositories as repositories
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Core(object, metaclass=Singleton):
    
    def __init__(self,**kwargs):
        # stretch user profile
        self._firebase_datasource_user_profile = externals.FirebaseDataSourceUserProfile(db)
        self._user_profile_repository = repositories.UserProfileRepositoryImpl(self._firebase_datasource_user_profile)
        self.user_profile_usecases = usecases.GetUserProfileImpl(self._user_profile_repository)
        # stretch design wall
        self._firebase_datasource_design_wall = externals.FirebaseDataSourceDesignWall(db)
        self._design_wall_repository = repositories.DesignWallRepositoryImpl(self._firebase_datasource_design_wall)
        self.design_wall_usecases = usecases.DesignWallImpl(self._design_wall_repository)
        # stretch de talent market
        self._firebase_datasource_talent_market = externals.FirebaseDataSourceTalentMarket(db)
        self._talent_market_repository = repositories.talent_market_repository.TalentMarketRepositoryImpl(self._firebase_datasource_talent_market)
        self.talent_market_usecases = usecases.talent_market.TalentMarketImpl(self._talent_market_repository)       

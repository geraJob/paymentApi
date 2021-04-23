from resources.transactions_resource import *
from resources.user_profile_resource import UserProfileResource
from resources.design_wall_resource import *
from resources.talent_market_resource import *
def routes(api):
    api.add_resource(Transactions,'/transaction')
    api.add_resource(Refund,'/refund/<string:id>')
    api.add_resource(Plan,'/plan')
    api.add_resource(Subscription,'/plan/subscription')
    api.add_resource(SubscriptionById,'/plan/subscription/<string:id>')
    api.add_resource(SubscriptionCancel,'/plan/subscription/<string:id>/cancel')
    api.add_resource(SubscriptionAllTransactionsById,'/plan/subscription/<string:id>/transactions')
    api.add_resource(Cards,'/card')
    api.add_resource(CardById,'/card/<string:id>')
    api.add_resource(UserProfileResource,'/user/<string:id>')
    api.add_resource(Recipient,'/recipients')
    api.add_resource(RecipientById,'/recipients/<string:id>')
    api.add_resource(BalanceByRecipient,'/recipients/<string:id>/balance')
    api.add_resource(BalanceByRecipientOperation,'/recipients/<string:id>/balance/operations')
    api.add_resource(BalanceByRecipientOperationById,'/recipients/<string:recipient_id>/balance/operations/<string:operation_id>')
    api.add_resource(DesignWallResource,'/designwall')
    api.add_resource(DesignWallById,'/designwall/<string:id>')
    api.add_resource(TalentMarket,'/talentmarket')
    api.add_resource(TalentMarketById,'/talentmarket/<string:id>')
    

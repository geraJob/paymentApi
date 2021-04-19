from resources.transactions import Transactions,Refund,Plan,Subscription,SubscriptionById,SubscriptionAllTransactionsById,Cards,CardById,SubscriptionCancel

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

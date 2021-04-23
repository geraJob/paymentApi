from src.domain.entities.talent_market_item import TalentMarketItem
class ResultTalentMarketItem(TalentMarketItem):
    def __init__(self,
    id = "",
    serviceDefinition = "",
    budgetMin = 0.0,
    budgetMax = 0.0,
    deadline = "",
    title ="",
    category = "",
    subCategory = "",
    projectSize = "",
    availability = "",
    uidDesignated = "",
    proposal = 18,
    createAt = "",
    tags = "",
    millisecondsEpoch = 0,
    **kwargs):
        super().__init__(
        id = "",
        serviceDefinition = "",
        budgetMin = 0.0,
        budgetMax = 0.0,
        deadline = "",
        title ="",
        category = "",
        subCategory = "",
        projectSize = "",
        uidDesignated="",
        availability = "",
        proposal = 18,
        createAt = "",
        tags = "",
        millisecondsEpoch = 0,
        **kwargs)
        self.id = id
        self.serviceDefinition = serviceDefinition
        self.budgetMin = budgetMin
        self.budgetMax = budgetMax
        self.deadline = deadline
        self.title = title
        self.category = category
        self.createAt = createAt
        self.proposal = proposal
        self.uidDesignated = uidDesignated
        self.subCategory = subCategory
        self.projectSize = projectSize
        self.availability = availability
        self.tags = tags
        self.millisecondsEpoch = millisecondsEpoch
    @classmethod
    def fromData(cls,data,id=''):
        if data == None :
            data={}
        return ResultTalentMarketItem(
            id=id,
            serviceDefinition=data['serviceDefinition'] if 'serviceDefinition' in data else '',
            budgetMin=data['budgetMin'] if 'budgetMin' in data else 0.0,
            budgetMax=data['budgetMax'] if 'budgetMax' in data else 0.0,
            deadline=data['deadline'] if 'deadline' in data else '',
            title=data['title'] if 'title' in data else '',
            category=data['category'] if 'category' in data else '',
            createAt=data['createAt'] if 'createAt' in data else '',
            uidDesignated=data['uidDesignated'] if 'uidDesignated' in data else "",
            proposal=data['proposal'] if 'proposal' in data else '',
            subCategory=data['subCategory'] if 'subCategory' in data else '',
            projectSize=data['projectSize'] if 'projectSize' in data else '',
            availability=data['availability'] if 'availability' in data else '',
            tags=data['tags'] if 'tags' in data else '',
            millisecondsEpoch = data['milisecondsEpoch'] if 'milisecondsEpoch' in data else '',
        )
    
    def toMap(self):
        return {
            'serviceDefinition':self.serviceDefinition,
            'budgetMin':self.budgetMin,
            'budgetMax':self.budgetMax,
            'deadline':self.deadline,
            'title':self.title,
            'category':self.category,
            'createAt':self.createAt,
            'proposal':self.proposal,
            'subCategory':self.subCategory,
            'projectSize':self.projectSize,
            'availability':self.availability,
            'tags':self.tags,
            'millisecondsEpoch':self.millisecondsEpoch
        }
    
    def toMapWithId(self):
        map = self.toMap()
        map['id'] = self.id
        return map
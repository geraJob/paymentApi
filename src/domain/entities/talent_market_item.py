class TalentMarketItem:
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
    proposal = 18,
    createAt = "",
    tags = [],
    millisecondsEpoch = 0,
    **kwargs):
        self.id = id
        self.serviceDefinition = serviceDefinition
        self.budgetMin = budgetMin
        self.budgetMax = budgetMax
        self.deadline = deadline
        self.title = title
        self.category = category
        self.createAt = createAt
        self.proposal = proposal
        self.subCategory = subCategory
        self.projectSize = projectSize
        self.availability = availability
        self.tags = tags
        self.millisecondsEpoch = millisecondsEpoch
    

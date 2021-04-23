class ItemDesignWall:
    def __init__(self,
    id = "",
    serviceDefinition = "",
    budget = 0.0,
    deadline = "",
    title ="",
    category = "",
    subCategory = "",
    projectSize = "",
    availability = "",
    uidDesignated = "",
    createAt = "",
    tags = "",
    millisecondsEpoch = 0,
    **kwargs):
        self.id = id
        self.serviceDefinition = serviceDefinition
        self.budget = budget
        self.deadline = deadline
        self.title = title
        self.category = category
        self.createAt = createAt
        self.uidDesignated = uidDesignated
        self.subCategory = subCategory
        self.projectSize = projectSize
        self.availability = availability
        self.tags = tags
        self.millisecondsEpoch = millisecondsEpoch
    

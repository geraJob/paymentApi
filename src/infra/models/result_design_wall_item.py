from src.domain.entities.design_wall_item import ItemDesignWall
class ResultItemDesignWall(ItemDesignWall):
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
        super().__init__(id = "",
    serviceDefinition = "",
    budget = 0.0,
    deadline = "",
    title ="",
    category = "",
    uidDesignated="",
    subCategory = "",
    createAt = "",
    projectSize = "",
    availability = "",
    tags = "",
    millisecondsEpoch = 0,**kwargs)
        self.id = id
        self.serviceDefinition = serviceDefinition
        self.budget = budget
        self.deadline = deadline
        self.title = title
        self.category = category
        self.subCategory = subCategory
        self.uidDesignated = uidDesignated
        self.createAt = createAt
        self.projectSize = projectSize
        self.availability = availability
        self.tags = tags
        self.millisecondsEpoch = millisecondsEpoch

    @classmethod
    def fromData(cls,data,id =""):
        if data == None :
            data={}
        return ResultItemDesignWall(
            id = id,
            serviceDefinition = data['serviceDefinition'] if 'serviceDefinition' in data else "",
            budget = data['budget'] if 'budget' in data else 0.0,
            deadline = data['deadline'] if 'deadline' in data else "",
            title = data['title'] if 'title' in data else "",
            category = data['category'] if 'category' in data else "",
            createAt=data['createAt'] if 'createAt' in data else "",
            subCategory = data['subCategory'] if 'subCategory' in data else "",
            uidDesignated=data['uidDesignated'] if 'uidDesignated' in data else "",
            projectSize = data['projectSize'] if 'projectSize' in data else "",
            availability = data['availability'] if 'availability' in data else "",
            tags = data['tags'] if 'tags' in data else "",
            millisecondsEpoch = data['millisecondsEpoch'] if 'millisecondsEpoch' in data else "",
        )

    def toMap(self):
        return {
            'serviceDefinition':self.serviceDefinition,
            'budget':self.budget,
            'deadline':self.deadline,
            'title':self.title,
            'category':self.category,
            'subCategory':self.subCategory,
            'projectSize':self.projectSize,
            'uidDesignated':self.uidDesignated,
            'createAt':self.createAt,
            'availability':self.availability,
            'tags':self.tags,
            'millisecondsEpoch':self.millisecondsEpoch
        }
    def toMapWithId(self):
        map = self.toMap()
        map['id'] = self.id
        return map   
    

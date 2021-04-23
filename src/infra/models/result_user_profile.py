from src.domain.entities.user_profile import UserProfile

class ResultUserProfile(UserProfile):
    def __init__(self,
    id = "",
    name = "",
    lastName = "",
    phone = "",
    documentType = "",
    numberDocument = "",
    birthday = "",
    email = "",
    country = "",
    street = "",
    recipientId = "",
    business ="",
    priceByHour = 0.0,
    description = "",
    subCategory = "",
    category ="",
    plan = "",
    subscription = "",
    city = "",
    work = {},
    createAt= "",
    title = "",
    education = [],
    photo = "",
    millisecondsEpochCreateAt = 0,
    neighborhood = "",
    streetnumber = "",
    zipcode ="",
    **kwargs):
        super().__init__(id = "",
    name = "",
    lastName = "",
    phone = "",
    documentType = "",
    numberDocument = "",
    priceByHour = 0.0,
    subCategory = "",
    category ="",
    description = "",
    title = "",
    education = [],
    work = {},
    birthday = "",
    recipientId= "", 
    millisecondsEpochCreateAt = 0,
    email = "",
    subscription = "",
    country = "",
    createAt= "",
    photo = "",
    plan = "",
    business ="",
    street = "",
    city = "",
    neighborhood = "",
    streetnumber = 0,
    zipcode ="",**kwargs)        
        self.id : str = id
        self.name : str = name
        self.photo = photo
        self.lastName: str = lastName
        self.phone: str = phone
        self.description = description
        self.documentType: str = documentType
        self.numberDocument: str = numberDocument
        self.title = title
        self.education = education
        self.birthday : str = birthday
        self.priceByHour = priceByHour
        self.category = category
        self.work = work
        self.subCategory = subCategory
        self.createAt = createAt
        self.millisecondsEpochCreateAt = millisecondsEpochCreateAt
        self.email : str = email
        self.plan = plan
        self.recipientId = recipientId
        self.subscription = subscription
        self.business = business
        self.country : str = country
        self.street : str = street
        self.city : str = city
        self.neighborhood : str = neighborhood
        self.streetnumber : int = streetnumber
        self.zipcode : int  = zipcode

    @classmethod
    def from_to_dict(cls, data, id):
        if data == None :
            data = {}

        return ResultUserProfile(
    id = id,
    name = data['name'],
    lastName = data['lastName'] if 'lastName' in data else "",
    phone =data['phone'] if 'phone' in data else "",
    documentType = data['documentType'] if 'documentType' in data else "",
    numberDocument =data['numberDocument'] if 'numberDocument' in data else "",
    birthday = data['birthday'] if 'birthday' in data else "",
    email = data['email'] if 'email' in data else "",
    business = data['business'] if 'business' in data else "",
    description=data['description'] if 'description' in data else '',
    country =  data['country'] if 'country' in data else "",
    street = data['street'] if 'street' in data else "",
    recipientId=data['recipientId'] if 'recipientId' in data else "",
    plan = data['plan'] if 'plan' in data else "",
    photo = data['photo'] if 'photo' in data else "",
    work=data['work'] if 'work' in data else {},
    millisecondsEpochCreateAt= data['millisecondsEpochCreateAt'] if 'millisecondsEpochCreateAt' in data else "",
    createAt= data['createAt'] if 'createAt' in data else "",
    subscription = data['subscription'] if 'subscription' in data else "",
    city = data['city'] if 'city' in data else "",
    priceByHour = data['priceByHour'] if 'priceByHour' in data else 0.0,
    subCategory =  data['subCategory'] if 'subCategory' in data else '',
    category = data['category'] if 'category' in data else '',
    title =  data['title'] if 'title' in data else '',
    education =  data['priceById'] if 'priceById' in data else [],
    neighborhood = data['neighborhood'] if 'neighborhood' in data else "",
    streetnumber = data['streetnumber'] if 'streetnumber' in data else 0,
    zipcode =data['zipcode'] if 'zipcode' in data else "" 
        )

    def toMap(self):
        return {
           
            'name':self.name,
            'lastName':self.lastName,
            'phone':self.phone,
            'documentType':self.documentType,
            'numberDocument':self.numberDocument,
            'birthday':self.birthday,
            'photo':self.photo,
            'email':self.email,
            'country':self.country, 
            'business':self.business,
            'title':self.title,
            'work':self.work,
            'subCategory':self.subCategory,
            'category':self.category,
            'priceByHour':self.priceByHour,
            'description':self.description,
            'street':self.street,
            'recipientId':self.recipientId,
            'createAt':self.createAt,
            'streetnumber':self.streetnumber,
            'millisecondsEpochCreateAt':self.millisecondsEpochCreateAt,
            'zipcode':self.zipcode,
            'plan':self.plan,
            'education':self.education,
            'subscription':self.subscription
        }



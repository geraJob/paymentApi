import unittest
class UserProfile:
    def __init__(self,
    id = "",
    name = "",
    lastName = "",
    phone = "",
    documentType = "",
    numberDocument = "",
    priceByHour = 0.0,
    subCategory = "",
    category ="",
    birthday = "",
    description = '',
    business ="",
    email = "",
    subscription = "",
    average = 0.0,
    country = "",
    street = "",
    title = "",
    education = [],
    recipientId = "",
    createAt = "",
    photo = "",
    plan = "",
    work = {},
    city ="",
    state = "",
    neighborhood = "",
    streetnumber = "",
    millisecondsEpochCreateAt = 0,
    zipcode = "",
    **kwargs):
        self.id : str = id
        self.name : str = name
        self.photo = photo
        self.average = average
        self.title = title
        self.state = state
        self.lastName: str = lastName
        self.priceByHour = priceByHour
        self.subCategory = subCategory
        self.education = education
        self.work = work
        self.description = description
        self.subCategory = category
        self.phone: str = phone
        self.business : str = business
        self.createAt = createAt
        self.millisecondsEpochCreateAt = millisecondsEpochCreateAt
        self.recipientId = recipientId
        self.documentType: str = documentType
        self.numberDocument: str = numberDocument
        self.birthday : str = birthday
        self.subscription = subscription
        self.email : str = email
        self.plan : str = plan
        self.country : str = country
        self.street : str = street
        self.city : str = city
        self.neighborhood : str = neighborhood
        self.streetnumber : int = streetnumber
        self.zipcode : int  = zipcode





import unittest
class UserProfile:
    def __init__(self,
    id = "",
    name = "",
    lastName = "",
    phone = "",
    documentType = "",
    numberDocument = "",
    birthday = "",
    business ="",
    email = "",
    subscription = "",
    country = "",
    street = "",
    recipientId = "",
    createAt = "",
    photo = "",
    plan = "",
    city ="",
    neighborhood = "",
    streetnumber = "",
    zipcode = "",
    **kwargs):
        self.id : str = id
        self.name : str = name
        self.photo = photo
        self.lastName: str = lastName
        self.phone: str = phone
        self.business : str = business
        self.createAt = createAt
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





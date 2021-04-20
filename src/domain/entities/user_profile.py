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
    email = "",
    country = "",
    street = "",
    city ="",
    neighborhood = "",
    streetnumber = "",
    zipcode = "",
    **kwargs):
        self.id : str = id
        self.name : str = name
        self.lastName: str = lastName
        self.phone: str = phone
        self.documentType: str = documentType
        self.numberDocument: str = numberDocument
        self.birthday : str = birthday
        self.email : str = email
        self.country : str = country
        self.street : str = street
        self.city : str = city
        self.neighborhood : str = neighborhood
        self.streetnumber : int = streetnumber
        self.zipcode : int  = zipcode





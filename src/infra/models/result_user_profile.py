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
    city = "",
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
    birthday = "",
    email = "",
    country = "",
    street = "",
    city = "",
    neighborhood = "",
    streetnumber = 0,
    zipcode ="",**kwargs)        
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

    @classmethod
    def from_to_dict(cls, data, id):
        return ResultUserProfile(
    id = id,
    name = data['name'],
    lastName = data['lastName'] if 'lastName' in data else "",
    phone =data['phone'] if 'phone' in data else "",
    documentType = data['documentType'] if 'documentType' in data else "",
    numberDocument =data['numberDocument'] if 'numberDocument' in data else "",
    birthday = data['birthday'] if 'birthday' in data else "",
    email = data['email'] if 'email' in data else "",
    country =  data['country'] if 'country' in data else "",
    street = data['street'] if 'street' in data else "",
    city = data['city'] if 'city' in data else "",
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
            'email':self.email,
            'country':self.country,
            'street':self.street,
            'streetnumber':self.streetnumber,
            'zipcode':self.zipcode
        }



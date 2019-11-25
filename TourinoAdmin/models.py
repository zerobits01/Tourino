from django.db import models
from django.core.signing import Signer
# Create your models here.


class TourinoAdmin(models.Model):
    Roles = [
        ('A', "Admin"),      # admin can do everything
        ('T', "TourLeader"),  # just making Tours
        ('S', "Seller"),     # publishing new products
        ('B', "Blogger")     # publishing new articles about lorestan and rimale
    ]
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    username = models.CharField(max_length=15, unique=True)
    password = models.TextField()
    role = models.CharField(max_length=1, choices=Roles)

    def toDict(self):
        '''
            gets no input args
            this returns dictionary(email,phone,username(unique),role)
        '''
        data = {
            'email': self.email,
            'phone': self.phone,
            'username': self.username,
            'role': self.role
        }
        return data

    # @classmethod
    # def register(cls, jsondata):
        '''
            gets json data should contains
                {
                    email,
                    password,
                    role from choices('A','B','S','T')admin,blogger,seller,tourleader
                }
            returns dictionary of added admin in database(email,phone,username(unique),role)
        '''
    #     data = jsondata.decode('utf-8')
    #     data = json.loads(data)
    #     admin = cls(email=data['email'],
    #                 password=signer.sign(['password']),
    #                 username=data['email'],
    #                 role=data['role'],
    #                 phone=data['phone']
    #                 )
    #     return admin.toDict()

    def signIn(self, candidate):
        '''
            input argument : candidate password to check
            returns Boolean if the hashed password is equal or not
        '''
        # userpwd = signer.unsign(self.password)
        if self.password != candidate:
            return False
        return True
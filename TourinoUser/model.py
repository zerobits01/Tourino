from django.db import models
import json
from Tourino.helpers import Hasher

class TourinoUser(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    username = models.CharField(max_length=15,unique=True)
    password = models.TextField()
    news = models.BooleanField(default=False)

    def toDict(self):
        '''
            returns dictionary for jsonresponse
                contains: email phone username
        '''
        data = {
            'email': self.email,
            'phone': self.phone,
            'username': self.username,
        }
        return data

    @classmethod
    def register(cls, jsondata):
        '''
            jsondata input arg: 
                email, password, username(unique), phone, news(boolean)
            returns dictionary for jsonresponse
        '''
        data = jsondata.decode('utf-8')
        data = json.loads(data)
        user = cls(
            email=data['email'],
            password=Hasher.makeHash(data['password']),
            username=data['username'],
            phone=data['phone'],
            news= bool(data['news'])
        )
        user.save()
        wallet = Wallet.newWallet(user)
        return user.toDict()

    def signIn(self, candidate):
        '''
            returns Boolean that if the user can
            login with candidate password
        '''
        return Hasher.checkHash(self.password,candidate)
    

    @staticmethod
    def findById(jsondata):
        ''' 
            returns a user json profile 
            arg jsondata : contains int(id)
            returns user info
        '''
        data = json.loads(jsondata.decode('utf-8'))
        id = int(data['id'])
        user = TourinoUser.objects.get(pk=int(id))

    @staticmethod
    def findByUsername(username):
        ''' 
            returns a user json profile 
            arg jsondata : contains username
            returns user info
        '''
        user = TourinoUser.objects.get(username=username)
        return user

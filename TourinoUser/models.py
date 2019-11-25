from django.db import models
from TourinoAdmin.models import Product,Tour,Post
# Create your models here.
def payment(jsondata):
    '''
        after adding payment we handlethis part
        but just returns True
    '''
    return True

def myCartDict(jsondata) :
    '''        
        input arg example : 
            jsondata : {products : [id1,..], tours : [id1,..]}
                the inner parts should be array of integer
        returns json data all products name and price and sum
    '''
    data = jsondata.decode('utf-8')
    data = json.loads(data)
    products = Product.objects.filter(pk__in=data['products']).values('id' , 'name' , 'price')
    sum = Product.objects.filter(pk__in=data['products']).aggregate(Sum('price'))
    tours = Tour.objects.filter(pk__in=data['tours']).values('id' , 'name' , 'price')
    sum1 = Tour.objects.filter(pk__in=data['tours']).aggregate(Sum('price'))
    sum = sum + sum1 
    ans = {
        'sum' : sum,
        'products' : products,
        'tours' : tours
    }
    return ans

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
            password=signer.sign(['password']),
            username=data['email'],
            phone=data['phone'],
            news= bool(data['news'])
        )
        wallet = Wallet.newWallet(user)
        return user.toDict()

    def signIn(self, candidate):
        # userpwd = signer.unsign(self.password)
        # TODO : checking with signer later
        if self.password != candidate:
            return False
        return True

    @staticmethod
    def findById(jsondata):
        ''' 
            returns a user json profile 
            arg jsondata : contains int(id)
            returns user info
        '''
        data = jsondata.decode('utf-8')
        id = int(data['id'])
        user = User.objects.get(pk=int(id))

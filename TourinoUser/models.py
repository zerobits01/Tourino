from django.db import models
import json
from Tourino.helpers import Hasher
from TourinoAdmin.models import Product,Tour,Post
from .model import TourinoUser

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


class TourComment(models.Model):
    rate = models.DecimalField(max_digits=2, decimal_places=1)
    comment = models.TextField()
    user = models.ForeignKey(TourinoUser, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

    
    def toDict(self):
        data = {
            'rate': self.rate,
            'comment': self.comment,
            'username': self.user.username,
            'tour' : self.tour.id
        }
        return data

    @classmethod
    def newComment(cls, jsondata):
        data = jsondata.decode('utf-8')
        data = json.loads(data)
        tour = Tour.objects.get(pk=int(data['tourid']))
        user = TourinoUser.objects.get(pk=int(data['userid']));
        tourcomment = user.tourcomment_set.create(
            rate =  float(data['rate']),
            comment= data['comment'],
            tour= tour
        )
        return tourcomment.toDict()
 
class ProductComment(models.Model):
    rate = models.DecimalField(max_digits=2, decimal_places=1)
    comment = models.TextField()
    user = models.ForeignKey(TourinoUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def toDict(self):
        data = {
            'rate': self.rate,
            'comment': self.comment,
            'username': self.user.username,
            'product' : self.product.id
        }
        return data

    @classmethod
    def newComment(cls, jsondata):
        '''
            rate= float(),
            comment,
            product,
            user
        '''
        data = jsondata.decode('utf-8')
        data = json.loads(data)
        product = Product.objects.get(pk=int(data['productid']))
        user = TourinoUser.objects.get(pk=int(data['userid']))
        productcomment = cls(
            rate= float(data['rate']),
            comment= data['comment'],
            product= product,
            user=user
        )
        return productcomment.toDict()


# for after adding payment options to it.
class Wallet(models.Model):
    user = models.OneToOneField(TourinoUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='ProductSell', blank=True, null=True)
    tours = models.ManyToManyField(Tour, through='TourSell', blank=True, null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=9,blank=True, null=True)

    @classmethod
    def newWallet(cls,user):
        # exactly with user register
        wallet = cls(user=user)
        return wallet
        
    def addToWallet(self):
        # products bought before
        pass

    def toJson(self):
            # TODO : json stringified dictionary
        pass


class ProductSell(models.Model):
    wallet = models.ForeignKey(Wallet , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    date = models.DateField()

    def toJson(self):
            # TODO : json stringified dictionary
        pass
    
    @classmethod
    def newProductSell(cls,jsondata):
        # TODO : creating ProductSell from json data
        # sample : book = Book.create("Pride and Prejudice")
        pass


class TourSell(models.Model):
    wallet = models.ForeignKey(Wallet , on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour , on_delete=models.CASCADE)
    date = models.DateField()

    def toJson(self):
            # TODO : json stringified dictionary
        pass
    
    @classmethod
    def newTourSell(cls,jsondata):
        # TODO : creating new TourSell from json data
        pass

# in next versions working on popular and saving all users data

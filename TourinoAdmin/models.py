from django.db import models
from django.core.signing import Signer
import json
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
        # TODO : checking with signer after test
        if self.password != candidate:
            return False
        return True

class Product(models.Model):
    Types = [
        ('C', "Craft"),
        ('A', "Agricultural"),
        ('F', "Fruit")
    ]
    ptype = models.CharField(max_length=1, choices=Types, default='S')
    name = models.CharField(max_length=55, unique=True)
    price = models.DecimalField(max_digits=20, decimal_places=7)
    image_url = models.TextField(blank=True)
    description = models.TextField()
    count = models.IntegerField(default=0)
    user = models.ForeignKey(TourinoAdmin, on_delete=models.CASCADE)

    def toDict(self):
        '''
            returns {
                    type, # returns ('C', "Craft"),
                                    ('A', "Agricultural"),
                                    ('F', "Fruit")
                    name
                    price
                    image_url(from cloudinary)
                    description about the product
                    count in store
                }
        '''
        data = {
            'type': self.type,
            'name': self.name,
            'price': self.price,
            'image_url': self.image_url,
            'description': self.description,
            'count': self.count
        }
        return data

    @classmethod
    def newProduct(cls, jsondata,id):
        '''
            creates a new product
            input arg :
                jsondata({
                    type,
                        ('C', "Craft"),('A', "Agricultural"), ('F', "Fruit")
                    name,
                    price=float,
                    description,
                    image_url=link,
                    count=int
                }) 
                id,"getting from user json token"
            returns : the dictionary of product
        '''
        data = json.loads(jsondata.decode('utf-8'))
        product = TourinoAdmin.objects.get(pk=id).product_set.create(
            type=data['ptype'],
            name=data['name'],
            price=float(data['price']),
            description=data['description'],
            image_url=data['image_url'],
            count=int(data['count'])
        )
        return product.toDict()

    @staticmethod
    def getLast10():
        '''
            returns an array of 10 last added
            products
        '''
        products = Product.objects.order_by('id').values('id', 'name',
                                                         'image_url', 'ptype', 'price', 'count')
        return products

    @staticmethod
    def getAll():
        ''' 
            returns all products sort by date
        '''
        products = Product.objects.order_by('id').values('id', 'name',
                                                         'image_url', 'ptype', 'price', 'count')
        return products

    @staticmethod
    def getById(id):
        '''
            input arg : 
                id : int identification of product
            returns the product dictionary
        '''
        product = Product.objects.get(pk=int(id))
        # TODO : maybe i need to find the comments and add them
        return product.toDict()

    @staticmethod
    def updateProduct(self, jsondata):
        '''
            input args : 
                jsondata({
                    id, id of product
                    and others are optional
                    ptype,name,image_url,description,
                    count(int),price(float)
                })
        '''
        body = json.loads(jsondata.decode('utf-8'))
        id = body['id']
        data = Product.objects.get(pk=int(id))
        if body['ptype']:
            data.ptype = body['ptype']
        if body['name']:
            data.name = body['name']
        if body['price']:
            data.price = float(body['price'])
        if body['image_url']:
            data.image_url = body['image_url']
        if body['description']:
            data.description = body['description']
        if body['count']:
            data.count = int(body['count'])
        data.save()
        return data.toDict()

class Tour(models.Model):
    # Types = (
    #     'E' : "Experiment",
    #     'G' : "Grand"
    # ) in next version
    name = models.CharField(max_length=55, unique=True)
    price = models.DecimalField(max_digits=20, decimal_places=7)
    # can saving js maps in this part
    description = models.TextField()
    location = models.TextField(blank=True)
    duration = models.IntegerField()     # how many days?
    start = models.DateField()
    end = models.DateField()
    image_url = models.TextField(blank=True)
    online = models.BooleanField(default=False)
    user = models.ForeignKey(TourinoAdmin, on_delete=models.CASCADE)

    def toDict(self):
        '''
            returns just dictionary of data
            to return as jsonresponse in the app
        '''
        data = {
            'name': self.name,
            'price': self.price,
            'length': self.length,
            'end': self.end,
            'start': self.start,
            'location': self.location,
            'online': self.online,
            'image_url': self.image_url,
            'description': self.description
        }
        return data

    @classmethod
    def newTour(cls, jsondata,id):
        '''
            input args : jsondata, int(id) -> user id
                jsondata : {
                    name , price(float)
                    duration(int), start(int) , end(int)
                    online(boolean), image_url,description
                }
            returns : dictionary of tour created and saved
        '''
        data = jsondata.decode('utf-8')
        data = json.loads(data)
        user = TourinoAdmin.objects.get(pk=int(data['id']))
        tour = cls(name=data['name'],
                   price=float(data['price']),
                   duration=int(data['duration']),
                   end=data['end'],
                   start=data['start'],
                   location=data['location'],
                   online=bool(data['online']),
                   image_url=data['image_url'],
                   description=data['description'],
                   user=user
                   )
        return tour.toDict()

    @staticmethod
    def getLast10():
        '''
            returns array of last 10 added tours
            with properties :
                'id', 'name','image_url', 'price', 'online'
        '''
        tours = Tour.objects.order_by('id').values('id', 'name',
                                                   'image_url', 'price', 'online')
        return tours

    @staticmethod
    def getAll():
        '''
            returns array of all added tours
            with properties :
                'id', 'name','image_url', 'price', 'online'
        '''
        tours = Tour.objects.order_by('id').values('id', 'name',
                                                   'image_url', 'price', 'online')
        return tours

    @staticmethod
    def getById(id):
        '''
            input arg : id(int) -> tourid
            returns the dictionary of tour with asked id
        '''
        data = Tour.objects.get(pk=int(id))
        # TODO : maybe i need to find the comments and add them
        return data.toDict()

    @staticmethod
    def updateTour(self, jsondata):
        body = json.loads(jsondata.decode('utf-8'))
        id = body['id']
        data = Tour.objects.get(pk=int(id))
        if body['ptype']:
            data.ptype = body['ptype']
        if body['name']:
            data.name = body['name']
        if body['online']:
            data.price = bool(body['online'])
        if body['image_url']:
            data.image_url = body['image_url']
        if body['description']:
            data.description = body['description']
        if body['count']:
            data.count = int(body['count'])
        if body['start']:
            data.start = body['start']
        if body['end']:
            data.end = body['end']
        if body['duration']:
            data.duration = int(body['duration'])
        if body['location']:
            data.location = body['location']
        data.save()
        return data.toDict()

class Post(models.Model):
    user = models.OneToOneField(TourinoAdmin, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    text = models.TextField()
    image_url = models.TextField(blank=True)

    def toDict(self):
        '''
            returns a dictionray as input of jsonresponse
                for get methods
        '''
        data = {
            'user': self.user__username,
            'name': self.name,
            'text': self.text,
            'image_url': self.image_url
        }
        return data

    @classmethod
    def newPost(cls, jsondata,id):
        '''
            input arg : 
                json data{
                    name,
                    text,
                    image_url
                }
                id(int) -> admin
                returns : dict for json response
        '''
        data = jsondata.decode('utf-8')
        data = json.loads(data)
        user = TourinoAdmin.objects.get(pk=int(id))
        post = user.post_set.create(
            name=data['name'],
            text=data['text'],
            image_url=data['image_url']
        )
        # TODO : mail_post(sender=cls.__class__, post=post)
        return post.toDict()

    @staticmethod
    def getLast10():
        ''' 
            return array of sorted last 10
        '''
        posts = Post.objects.order_by('id').values(
            'title', 'image_url').order_by('id') 
        # TODO : handling last 10 objects
        return posts

    @staticmethod
    def getAll():
        posts = Post.objects.order_by('id').values('title', 'image_url')
        return posts

    @staticmethod
    def getById(id):
        data = Post.objects.get(pk=int(id))
        # TODO : maybe i need to find the comments and add them
        return data.toDict()

    @staticmethod
    def updatePost(self, jsondata):
        body = json.loads(jsondata.decode('utf-8'))
        id = body['id']
        data = Post.objects.get(pk=int(id))
        if body['title']:
            data.title = body['title']
        if body['text']:
            data.text = body['text']
        if body['image_url']:
            data.image_url = body['image_url']

        data.save()
        return data.toDict()

def search(jsondata):
    '''
        input arg :
            jsondata : a list of words
        returns : 
            all products contain one of the words in jsondata
            in their name as an dictionary of lists(objects)
    '''
    data = jsondata.decode('utf-8')
    data = json.loads(data)
    data = data['search'].split()
    # in a for creating some links with name
    products = {}
    tours = {}
    posts = {}
    for word in data:
        products = products + \
            set(Product.objects.filter(name__icontains=word).values(
                'id', 'name', 'image_url', 'rate'))
        tours = tours + \
            set(Tour.objects.filter(name__icontains=word).values(
                'id', 'name', 'image_url', 'rate'))
        posts = posts + \
            set(Post.objects.filter(name__icontains=word).values(
                'id', 'name', 'image_url', 'rate'))
    ans = {
        'products': products,
        'tours': tours,
        'post': post,
        'basepathp': 'localhost/products',
        'basepatht': 'localhost/tours',  # just add the id at the end
        'basepathp': 'localhost/posts'  # just add the id at the end
    }
    return ans

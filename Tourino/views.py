from TourinoAdmin.models import Product, Tour, search, Post
from django.http import JsonResponse, request

# TODO : adding comments and rates to return that

def homePage(request):
    # TODO Next : pagination with url get
    if request.method == 'GET':
        try:
            products = Product.getLast10()
            tours = Tour.getLast10()
            posts = Post.getLast10()
            return JsonResponse({
                'products': products,
                'tours': tours,
                'posts': posts
            })
        except Exception as e:
            return JsonResponse({
                'err': e
            }, status=406)
    else :
        return JsonResponse({
            'error' : 'this is method is not supported'
        },status=406)

def productsHome(request):
    # TODO Next : pagination
    if request.method == 'GET':
        try:
            products = Product.getAll()
            return JsonResponse({
                'products' : products
            })        
        except Exception as e:
            return JsonResponse({
                'err': e
            }, status=406)
    else :
        return JsonResponse({
            'error' : 'this is method is not supported'
        },status=406)

def tourHome(request):
    # TODO Next : pagination
    if request.method == 'GET':
        try:
            tours = Tour.getAll()
            return JsonResponse({
                'tours' : tours
            })
        except Exception as e:
            return JsonResponse({
                'err': e
            }, status=406)
    else :
        return JsonResponse({
            'error' : 'this is method is not supported'
        },status=406)

def postHome(request):
    # TODO Next : pagination
    if request.method == 'GET':
        try:
            posts = Post.getAll()
            return JsonResponse({
                'post': posts
            })
        except Exception as e:
            return JsonResponse({
                'err': e
            }, status=406)
    else :
        return JsonResponse({
            'error' : 'this is method is not supported'
        },status=406)

def searchBar(request):
    if request.method == 'POST':
        try:
            data = search(request.body)
            return JsonResponse({
                'answer' : data
            })
        except Exception as e:
            return JsonResponse({
                'err': e
            }, status=406)
    else :
        return JsonResponse({
            'error' : 'this is method is not supported'
        },status=406)

def getPostById(request, id):
    if request.method == 'GET':
        try:
            post = Post.getById(id)
            return JsonResponse(post)
        except Exception as e:
            return JsonResponse({
                'err': e
            }, status=406)
    else :
        return JsonResponse({
            'error' : 'this is method is not supported'
        },status=406)

def getProductById(request, id):
    if request.method == 'GET':
        try:
            pro = Product.getById(id)
            return JsonResponse(pro)
        except Exception as e:
            return JsonResponse({
                'err': e
            }, status=406)
    else :
        return JsonResponse({
            'error' : 'this is method is not supported'
        },status=406)

def getTourById(request, id):
    if request.method == 'GET':
            try:
                tour = Tour.getById(id)
                return JsonResponse(tour)
            except Exception as e:
                return JsonResponse({
                    'err': e
                }, status=406)
    else :
        return JsonResponse({
            'error' : 'this is method is not supported'
        },status=406)
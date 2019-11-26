from django.shortcuts import render
from django.http import request,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import signing
# Create your views here.


def jwt_auth(old_fuction):
    '''
        decorator for checking access token authentication
        using django signer
    '''
    def new_function(request,*args, **kwargs):
       
        jwt = request.environ['HTTP_USER_JWT'] 
        
        # this is the way of being the best, first i print the dict and then i
        # copied that and structured that then with my knowledge i found how to access it
        
        if jwt is not None:
            loaded = signing.loads(jwt)
            user = M.TourinoUser.objects.get(pk=loaded['id'])
        else:
            return JsonResponse({
                'msg': "access denied"
            }, status=403)
        if user is None:
            return JsonResponse({
                'msg': "access denied"
            }, status=403)
        return old_fuction(request,*args, **kwargs)
    return new_function


@csrf_exempt
def logIn(request):
    if request.method == 'POST':
        try:
            body = json.loads(requestuest.body.decode('utf-8'))
            user = RimaleAdmin.objects.get(pk=int(body['id']))
            flag = user.signIn(body['password'])
            if flag :
                token = signing.dumps({"id": user.id})
                return JsonResponse({
                    'token' : token
                })
        except Exception as e:
            return JsonResponse({
                'error' : e
            },status=406)
    else :
        return JsonResponse({
            'error' : 'this is method is not supported'
        },status=406)

@csrf_exempt
@jwt_auth
def addProduct(request):
    if request.method == 'POST':
        try :
            product = Product.newProduct(request.body)
            return JsonResponse(product)
        except Exception as e:
            return JsonResponse({
                'err' : e
            },status=406)
    else :
        return JsonResponse({
            'error' : 'this is method is not supported'
        },status=406)

@csrf_exempt
@jwt_auth
def updateProduct(request):
    if request.method == 'POST':
        try :
            product = Product.updateProduct(request.body)
            return JsonResponse(product)
        except Exception as e:
            return JsonResponse({
                'err' : e
            },status=406)
    else :
        return JsonResponse({
            'error' : 'this is method is not supported'
        },status=406)

@csrf_exempt
@jwt_auth
def addTour(request):
    if request.method == 'POST':
        try :
            tour = Tour.newTour(request.body)
            return JsonResponse(tour)
        except Exception as e:
            return JsonResponse({
                'err' : e
            },status=406)
    else :
        return JsonResponse({
            'error' : 'this is method is not supported'
        },status=406)

@csrf_exempt
@jwt_auth
def updateTour(request):
    if request.method == 'POST':
        try : 
            tour = Tour.updateTour(request.body)
            return JsonResponse(tour)
        except Exception as e:
            return JsonResponse({
                'err' : e
            },status=406)
    else :
        return JsonResponse({
            'error' : 'this is method is not supported'
        },status=406)

@csrf_exempt
@jwt_auth
def addPost(request):
    if request.method == 'POST':
        try : 
            post = Post.newPost(request.body)
            return JsonResponse(post)
        except Exception as e:
            return JsonResponse({
                'err' : e
            },status=406)
    else :
        return JsonResponse({
            'error' : 'this is method is not supported'
        },status=406)

@csrf_exempt
@jwt_auth
def updatePost(request):
    if request.method == 'POST':
        try : 
            post = Post.updatePost(request.body)
            return JsonResponse(post)
        except Exception as e:
            return JsonResponse({
                'err' : e
            },status=406)
    else :
        return JsonResponse({
            'error' : 'this is method is not supported'
        },status=406)
'''
@jwt_auth
def deletePost(request):
    if request.method == 'POST':
        try:
            id = json.loads(request.body.decode('utf-8'))['id']
            Post.objects.delete(pk=if)
            return JsonResponse({'msg' : 'done!'})
        except Exception as e:
            return JsonResponse({
                'err' : e
            },status=406)
'''
from django.shortcuts import render
from django.core import signing
from . import models as M
import json
from django.http import JsonResponse,request
from django.views.decorators.csrf import csrf_protect,csrf_exempt


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


@csrf_exempt # for csrf escape
def signUp(req):
    if req.method == 'POST':
        try:
            data = M.TourinoUser.register(req.body)
            return JsonResponse(data)
        except Exception as e:
            return JsonResponse({
                'err' : e
            },status=406)
    else :
        return JsonResponse({
            'error' : 'this is method is not supported'
        },status=406)

@csrf_exempt
def logIn(req):
    if req.method == 'POST':     
        data = json.loads(req.body.decode('utf-8'))
        password = data['password']
        username = data['username']
        user = M.TourinoUser.findByUsername(username)
        try:
            flag = user.signIn(password)
            token = signing.dumps({"id": user.id})
            return JsonResponse({
                'token' : token
            })
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
def comment(req):
    if req.method == 'POST':
        try :
            data = json.loads(req.body.decode('utf-8'))
            typ = data['type']
            if typ == 'P':
                comment = M.ProductComment.newComment(req.body)
            else:
                comment = M.TourComment.newComment(req.body)
            return JsonResponse(comment)
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
def checkCart(req):
    if req.method == 'POST':
        try :
            data = M.myCartDict(req.body)
            return JsonResponse(data)
        except Exception as e:
            return JsonResponse({
                'err' : e
            },status=406)
    else :
        return JsonResponse({
            'error' : 'this is method is not supported'
        },status=406)
        
'''
# after adding real payment
@jwt_auth
def checkWallet(req):
    # everything this user payed before
    pass

# need jwt auth and decorators
@jwt_auth
def payment(req):
    # 
    pass
'''

# TODO : changing hash or encrypt pattern
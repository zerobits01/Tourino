from django.shortcuts import render
from django.core import signing
from . import models as M
import json
from django.http import JsonResponse
from Tourino.helpers import jwt_auth
from django.views.decorators.csrf import csrf_protect,csrf_exempt
# Create your views here.

@csrf_exempt
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
        user = M.TourinoUser.findByUsername(req.body)
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
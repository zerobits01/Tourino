'''
    adding all apps helpers here
'''

from django.core import signing
from django.http import JsonResponse
import json
from TourinoUser.models import TourinoUser

'''
def decorator(arg1, arg2):    
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            print "Congratulations.  You decorated a function that does something with %s and %s" % (arg1, arg2)
            function(*args, **kwargs)
        return wrapper
    return real_decorator
@decorator("arg1", "arg2")
def print_args(*args):
    for arg in args:
    print arg

'''


def jwt_auth(old_fuction):
    def new_function(request, *args, **kwargs):
        if request.headers['user-jwt'] is not None:
            token = request.headers['user-jwt']
            loaded = signing.loads(token)
            user = TourinoUser.objects.get(pk=loaded['id'])
        else:
            return JsonResponse({
                'msg': "access denied"
            }, status=403)
            # request.headers['user-jwt']
            # loaded = signing.loads(token)
            # user = RimaleAdmin.objects.get(pk=loaded['id'])

        if user is None:
            return JsonResponse({
                'msg': "access denied"
            }, status=403)
        old_fuction(request, *args, **kwargs)
    return new_function


# TODO : writing logger

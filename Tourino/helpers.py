'''
    adding all apps helpers here
'''
import hashlib
# from django.apps import apps
# TourinoUser = apps.get_model('TourinoUser', 'TourinoUser')

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



# TODO : writing logger


# hash functions : 


class Hasher:
    @staticmethod 
    def makeHash(string):
        '''
            returns the hash value of string input
        '''
        hashed = hashlib.sha256(string.encode())
        hex_of_hashed = hashed.hexdigest()
        return hex_of_hashed

    @staticmethod
    def checkHash(string, candidate):
        '''
            string : hash value
            candidate : the input to check with hash value
            returns True if equal else False
        '''
        hashed = hashlib.sha256(string.encode())
        hex_of_string = hashed.hexdigest()
        hashed = hashlib.sha256(candidate.encode())
        hex_of_candidate = hashed.hexdigest()
        return hex_of_string == hex_of_string 


print('[+] done')
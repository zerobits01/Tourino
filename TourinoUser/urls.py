from django.urls import path
from . import views


urlpatterns = [
    path('register',views.signUp),
    path('login',views.logIn),
    path('comment',views.comment),
    path('checkcart',views.checkCart),
]

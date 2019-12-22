from django.urls import path
from . import views


urlpatterns = [
    # path('adminhome',views.home)
    # path('login/',views.logIn),
    path('add/product',views.addProduct),
    path('add/post',views.addPost),
    path('add/tour',views.addTour),
    path('update/product',views.updateProduct),
    path('update/post',views.updatePost),
    path('update/tour',views.updateTour),
]

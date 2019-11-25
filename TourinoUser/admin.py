from django.contrib import admin
from .models import TourinoUser,TourComment,ProductComment,Wallet,ProductSell,TourSell
# Register your models here.

admin.site.register(TourinoUser)
admin.site.register(ProductComment)
admin.site.register(TourComment)
admin.site.register(ProductSell)
admin.site.register(TourSell)
admin.site.register(Wallet)


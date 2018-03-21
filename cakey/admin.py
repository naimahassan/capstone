from django.contrib import admin
from . models import Profile,Post,Cake

# Register your models here.
admin.site.register(Post)
admin.site.register(Cake)
admin.site.register(Profile)


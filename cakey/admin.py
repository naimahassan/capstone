from django.contrib import admin
from . models import Profile,Post,Recipe

# Register your models here.
admin.site.register(Post)
admin.site.register(Recipe)
admin.site.register(Profile)


from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length = 90)
    image = models.ImageField(upload_to = 'profile', null = True, blank = True)
    email = models.EmailField(null = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True)

    def __str__(self):
        return str(self.image)

    def create_profile(self):
        self.save

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.remove      

    @classmethod
    def update_profile(self):
        Profile_update = cls.objects.filter(id).all()
        return Profile_update

    @classmethod
    def get_profile(self):
        profile = Profile.objects.all()
        return profile          

class Cake(models.Model):
    name = models.CharField(max_length = 90)
    image = models.ImageField(upload_to = 'cake/', null = True, blank = True)
    caption = models.CharField(max_length = 500)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null = True)

    def __str__(self):
        return str(self.image)

    def create_cake(self):
        self.save

    def delete_cake(self):
        self.delete    

    @classmethod
    def get_cake(self):
        cake = Cake.objects.all()
        return cake
     
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null = True)
    image = models.ImageField(upload_to = 'post/', null = True, blank = True)
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE, null = True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE , null = True)
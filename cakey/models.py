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

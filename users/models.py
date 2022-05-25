from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# cascade = if the user is deleted, the profile is deleted. not vice-versa.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to="profile_pics")

    def __str__(self):
        return f'{self.user.username} Profile'

    #resize image of profile picture
    def save(self, *args, **kwargs):
        #another way is super(Profile, self).save(*args, **kwargs)
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

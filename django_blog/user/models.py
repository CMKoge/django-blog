from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    image = models.ImageField(default='default.jpg', upload_to="prfile_")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} profile'
    
    def save(self):
        super().save()

        img = Image.open(self.image.path) # Get image path
        # Resizing image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
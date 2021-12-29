from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=300)
    image = models.ImageField(blank=True,null=True,upload_to='images',default='download.png')
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



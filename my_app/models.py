from django.db import models

# Create your models here.

class Blog(models.Model):
    title =models.CharField(max_length=100)
    content =models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(blank=True, null=True)
    images = models.ImageField(upload_to='blog_images/',blank=True, null=True)

    def __str__(self):
        return self.title

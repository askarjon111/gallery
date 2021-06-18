from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
      return self.title

    def get_absolute_url(self):
        return reverse('category', args=[str(self.id)])
    


class Image(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='images')
    image = models.ImageField(upload_to="")
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
      return self.title

    def get_absolute_url(self):
        return reverse('image_detail', args=[str(self.id)])
    

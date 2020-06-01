from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    image = models.ImageField(blank='default',null=True)
    caption = models.TextField()
    likes   = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')
    created_date = models.DateField(default=timezone.now)
    saved   = models.BooleanField(default=False) 

    def get_absolute_url(self):
        return reverse('insta:post_detail', kwargs={"id":self.id})

    def __str__(self):
        return self.caption

     
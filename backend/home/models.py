from django.conf import settings
from django.db import models
class Post(models.Model):
    'Generated Model'
    caption = models.CharField(max_length=256,)
    image = models.URLField()
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="post_user",)

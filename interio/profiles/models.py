from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=300)
    sub_title=models.CharField(max_length=250)
    description=models.CharField(max_length=500)
    image=models.ImageField(max_length=500)
    timestamp=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE, null=True)  

    def __str__(self):
        return self.title
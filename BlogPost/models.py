from django.db import models
from BlogUser.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} from {self.owner}"
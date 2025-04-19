from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=500)
    username = models.CharField(max_length=200)
    community = models.ForeignKey("communities.Community", on_delete=models.SET_NULL, null=True, blank=True, related_name="members")
    bio = models.TextField(blank=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
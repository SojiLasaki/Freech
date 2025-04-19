from django.db import models
import uuid
from users.models import Profile
# Create your models here.

class Community(models.Model):
    # creator = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=300, unique=True)
    # members = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Communities"


class Circle(models.Model):
    creator = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    members = models.ManyToManyField("users.Profile", related_name="circles")  #
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Circles"


class Post(models.Model):
    title = models.CharField(max_length=5000, null=True, blank=True)
    body = models.TextChoices
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)

    def __str__(self):
        return self.name
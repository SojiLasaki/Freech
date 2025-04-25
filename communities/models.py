from django.db import models
import uuid
from django.contrib.auth.models import User
from users.models import Profile
# Create your models here.

class Community(models.Model):
    # creator = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=300, unique=True)
    # convo = models.ManyToManyField("Convo")
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
    # convo = models.ManyToManyField("Convo")
    members = models.ManyToManyField("users.Profile", related_name="circles")  #
    # is_public = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Circles"


class Convo(models.Model):
    creator = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, null=True, blank=True)
    circle = models.ForeignKey(Circle, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=5000, null=True, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)

    def __str__(self):
        return str(self.title)
    

class Reply(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    convo = models.ForeignKey("Convo", on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)

    def __str__(self):
        return str(self.profile)
    
    class Meta:
        verbose_name_plural = "Replies"


# class RequestForm(models.Model):

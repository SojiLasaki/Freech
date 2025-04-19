from django.db import models
import uuid
# Create your models here.

class Community(models.Model):
    # creator = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=300, unique=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Communities"
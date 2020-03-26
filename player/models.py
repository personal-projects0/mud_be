from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.
class Player(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, unique=True, editable=False)
    coord = ArrayField(base_field=models.IntegerField(), size=2, default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
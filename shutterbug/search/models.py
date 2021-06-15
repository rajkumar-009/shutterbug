from django.db import models
from home.models import Photographer, Client
import uuid
# Create your models here.


class PhotoshootSession(models.Model):
    session_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    session_date = models.DateField()

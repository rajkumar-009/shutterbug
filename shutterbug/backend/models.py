from django.db import models
import uuid
# Create your models here.


class Photographer(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200)
    dob = models.DateField()
    country_of_origin = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.PositiveIntegerField()
    telephone = models.CharField(max_length=20)
    member_organization = models.CharField(
        max_length=100, blank=True, null=True)
    base_price = models.PositiveIntegerField()


class Client(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200)
    dob = models.DateField()
    country_of_origin = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.PositiveIntegerField()
    telephone = models.CharField(max_length=20)
    member_organization = models.CharField(
        max_length=100, blank=True, null=True)


class PhotoshootSession(models.Model):
    session_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    session_date = models.DateField()

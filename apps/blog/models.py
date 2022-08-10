from django.db import models

# Create your models here.

class Person(models.Model):
    dni = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


class Member(models.Model):
    id_member = models.ForeignKey('Person', on_delete=models.CASCADE)


class Administrator(models.Model):
    id_admin = models.ForeignKey('Person', on_delete=models.CASCADE)
    email = models.EmailField(blank=True)


class Area(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=255)
    id_admin = models.ForeignKey('Administrator', on_delete=models.DO_NOTHING)


class Post(models.Model):
    id_post = models.IntegerField(primary_key=True)
    name_post = models.CharField(max_length=60)
    date = models.DateField()
    section = models.CharField(max_length=60)
    description = models.TextField(max_length=255)
    reactions = models.IntegerField()
    references = models.IntegerField()
    id_area = models.ForeignKey('Area', on_delete=models.DO_NOTHING)
    id_admin = models.ForeignKey('Administrator', on_delete=models.DO_NOTHING)
    


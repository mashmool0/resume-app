from django.db import models

# Create your models here.


class HeaderInfo(models.Model):
    FullName = models.CharField(max_length=30)
    job = models.CharField(max_length=40)
    instagram = models.CharField(max_length=200, null=True)
    facebook = models.CharField(max_length=200, null=True)
    PhoneNumber = models.CharField(max_length=12)
    BirthdayDate = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    BirthdayPlace = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.FullName


class AboutMe(models.Model):
    text = models.TextField()


class WhatToDo(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    img = models.ImageField(upload_to='media', default=True)

    def __str__(self) -> str:
        return self.title


class Comments(models.Model):
    name = models.CharField(max_length=30)
    text = models.TextField(max_length=150)
    profile = models.ImageField(upload_to='media/',default=False)

    def __str__(self) -> str:
        return self.name

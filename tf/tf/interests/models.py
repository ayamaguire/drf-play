from django.db import models


class Interest(models.Model):
    name = models.CharField(max_length=200)


class Friend(models.Model):
    name = models.CharField(max_length=200)
    interest = models.ForeignKey(Interest, on_delete=models.DO_NOTHING)

from django.db import models
class RegModel(models.Model):
    FirstName = models.CharField(max_length=15)
    LastName = models.CharField(max_length=15)
    UserName = models.CharField(max_length=15)
    Password = models.CharField(max_length=15)
    CPassword = models.CharField(max_length=15)
    EmailID = models.EmailField()
    MobileNo = models.IntegerField()
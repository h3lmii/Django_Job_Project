from django.db import models
from django.conf import settings

# Create your models here.


class Job(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,null=True,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=200,null=True)
    position=models.CharField(max_length=200,null=True)
    description=models.CharField(max_length=2000,null=True)
    Location=models.CharField(max_length=2000,null=True)
    salary=models.IntegerField(null=True)

    def __str__(self):
        return self.position


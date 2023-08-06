from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=20)
    loc = models.CharField(max_length=20)
    doj = models.DateField(auto_now_add=True)



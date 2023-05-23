from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=250,blank=True,null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=250, blank=True,null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

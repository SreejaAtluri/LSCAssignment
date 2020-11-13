from django.db import models

# Create your models here.
class Employees(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    firstname = models.CharField(max_length=255, null=False)
    managername = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {} - {}".format(self.id,self.firstname,self.lastname)

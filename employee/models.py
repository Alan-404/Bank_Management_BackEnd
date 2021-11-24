from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.

class EmployeeModel(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    emailWork = models.CharField(max_length=50, unique=True, null=False)
    userId = models.IntegerField()
    class Meta:
        db_table = 'employee'
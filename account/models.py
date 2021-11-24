from django.db import models

# Create your models here.

class AccountModel(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50, unique=True, null = False)
    password = models.TextField(null= False)
    class Meta:
        db_table = 'account'
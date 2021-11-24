from django.db import models
# Create your models here.

class UserModel(models.Model):
    id = models.AutoField(primary_key=True)
    cId = models.CharField(max_length=50, unique=True, null= False)
    firstName = models.CharField(max_length=50, null=False)
    middleName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50, null = False)
    bDate = models.DateField()
    phone = models.CharField(max_length=12, unique=True)
    address = models.TextField()
    avatar = models.TextField()
    email = models.CharField(max_length=100,unique=True)
    role = models.IntegerField()
    class Meta:
        db_table = 'user'
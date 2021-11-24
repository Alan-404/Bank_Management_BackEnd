from django.db import models


# Create your models here.

class BankCardModel(models.Model):
    customerId = models.IntegerField(primary_key=True)
    card = models.CharField(max_length=50)
    class Meta:
        db_table = "bankcard"
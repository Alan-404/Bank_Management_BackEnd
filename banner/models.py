from django.db import models

# Create your models here.


class BannerModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.TextField()
    class Meta:
        db_table = "banner"
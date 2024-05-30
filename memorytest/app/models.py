from django.db import models

# Create your models here.
class Test(models.Model):
    sid=models.IntegerField()
    name=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='images/') 
    def __str__(self):
        return f"{self.name}"
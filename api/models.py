from django.db import models

# Create your models here.


class chat(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    info1 = models.IntegerField(blank=False)
    info2 = models.TextField(blank=False)
    
    
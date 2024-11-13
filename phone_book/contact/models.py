from django.db import models
# from uuid import uuid4
# Create your models here.
class User(models.Model):
    

   
    # id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    id = models.AutoField(primary_key=True) # SERIAL PRIMARY KEY 
    username = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.username
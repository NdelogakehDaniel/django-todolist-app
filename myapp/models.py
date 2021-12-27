from django.db import models

class List(models.Model):
    data = models.CharField(max_length=500)
    done = models.BooleanField(default=False)
    
    class Meta:  
        db_table = "list"  

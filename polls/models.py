from django.db import models
from datetime import datetime
# Create your models here.

class TelChopModel(models.Model):
    model = models.CharField(max_length=25)
    tel_haqida = models.TextField()
    creat_date = models.DateTimeField(default=datetime.now)
    update_date = models.DateTimeField(default=datetime.now)
    del_date = models.DateTimeField(default=datetime.now)
    status = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.model
    
    class Meta:
        db_table = 'Chop'

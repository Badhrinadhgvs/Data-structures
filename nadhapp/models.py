from django.db import models

# Create your models here.
class FAQ(models.Model):
  tit=models.CharField(max_length=100)
  Desc=models.TextField()
  
  
  
  
  def __str__(self):
    return self.tit
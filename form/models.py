from django.db import models

# Create your models here.
class createform(models.Model):
    title=models.CharField(max_length=1234),
    discription=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
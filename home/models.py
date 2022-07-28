from django.db import models

# from home.views import feedback

# Create your models here.
class contact(models.Model):
    fname=models.CharField(max_length=122)
    lname=models.CharField(max_length=122)
    emaill=models.CharField(max_length=122)
    gender=models.CharField(max_length=122)
    contactno=models.CharField(max_length=10)

    def __str__(self):
        return self.fname

class fb(models.Model):
    emaill=models.CharField(max_length=122)
    feedbacki=models.TextField(max_length=400)    
    def __str__(self):
        return self.emaill
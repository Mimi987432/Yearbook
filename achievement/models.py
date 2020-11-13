from django.db import models

class student(models.Model):
    name=models.CharField(max_length=100,blank=False)
    department=models.TextField(max_length=100,blank=False)
    roll=models.TextField(max_length=100,blank=False)
    email=models.TextField(max_length=100,blank=False)
    facebook=models.TextField(max_length=100,blank=False)
    address=models.TextField(max_length=100,blank=False)
    about=models.TextField(max_length=100,blank=False)

    def __str__(self):
        return self.name

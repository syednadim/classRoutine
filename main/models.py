from django.db import models
from django.utils import timezone

class ClassRoom(models.Model):
    classid = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=50,default='')
    

    def __str__(self):
        return self.class_name
    


class Subject(models.Model):
    sub_id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.subject

class Teacher(models.Model):
    teacherid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default='')
    phone = models.CharField(max_length=20,default='')
    location = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.name

    
class ClassRoutine(models.Model):
    routineid =  models.AutoField(primary_key=True)
    ClassRoom = models.CharField(max_length=100,default='')
    start = models.CharField(max_length=100,default='')
    end = models.CharField(max_length=100,default='')
    subject =  models.CharField(max_length=100,default='')
    teacher =  models.CharField(max_length=100,default='')
    created_date = models.DateTimeField(default=timezone.now) 

    
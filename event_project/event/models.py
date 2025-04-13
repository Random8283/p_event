from django.db import models

# Create your models here.
#install pip install pillow for imagefield
#pip3 install django-taggit


class Events(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'images/')
    description = models.TextField()
    campuses = {'W':'Warner Robins',
                'C':"Cochran",
                'D':'Dublin',
                'E':"Eastman",
                'M':"Macon",
                'N/A':"Non Campus"
                }
    campus = models.CharField(max_length=3,choices=campuses) #
    types = {'A':'Academic',
             'S':'Social',
             'C':'Club',
             'V':'Volunteer'}
    type = models.CharField(max_length =1,choices=types)  #
    location = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()

def __str__(self):
    return self.title


from django.db import models

# Create your models here.
class Member(models.Model):
  adminname = models.CharField(max_length=255, blank=False)
  adminstaffnumber = models.CharField(max_length=255, blank=False)
  adminemail = models.EmailField(max_length=255, default='mwajuma@gmail.com', blank=False)
  adminphonenumber = models.CharField(max_length=15, default= +254700000000, blank=False)
  institution = models.CharField(max_length=255, default= 'Technical University of Mombasa', blank=False)
  password = models.CharField(max_length=128, default='password')

  def __str__(self):
        return self.adminstaffnumber

class Student(models.Model):
    admision_number = models.CharField(max_length=255, blank= False)
    full_name = models.CharField(max_length=255, blank= False)
    course_of_study = models.CharField(max_length=255, blank= False)
    duration_of_study = models.CharField(max_length=255, blank= False)
    mode_of_study = models.CharField(max_length=255, blank= False)

    def __str__(self):
        return self.admision_number
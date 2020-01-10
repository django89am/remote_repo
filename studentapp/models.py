from django.db import models
class StudentData(models.Model):
    student_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    course_fee = models.IntegerField()
    institute_name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    location_name = models.CharField(max_length=100)
    def __str__(self):
        return self.student_name
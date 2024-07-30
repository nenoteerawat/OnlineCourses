# courses/models.py
from django.db import models

class Course(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]

    course_code = models.CharField(max_length=10)
    course_name = models.CharField(max_length=100)
    instructor_name = models.CharField(max_length=100)
    num_students = models.IntegerField()
    day_of_week = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.course_name

from django.contrib import admin
from .models import Course

# Register your models here.
# courses/admin.py



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'course_name', 'instructor_name', 'num_students', 'day_of_week', 'start_time', 'end_time')

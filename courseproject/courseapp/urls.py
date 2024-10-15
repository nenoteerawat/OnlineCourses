from django.urls import path
from . import views

urlpatterns = [
    path('cfv/', views.courseFormView, name='course_url'),
    path('scv/', views.showView, name='show_url'),
    path('up/<int:f_oid>', views.updateView, name= 'update_url'),
    path('del/<int:f_oid>', views.deleteView, name= 'delete_url'),
]
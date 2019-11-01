from django.urls import path
from employee import views
from employee.views import *

urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('add/', employee_add, name= "employee_add"),
    path('<int:id>/details/', employee_details, name= "employee_details"),
    path('<int:id>/edit/', employee_edit, name = "employee_edit"),
    path('<int:id>/delete/', employee_delete, name =  "employee_delete"),
]

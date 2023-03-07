from django.urls import path
from .views import  create_employee, employee_list, get_employee, update_employee, delete_employee

urlpatterns = [
    path('employees/', employee_list, name='employee_list'),
    path('create_employee/', create_employee, name='create_employee'),
    path('get_employees/<int:emp_id>/', get_employee, name='get_employee'),
    path('employee_update/<int:emp_id>/', update_employee, name='update_employee'),
    path('delete_employee/<int:emp_id>/', delete_employee, name='delete_employee'),
]

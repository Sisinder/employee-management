import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.settings')
django.setup()

from appname.models import Employee, Manager

employees = Employee.objects.all()

for employee in employees:
    print(f"Employee ID: {employee.id}")
    print(f"Employee name: {employee.name}")
    if employee.manager:
        print(f"Manager name: {employee.manager}")
    else:
        print("No manager assigned")
    print()

managers = Manager.objects.all()
for manager in managers:
    print(manager.id, manager.name)
from django.http import JsonResponse
from django.shortcuts import render
from .models import Employee, Manager
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_employee(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        emp_id = data.get('id')
        emp_name = data.get('name')
        manager_id = data.get('manager_id')
        manager = Manager.objects.get(pk=manager_id)
        employee = Employee.objects.create(id=emp_id, name=emp_name, manager=manager)
        employee.save()
        return JsonResponse({'message': 'Employee created successfully!'})
    else:
        return JsonResponse({'error': 'Invalid request method!'})

def employee_list(request):
    employees = Employee.objects.all()
    data = []
    for employee in employees:
        data.append({
            'id': employee.id,
            'name': employee.name,
            'manager_name': employee.manager.name if employee.manager else None
        })
    return JsonResponse(data, safe=False) 

def get_employee(request, emp_id):
    try:
        employees=Employee.objects.get(id=emp_id)
    except Employee.DoesNotExist:
        return JsonResponse({"error": "Employee does not exist"})
    return JsonResponse({"name": employees.name})


@csrf_exempt
def update_employee(request, emp_id):
    try:
        employee = Employee.objects.get(id=emp_id)
    except Employee.DoesNotExist:
        return JsonResponse({'error': 'Employee does not exist'})
    
    if request.method == 'PUT':
        data = json.loads(request.body)
        
        # Update employee fields
        employee.name = data.get('name', employee.name)
        
        # Update manager if provided
        manager_id = data.get('manager_id')
        if manager_id:
            try:
                manager = Manager.objects.get(id=manager_id)
                employee.manager = manager
            except Manager.DoesNotExist:
                return JsonResponse({'error': 'Manager does not exist'})
        employee.save()
        
        return JsonResponse({'success': f'Employee {emp_id} updated'})
    else:
        return JsonResponse({'error': 'PUT request required'})
@csrf_exempt
def delete_employee(request, emp_id):
    try:
        employee = Employee.objects.get(id=emp_id)
        employee.delete()
        return JsonResponse({'success': True})
    except Employee.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Employee not found'})

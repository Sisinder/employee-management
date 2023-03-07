from appname.models import Employee, Manager

employee_data = [
    {
        "emp_id": 1,
        "emp_name": "A",
        "manager_name": "B"
    },
    {
        "emp_id": 2,
        "emp_name": "C",
        "manager_name": "B"
    },
    {
        "emp_id": 3,
        "emp_name": "D",
        "manager_name": "C"
    },
    # add more employee data here
]

# loop through the employee data and insert into the Employee and Manager tables
for data in employee_data:
    # get the manager object or create a new one if it doesn't exist
    manager, created = Manager.objects.get_or_create(name=data["manager_name"])

    # create a new employee object with the given data
    employee = Employee(
        id=data["emp_id"],
        name=data["emp_name"],
        manager=manager
    )

    # save the employee object to the database
    employee.save()
    manager.save()

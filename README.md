# employee-management

This is a API to perform CRUD operations to employee Table

1. Create: To Insert a new record into the database
        
       POST url: http://127.0.0.1:8000/create_employee/
  
  
        Json Data:  {
                  "id": 7,
                  "name": "Bob",
                  "manager_id": 2
                }

       Output:  {
                  "message": "Employee created successfully!"
               }

2.Read: To Get all the data from the database
  
    GET url: http://127.0.0.1:8000/employees
  
    Output: [
              {
                  "id": 1,
                  "name": "A",
                  "manager_name": "B"
              },
              {
                  "id": 3,
                  "name": "D",
                  "manager_name": "C"
              }
            ]
    
3. Update: To Update the Existing data using Emp_id

        PUT url: http://127.0.0.1:8000/employee_update/3

        Output: {
          "success": "Employee 3 updated"
                }
                
4. Delete: To Delete the Data of employee based on Emp_id

        DELETE url: http://127.0.0.1:8000/delete_employee/3/

        Output: {
            "success": true
                }

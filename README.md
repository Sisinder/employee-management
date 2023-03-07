# employee-management

This application perform CRUD operations for the employee Table

1. Create: Insert a new record into the database
        
       POST url: http://127.0.0.1:8000/create_employee/
  
  
        Json Data:  {
                  "id": 7,
                  "name": "Bob",
                  "manager_id": 2
                }

       Output:  {
                  "message": "Employee created successfully!"
               }

2.Read: Get all the data from the database
  
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
    
3. Update: Update the Existing data using Emp_id

        PUT url: http://127.0.0.1:8000/employee_update/3

        Output: {
          "success": "Employee 3 updated"
                }
                
4. Delete: Delete the Data of employee based on Emp_id

        DELETE url: http://127.0.0.1:8000/delete_employee/3/

        Output: {
            "success": true
                }

'''
Data Access Adapter

You are working with an old data service that cannot be modified.

The existing service is represented by the following class:

class OldDirectory:
    def __init__(self, employees):
        self.employees = employees

    def get_employee(self, employee_id):
        # Returns an employee record as a dictionary
        # or None if the employee doesn't exist.
        ...

Each employee record looks like:

{
    "id": 42,
    "first_name": "Maya",
    "last_name": "Patel",
    "department": "Engineering",
    "manager_id": 17
}

The existing API has several limitations:

It only retrieves one employee at a time.
Clients should not need to know the underlying dictionary structure.
You cannot modify OldDirectory.
Your Task

Implement a new class called EmployeeDirectory that wraps the existing OldDirectory API and provides a cleaner interface.

Class Requirements

Implement:

EmployeeDirectory(old_directory)

Initializes the wrapper using an existing OldDirectory instance.

Implement:

getEmployeeName(employee_id)

Returns the employee's full name as:

"FirstName LastName"

If the employee does not exist, return None.

Implement:

getEmployeesByDepartment(department)

Returns a list containing the IDs of all employees belonging to the given department.

The order of the returned IDs should match the order in which employees appear in the underlying directory.

Implement:

getManagementChain(employee_id)

Returns a list of employee IDs representing the employee's management chain.

The employee themselves should not be included.

For example, if:

42 → 17 → 5

where 42 reports to 17, and 17 reports to 5, the result should be:

[17, 5]

If the employee does not exist, return an empty list.

Constraints
You may not modify OldDirectory.
You may only access employee information through get_employee().
The directory may contain thousands of employees.
A manager may have many direct reports.
An employee's manager_id may be None.
Assume employee IDs are unique.
Example

Given:

Employee 5  → manager: None
Employee 17 → manager: 5
Employee 42 → manager: 17
Employee 91 → manager: 17
Employee 63 → manager: None

Then:

directory.getEmployeeName(42)

returns:

"Maya Patel"

and:

directory.getEmployeesByDepartment("Engineering")

returns the IDs of the Engineering employees in their original order.

And:

directory.getManagementChain(42)

returns:

[17, 5]
'''

class OldDirectory:
    def __init__(self, employees):
        self.employees = employees

    def get_employee(self, employee_id):
        for i in self.employees:
            if i[0] == employee_id:
                return i

class Employee:
    def __init__(self, name, departement, manager_id):
        self.name = name
        self.departement = departement
        self.manager_id = manager_id

class EmployeeDirectory:
    def __init__(self, old_directory):
        self.store = {}
        self.departements = {}
        self.management = {}
        employees = old_directory.employees

        for i in employees:
            self.store[i[0]] = Employee(str(i[1] + " " + i[2]), i[3], i[4])
            if i[3] in self.departements:
                self.departements[i[3]].append(i[0])
            else:
                self.departements[i[3]] = [i[0]]
            self.management[i[0]] = i[4]

    def getEmployeeName(self, employee_id):
        if employee_id in self.store:
            return self.store[employee_id].name
        else:
            return None

    def getEmployeesByDepartment(self, department):
        if department in self.departements:
            return self.departements[department]
        else:
            return []

    def getManagementChain(self, employee_id):
        manager = self.management[employee_id]
        output = []

        while manager in self.management:
            output.append(manager)
            manager = self.management[manager]
        return output

employees = [
    (10, "A", "One", "Engineering", None),
    (20, "B", "Two", "Sales", None),
    (30, "C", "Three", "Engineering", 10),
    (40, "D", "Four", "Engineering", 10),
]

old = OldDirectory(employees)
directory = EmployeeDirectory(old)

print(directory.getEmployeesByDepartment("Engineering"))
from ninja import NinjaAPI
from testCRUD.models import Department, Employee
from testCRUD.schema import DepartmentSchema, EmployeeInSchema, EmployeeOutSchema, NotFoundSchema
from typing import List, Optional

api = NinjaAPI()

@api.get('/test')
def test(request):
    return { "test": "success" }

@api.get("/departments", response=List[DepartmentSchema])
def all_departments(request, title: Optional[str] = None):
    if title:
        return Department.objects.filter(title__icontains=title)
    return Department.objects.all()

@api.get("/departments/{d_id}", response={200: DepartmentSchema, 404: NotFoundSchema})
def get_department(request, d_id: int):
    try:
        d = Department.objects.get(pk=d_id)
        return 200, d
    except:
        return 404, {"message": "Not Found"}
    
@api.post("/departments", response={201: DepartmentSchema})
def create_department(request, department: DepartmentSchema):
    department = Department.objects.create(**department.dict())
    return department

@api.put("/departments/{d_id}", response={200: DepartmentSchema, 404: NotFoundSchema})
def update_department(request, d_id: int, data: DepartmentSchema):
    try:
        d = Department.objects.get(pk=d_id)
        for attr, value in data.dict().items():
            setattr(d, attr, value)
        d.save()
        return 200, d
    except Department.DoesNotExist as e:
        return 404, {"message": "Not Found"}
    
@api.delete("/departments/{d_id}", response={200: None, 404: NotFoundSchema})
def delete_department(request, d_id: int):
    try:
        d = Department.objects.get(pk=d_id)
        d.delete()
        return 200
    except Department.DoesNotExist as e:
        return 404, {"message": "Not Found"}
    

# -------------------- Employees ------------------

@api.get("/employees", response=List[EmployeeOutSchema])
def all_employees(request, title: Optional[str] = None):
    if title:
        return Employee.objects.filter(first_name__icontains=title)
    return Employee.objects.all()

@api.get("/employees/{e_id}", response={200: EmployeeOutSchema, 404: NotFoundSchema})
def get_employee(request, e_id: int):
    try:
        e = Employee.objects.get(pk=e_id)
        return 200, e
    except:
        return 404, {"message": "Not Found"}
    
@api.post("/employees", response={201: EmployeeOutSchema})#, 500: NotFoundSchema})
def create_employee(request, employee: EmployeeInSchema):
    # try:
    employee = Employee.objects.create(**employee.dict())
    # except:
    #     return 500, {"message": "Can't Create"}
    return 200, employee

@api.put("/employees/{e_id}", response={200: EmployeeOutSchema, 404: NotFoundSchema})
def update_employee(request, e_id: int, data: EmployeeInSchema):
    try:
        e = Employee.objects.get(pk=e_id)
        for attr, value in data.dict().items():
            setattr(e, attr, value)
        e.save()
        return 200, e
    except Employee.DoesNotExist as err:
        return 404, {"message": "Not Found"}
    
@api.delete("/employees/{e_id}", response={200: None, 404: NotFoundSchema})
def delete_employee(request, e_id: int):
    try:
        e = Employee.objects.get(pk=e_id)
        e.delete()
        return 200
    except Employee.DoesNotExist as err:
        return 404, {"message": "Not Found"}
from datetime import date
from ninja import Schema, ModelSchema
from testCRUD.models import Department

class DepartmentSchema(Schema):
    title: str

class EmployeeInSchema(Schema):
    first_name: str
    last_name: str
    department_id: int = None
    birthdate: date = None
    
class EmployeeOutSchema(Schema):
    id: int
    first_name: str
    last_name: str
    department_id: int = None
    birthdate: date = None
    
class NotFoundSchema(Schema):
    message: str

# ModelSchema

class DepartmentModelSchema(ModelSchema):
    class Config:
        model = Department
        model_fields = ['title']

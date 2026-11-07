from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "Nitish"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(..., gt=0.0, lt=10.0, default=8.0)

new_student = {"name": "Alice", "age": 30, "email": "alice@gmail.com", "cgpa": 8.5}

new_student = Student(**new_student)

print(new_student)

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

students = []


# Pydantic model
class Student(BaseModel):
    name: str
    email: str
    course: str


# to create student
@app.post("/student")
def create_student(student: Student):

    students.append(student)

    return {
        "message": "student bn gya successfully",
        "student": student
    }


# view/search by name
@app.get("/student")
def get_students(name: Optional[str] = None):

    # Search by name
    if name:
        for student in students:
            if student.name.lower() == name.lower():
                return student

        return {
            "error": "student nhai hai "
        }

    # View all students
    return students





#uodate
@app.put("/student/{id}")
def update_student(id: int, student: Student):

    if id >= len(students):
        return {
            "error": "student nhai hai"
        }

    students[id] = student

    return {
        "message": "student bna gya successfully",
        "student": student
    }


############ delete krne ke liye use krte hai 

#use kr rhe hai decorator ka  http commands ko handle krke function execute hoga
@app.delete("/student/{id}")
def delete_student(id: int):

    if id >= len(students):
        return {
            "error": "student not found"
        }

    student = students.pop(id)

    return {
        "message": "student deleted successfully",
        "student": student
    }
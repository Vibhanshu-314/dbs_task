from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

students = []


class Student(BaseModel):
    name: str
    email: str
    course: str



@app.post("/student")
def create_student(student: Student):

    students.append(student)

    return {
        "message": "student ban gaya successfully",
        "student": student
    }



@app.get("/student")
def get_students(name: Optional[str] = None):

   
    if name:
        for student in students:
            if student.name.lower() == name.lower():
                return student

        return {
            "error": "student nahi hai"
        }

    
    return students



@app.put("/student/{name}")
def update_student(name: str, student: Student):

    for i in range(len(students)):

        if students[i].name.lower() == name.lower():

            students[i] = student

            return {
                "message": "student update ho gaya successfully",
                "student": student
            }

    return {
        "error": "student nahi hai"
    }



@app.delete("/student/{name}")
def delete_student(name: str):

    for i in range(len(students)):

        if students[i].name.lower() == name.lower():

            student = students.pop(i)

            return {
                "message": "student deleted successfully",
                "student": student
            }

    return {
        "error": "student nahi hai"
    }

STUDENT MANAGEMENT SYSTEM


using the fastapi

FEATURES
1.add new student
2.view all students
3.search by student name
4.delete student

tech stack
1.python
2.fastapi
3.pydantic
4.uvicorn

struc
DBS_task/
|
|--main.py
|
|--README.md


setup instructions
1. create the virtual env
2. activate the venv
3. install req dependencies
4. run the fastapi appication
5. open swagger ui 
for example
hum agr swagger open kree toh 
request body main  value edit  kre skte hai


schemaa yeh hai{
  "name": "vashu",
  "email": "kumarvibhanshu@gmail.com",
  "course": "python"
}
 execute krne prrr create ho jayega 

 or search by name ke liye 
 GET/student
 Name	-vashu
 execeute krne pr 


	
Response body esa hoga
Download
{
  "name": "vashu",
  "email": "kumarvibhanshu@gmail.com",
  "course": "python"
}
 


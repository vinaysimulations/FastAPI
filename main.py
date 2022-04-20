from http.client import HTTPException
from typing import List
from fastapi import FastAPI
from psutil import users

from empdata import Employee

app = FastAPI()

db: List[Employee] = [
    Employee(emp_id="1", emp_name="Vinay K"),
     Employee( emp_id="2", emp_name="anotherone")
]


@app.get("/api/employee")
async def fetch_employees():
    return db();

@app.post("app/employee")
async def register_employee(Employee: emp_id):
    db.append(Employee)
    return {"id" : emp_id.id}

@app.delete("api/employee/{employee_ID")
async def delete_user(user_id : emp_id):
    for user in db:
        if emp_id == emp_id:
            db.remove(Employee)
            return

    raise HTTPException
        status_code=404,
        detail=f"employee with id:{emp_id} doesn't exist"
from ast import Str
from typing import Optional, List
from pydantic import BaseModel

#using pydantic for management and data validation

class Employee(BaseModel):    
    emp_id: int
    emp_name: str
   
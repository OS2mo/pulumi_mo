from typing import Optional

from .base_model import BaseModel


class PersonRead(BaseModel):
    employees: "PersonReadEmployees"


class PersonReadEmployees(BaseModel):
    objects: list["PersonReadEmployeesObjects"]


class PersonReadEmployeesObjects(BaseModel):
    current: Optional["PersonReadEmployeesObjectsCurrent"]


class PersonReadEmployeesObjectsCurrent(BaseModel):
    given_name: str
    surname: str


PersonRead.update_forward_refs()
PersonReadEmployees.update_forward_refs()
PersonReadEmployeesObjects.update_forward_refs()
PersonReadEmployeesObjectsCurrent.update_forward_refs()

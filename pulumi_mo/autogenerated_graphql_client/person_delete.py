from uuid import UUID

from .base_model import BaseModel


class PersonDelete(BaseModel):
    employee_delete: "PersonDeleteEmployeeDelete"


class PersonDeleteEmployeeDelete(BaseModel):
    uuid: UUID


PersonDelete.update_forward_refs()
PersonDeleteEmployeeDelete.update_forward_refs()

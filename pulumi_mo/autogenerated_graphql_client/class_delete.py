from uuid import UUID

from .base_model import BaseModel


class ClassDelete(BaseModel):
    class_delete: "ClassDeleteClassDelete"


class ClassDeleteClassDelete(BaseModel):
    uuid: UUID


ClassDelete.update_forward_refs()
ClassDeleteClassDelete.update_forward_refs()

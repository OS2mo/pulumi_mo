from uuid import UUID

from .base_model import BaseModel


class RolebindingDelete(BaseModel):
    rolebinding_delete: "RolebindingDeleteRolebindingDelete"


class RolebindingDeleteRolebindingDelete(BaseModel):
    uuid: UUID


RolebindingDelete.update_forward_refs()
RolebindingDeleteRolebindingDelete.update_forward_refs()

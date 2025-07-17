from uuid import UUID

from .base_model import BaseModel


class RolebindingCreate(BaseModel):
    rolebinding_create: "RolebindingCreateRolebindingCreate"


class RolebindingCreateRolebindingCreate(BaseModel):
    uuid: UUID


RolebindingCreate.update_forward_refs()
RolebindingCreateRolebindingCreate.update_forward_refs()

from uuid import UUID

from .base_model import BaseModel


class RolebindingUpdate(BaseModel):
    rolebinding_update: "RolebindingUpdateRolebindingUpdate"


class RolebindingUpdateRolebindingUpdate(BaseModel):
    uuid: UUID


RolebindingUpdate.update_forward_refs()
RolebindingUpdateRolebindingUpdate.update_forward_refs()

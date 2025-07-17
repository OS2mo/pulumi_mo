from typing import Optional
from uuid import UUID

from .base_model import BaseModel


class RolebindingRead(BaseModel):
    rolebindings: "RolebindingReadRolebindings"


class RolebindingReadRolebindings(BaseModel):
    objects: list["RolebindingReadRolebindingsObjects"]


class RolebindingReadRolebindingsObjects(BaseModel):
    current: Optional["RolebindingReadRolebindingsObjectsCurrent"]


class RolebindingReadRolebindingsObjectsCurrent(BaseModel):
    user_key: str
    ituser: list["RolebindingReadRolebindingsObjectsCurrentItuser"]
    role: list["RolebindingReadRolebindingsObjectsCurrentRole"]


class RolebindingReadRolebindingsObjectsCurrentItuser(BaseModel):
    uuid: UUID


class RolebindingReadRolebindingsObjectsCurrentRole(BaseModel):
    uuid: UUID


RolebindingRead.update_forward_refs()
RolebindingReadRolebindings.update_forward_refs()
RolebindingReadRolebindingsObjects.update_forward_refs()
RolebindingReadRolebindingsObjectsCurrent.update_forward_refs()
RolebindingReadRolebindingsObjectsCurrentItuser.update_forward_refs()
RolebindingReadRolebindingsObjectsCurrentRole.update_forward_refs()

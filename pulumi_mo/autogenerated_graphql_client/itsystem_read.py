from typing import Optional

from .base_model import BaseModel


class ItsystemRead(BaseModel):
    itsystems: "ItsystemReadItsystems"


class ItsystemReadItsystems(BaseModel):
    objects: list["ItsystemReadItsystemsObjects"]


class ItsystemReadItsystemsObjects(BaseModel):
    current: Optional["ItsystemReadItsystemsObjectsCurrent"]


class ItsystemReadItsystemsObjectsCurrent(BaseModel):
    user_key: str
    name: str


ItsystemRead.update_forward_refs()
ItsystemReadItsystems.update_forward_refs()
ItsystemReadItsystemsObjects.update_forward_refs()
ItsystemReadItsystemsObjectsCurrent.update_forward_refs()

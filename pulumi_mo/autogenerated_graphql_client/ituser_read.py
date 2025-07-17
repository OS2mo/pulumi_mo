from typing import Optional
from uuid import UUID

from .base_model import BaseModel


class ItuserRead(BaseModel):
    itusers: "ItuserReadItusers"


class ItuserReadItusers(BaseModel):
    objects: list["ItuserReadItusersObjects"]


class ItuserReadItusersObjects(BaseModel):
    current: Optional["ItuserReadItusersObjectsCurrent"]


class ItuserReadItusersObjectsCurrent(BaseModel):
    user_key: str
    itsystem: "ItuserReadItusersObjectsCurrentItsystem"
    person: list["ItuserReadItusersObjectsCurrentPerson"] | None


class ItuserReadItusersObjectsCurrentItsystem(BaseModel):
    uuid: UUID


class ItuserReadItusersObjectsCurrentPerson(BaseModel):
    uuid: UUID


ItuserRead.update_forward_refs()
ItuserReadItusers.update_forward_refs()
ItuserReadItusersObjects.update_forward_refs()
ItuserReadItusersObjectsCurrent.update_forward_refs()
ItuserReadItusersObjectsCurrentItsystem.update_forward_refs()
ItuserReadItusersObjectsCurrentPerson.update_forward_refs()

from typing import Optional
from uuid import UUID

from .base_model import BaseModel


class ClassRead(BaseModel):
    classes: "ClassReadClasses"


class ClassReadClasses(BaseModel):
    objects: list["ClassReadClassesObjects"]


class ClassReadClassesObjects(BaseModel):
    current: Optional["ClassReadClassesObjectsCurrent"]


class ClassReadClassesObjectsCurrent(BaseModel):
    user_key: str
    name: str
    it_system: Optional["ClassReadClassesObjectsCurrentItSystem"]
    facet: "ClassReadClassesObjectsCurrentFacet"


class ClassReadClassesObjectsCurrentItSystem(BaseModel):
    uuid: UUID


class ClassReadClassesObjectsCurrentFacet(BaseModel):
    uuid: UUID


ClassRead.update_forward_refs()
ClassReadClasses.update_forward_refs()
ClassReadClassesObjects.update_forward_refs()
ClassReadClassesObjectsCurrent.update_forward_refs()
ClassReadClassesObjectsCurrentItSystem.update_forward_refs()
ClassReadClassesObjectsCurrentFacet.update_forward_refs()

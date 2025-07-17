from uuid import UUID

from .base_model import BaseModel


class TestingFacetRead(BaseModel):
    facets: "TestingFacetReadFacets"


class TestingFacetReadFacets(BaseModel):
    objects: list["TestingFacetReadFacetsObjects"]


class TestingFacetReadFacetsObjects(BaseModel):
    uuid: UUID


TestingFacetRead.update_forward_refs()
TestingFacetReadFacets.update_forward_refs()
TestingFacetReadFacetsObjects.update_forward_refs()

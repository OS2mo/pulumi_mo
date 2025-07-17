from uuid import UUID

from .base_client import BaseClient
from .class_create import ClassCreate
from .class_create import ClassCreateClassCreate
from .class_delete import ClassDelete
from .class_delete import ClassDeleteClassDelete
from .class_read import ClassRead
from .class_read import ClassReadClasses
from .class_update import ClassUpdate
from .class_update import ClassUpdateClassUpdate
from .input_types import ClassCreateInput
from .input_types import ClassFilter
from .input_types import ClassUpdateInput
from .input_types import EmployeeCreateInput
from .input_types import EmployeeFilter
from .input_types import EmployeeUpdateInput
from .input_types import ITSystemCreateInput
from .input_types import ITSystemFilter
from .input_types import ITSystemUpdateInput
from .input_types import ITUserCreateInput
from .input_types import ITUserFilter
from .input_types import ITUserUpdateInput
from .itsystem_create import ItsystemCreate
from .itsystem_create import ItsystemCreateItsystemCreate
from .itsystem_delete import ItsystemDelete
from .itsystem_delete import ItsystemDeleteItsystemDelete
from .itsystem_read import ItsystemRead
from .itsystem_read import ItsystemReadItsystems
from .itsystem_update import ItsystemUpdate
from .itsystem_update import ItsystemUpdateItsystemUpdate
from .ituser_create import ItuserCreate
from .ituser_create import ItuserCreateItuserCreate
from .ituser_delete import ItuserDelete
from .ituser_delete import ItuserDeleteItuserDelete
from .ituser_read import ItuserRead
from .ituser_read import ItuserReadItusers
from .ituser_update import ItuserUpdate
from .ituser_update import ItuserUpdateItuserUpdate
from .person_create import PersonCreate
from .person_create import PersonCreateEmployeeCreate
from .person_delete import PersonDelete
from .person_delete import PersonDeleteEmployeeDelete
from .person_read import PersonRead
from .person_read import PersonReadEmployees
from .person_update import PersonUpdate
from .person_update import PersonUpdateEmployeeUpdate
from .who_am_i import WhoAmI
from .who_am_i import WhoAmIMe


def gql(q: str) -> str:
    return q


class GraphQLClient(BaseClient):
    def class_read(self, filter: ClassFilter) -> ClassReadClasses:
        query = gql(
            """
            query class_read($filter: ClassFilter!) {
              classes(filter: $filter) {
                objects {
                  current {
                    user_key
                    name
                    it_system {
                      uuid
                    }
                    facet {
                      uuid
                    }
                  }
                }
              }
            }
            """
        )
        variables: dict[str, object] = {"filter": filter}
        response = self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return ClassRead.parse_obj(data).classes

    def class_create(self, input: ClassCreateInput) -> ClassCreateClassCreate:
        query = gql(
            """
            mutation class_create($input: ClassCreateInput!) {
              class_create(input: $input) {
                uuid
              }
            }
            """
        )
        variables: dict[str, object] = {"input": input}
        response = self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return ClassCreate.parse_obj(data).class_create

    def class_update(self, input: ClassUpdateInput) -> ClassUpdateClassUpdate:
        query = gql(
            """
            mutation class_update($input: ClassUpdateInput!) {
              class_update(input: $input) {
                uuid
              }
            }
            """
        )
        variables: dict[str, object] = {"input": input}
        response = self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return ClassUpdate.parse_obj(data).class_update

    def class_delete(self, uuid: UUID) -> ClassDeleteClassDelete:
        query = gql(
            """
            mutation class_delete($uuid: UUID!) {
              class_delete(uuid: $uuid) {
                uuid
              }
            }
            """
        )
        variables: dict[str, object] = {"uuid": uuid}
        response = self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return ClassDelete.parse_obj(data).class_delete

    def itsystem_read(self, filter: ITSystemFilter) -> ItsystemReadItsystems:
        query = gql(
            """
            query itsystem_read($filter: ITSystemFilter!) {
              itsystems(filter: $filter) {
                objects {
                  current {
                    user_key
                    name
                  }
                }
              }
            }
            """
        )
        variables: dict[str, object] = {"filter": filter}
        response = self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return ItsystemRead.parse_obj(data).itsystems

    def itsystem_create(
        self, input: ITSystemCreateInput
    ) -> ItsystemCreateItsystemCreate:
        query = gql(
            """
            mutation itsystem_create($input: ITSystemCreateInput!) {
              itsystem_create(input: $input) {
                uuid
              }
            }
            """
        )
        variables: dict[str, object] = {"input": input}
        response = self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return ItsystemCreate.parse_obj(data).itsystem_create

    def itsystem_update(
        self, input: ITSystemUpdateInput
    ) -> ItsystemUpdateItsystemUpdate:
        query = gql(
            """
            mutation itsystem_update($input: ITSystemUpdateInput!) {
              itsystem_update(input: $input) {
                uuid
              }
            }
            """
        )
        variables: dict[str, object] = {"input": input}
        response = self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return ItsystemUpdate.parse_obj(data).itsystem_update

    def itsystem_delete(self, uuid: UUID) -> ItsystemDeleteItsystemDelete:
        query = gql(
            """
            mutation itsystem_delete($uuid: UUID!) {
              itsystem_delete(uuid: $uuid) {
                uuid
              }
            }
            """
        )
        variables: dict[str, object] = {"uuid": uuid}
        response = self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return ItsystemDelete.parse_obj(data).itsystem_delete

    def ituser_read(self, filter: ITUserFilter) -> ItuserReadItusers:
        query = gql(
            """
            query ituser_read($filter: ITUserFilter!) {
              itusers(filter: $filter) {
                objects {
                  current {
                    user_key
                    itsystem {
                      uuid
                    }
                    person {
                      uuid
                    }
                  }
                }
              }
            }
            """
        )
        variables: dict[str, object] = {"filter": filter}
        response = self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return ItuserRead.parse_obj(data).itusers

    def ituser_create(self, input: ITUserCreateInput) -> ItuserCreateItuserCreate:
        query = gql(
            """
            mutation ituser_create($input: ITUserCreateInput!) {
              ituser_create(input: $input) {
                uuid
              }
            }
            """
        )
        variables: dict[str, object] = {"input": input}
        response = self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return ItuserCreate.parse_obj(data).ituser_create

    def ituser_update(self, input: ITUserUpdateInput) -> ItuserUpdateItuserUpdate:
        query = gql(
            """
            mutation ituser_update($input: ITUserUpdateInput!) {
              ituser_update(input: $input) {
                uuid
              }
            }
            """
        )
        variables: dict[str, object] = {"input": input}
        response = self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return ItuserUpdate.parse_obj(data).ituser_update

    def ituser_delete(self, uuid: UUID) -> ItuserDeleteItuserDelete:
        query = gql(
            """
            mutation ituser_delete($uuid: UUID!) {
              ituser_delete(uuid: $uuid) {
                uuid
              }
            }
            """
        )
        variables: dict[str, object] = {"uuid": uuid}
        response = self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return ItuserDelete.parse_obj(data).ituser_delete

    def person_read(self, filter: EmployeeFilter) -> PersonReadEmployees:
        query = gql(
            """
            query person_read($filter: EmployeeFilter!) {
              employees(filter: $filter) {
                objects {
                  current {
                    given_name
                    surname
                  }
                }
              }
            }
            """
        )
        variables: dict[str, object] = {"filter": filter}
        response = self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return PersonRead.parse_obj(data).employees

    def person_create(self, input: EmployeeCreateInput) -> PersonCreateEmployeeCreate:
        query = gql(
            """
            mutation person_create($input: EmployeeCreateInput!) {
              employee_create(input: $input) {
                uuid
              }
            }
            """
        )
        variables: dict[str, object] = {"input": input}
        response = self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return PersonCreate.parse_obj(data).employee_create

    def person_update(self, input: EmployeeUpdateInput) -> PersonUpdateEmployeeUpdate:
        query = gql(
            """
            mutation person_update($input: EmployeeUpdateInput!) {
              employee_update(input: $input) {
                uuid
              }
            }
            """
        )
        variables: dict[str, object] = {"input": input}
        response = self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return PersonUpdate.parse_obj(data).employee_update

    def person_delete(self, uuid: UUID) -> PersonDeleteEmployeeDelete:
        query = gql(
            """
            mutation person_delete($uuid: UUID!) {
              employee_delete(uuid: $uuid) {
                uuid
              }
            }
            """
        )
        variables: dict[str, object] = {"uuid": uuid}
        response = self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return PersonDelete.parse_obj(data).employee_delete

    def who_am_i(self) -> WhoAmIMe:
        query = gql(
            """
            query WhoAmI {
              me {
                actor {
                  uuid
                }
              }
            }
            """
        )
        variables: dict[str, object] = {}
        response = self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return WhoAmI.parse_obj(data).me

from uuid import UUID

from .base_client import BaseClient
from .input_types import EmployeeCreateInput
from .input_types import EmployeeFilter
from .input_types import EmployeeUpdateInput
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

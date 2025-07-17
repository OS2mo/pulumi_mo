from .base_client import BaseClient
from .who_am_i import WhoAmI
from .who_am_i import WhoAmIMe


def gql(q: str) -> str:
    return q


class GraphQLClient(BaseClient):
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

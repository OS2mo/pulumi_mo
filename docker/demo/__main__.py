# SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from pulumi import Config
from pulumi import Output
from pulumi import export

from pulumi_mo.base import create_graphql_client_from_config
from pulumi_mo.person import Person
from pulumi_mo.person import PersonArgs


def fetch_actor_uuid() -> str:
    graphql_client = create_graphql_client_from_config(Config())
    with graphql_client as session:
        result = session.who_am_i()
        return str(result.actor.uuid)


alya = Person("alya", PersonArgs("Alya", "Shadowsong"))

export("actor_uuid", Output.from_input(fetch_actor_uuid()))
export("person_uuid", alya.id)

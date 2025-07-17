# SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from pulumi import Config
from pulumi import Output
from pulumi import export

from pulumi_mo.base import create_graphql_client_from_config
from pulumi_mo.itsystem import ITSystem
from pulumi_mo.itsystem import ITSystemArgs
from pulumi_mo.ituser import ITUser
from pulumi_mo.ituser import ITUserArgs
from pulumi_mo.person import Person
from pulumi_mo.person import PersonArgs


def fetch_actor_uuid() -> str:
    graphql_client = create_graphql_client_from_config(Config())
    with graphql_client as session:
        result = session.who_am_i()
        return str(result.actor.uuid)


alya = Person("alya", PersonArgs("Alya", "Shadowsong"))
suila = ITSystem("suila", ITSystemArgs("Suila"))
suila = itsystem = ITSystem("suila", ITSystemArgs("Suila"))
ituser = ITUser("suila:alya", ITUserArgs("alya", alya.id, suila.id))


export("actor_uuid", Output.from_input(fetch_actor_uuid()))
export("person_uuid", alya.id)
export("itsystem_uuid", suila.id)
export("ituser_uuid", ituser.id)

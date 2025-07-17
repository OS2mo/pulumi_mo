# SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from pulumi import Config
from pulumi import Output
from pulumi import export

from pulumi_mo.base import create_graphql_client_from_config


def fetch_actor_uuid() -> str:
    graphql_client = create_graphql_client_from_config(Config())
    with graphql_client as session:
        result = session.who_am_i()
        return str(result.actor.uuid)


export("actor_uuid", Output.from_input(fetch_actor_uuid()))

# SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from typing import Any

from pulumi import Input
from pulumi import ResourceOptions
from pulumi.dynamic import CheckFailure
from pulumi.dynamic import CheckResult
from pulumi.dynamic import Resource

from .base import AutoMOGraphQLProvider


class PersonProvider(AutoMOGraphQLProvider):
    collection: str = "person"

    def check(self, _olds: dict[str, Any], news: dict[str, Any]) -> CheckResult:
        failures: list[CheckFailure] = []
        for attribute in ["given_name", "surname"]:
            if attribute not in news or news[attribute] == "":
                failures.append(
                    CheckFailure(
                        attribute,
                        reason="Attribute cannot be the empty string",
                    )
                )

        return CheckResult(news, failures)


class PersonArgs:
    given_name: Input[str]
    surname: Input[str]

    def __init__(self, given_name: str, surname: str) -> None:
        self.given_name = given_name
        self.surname = surname


class Person(Resource):
    def __init__(
        self, name: str, args: PersonArgs, opts: ResourceOptions | None = None
    ):
        full_args = {"given_name": None, "surname": None, **vars(args)}
        super().__init__(PersonProvider(), name, full_args, opts)

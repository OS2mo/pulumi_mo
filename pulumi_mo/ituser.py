# SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from typing import Any

from pulumi import Input
from pulumi import ResourceOptions
from pulumi.dynamic import CheckFailure
from pulumi.dynamic import CheckResult
from pulumi.dynamic import Resource

from .base import AutoMOGraphQLProvider


class ITUserProvider(AutoMOGraphQLProvider):
    collection: str = "ituser"

    def check(self, _olds: dict[str, Any], news: dict[str, Any]) -> CheckResult:
        failures: list[CheckFailure] = []
        if "user_key" not in news or news["user_key"] == "":
            failures.append(
                CheckFailure(
                    "user_key",
                    reason="Attribute cannot be the empty string",
                )
            )
        return CheckResult(news, failures)


class ITUserArgs:
    user_key: Input[str]
    person: Input[str]
    itsystem: Input[str]

    def __init__(self, user_key: str, person: Input[str], itsystem: Input[str]) -> None:
        self.user_key = user_key
        self.person = person
        self.itsystem = itsystem


class ITUser(Resource, name="ITUser"):
    def __init__(
        self, name: str, args: ITUserArgs, opts: ResourceOptions | None = None
    ) -> None:
        full_args = {"user_key": None, "person": None, "itsystem": None, **vars(args)}
        super().__init__(ITUserProvider(), name, full_args, opts)

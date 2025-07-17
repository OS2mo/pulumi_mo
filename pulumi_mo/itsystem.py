# SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from typing import Any

from pulumi import Input
from pulumi import ResourceOptions
from pulumi.dynamic import CheckFailure
from pulumi.dynamic import CheckResult
from pulumi.dynamic import Resource

from .base import AutoMOGraphQLProvider


class ITSystemProvider(AutoMOGraphQLProvider):
    collection: str = "itsystem"

    def check(self, _olds: dict[str, Any], news: dict[str, Any]) -> CheckResult:
        failures: list[CheckFailure] = []
        if "user_key" not in news or news["user_key"] == "":
            failures.append(
                CheckFailure(
                    "user_key",
                    reason="Attribute cannot be the empty string",
                )
            )
        if "name" in news and news["name"] == "":
            failures.append(
                CheckFailure(
                    "name",
                    reason="Attribute cannot be the empty string",
                )
            )
        return CheckResult(self.transform(news), failures)

    def transform(self, news: dict[str, Any]) -> dict[str, Any]:
        name = news.get("name", news["user_key"].capitalize())
        return {**news, "name": name}


class ITSystemArgs:
    user_key: Input[str]
    name: Input[str] | None

    def __init__(self, user_key: str, name: str | None = None) -> None:
        self.user_key = user_key
        self.name = name


class ITSystem(Resource):
    def __init__(
        self, name: str, args: ITSystemArgs, opts: ResourceOptions | None = None
    ) -> None:
        full_args = {"user_key": None, "name": None, **vars(args)}
        super().__init__(ITSystemProvider(), name, full_args, opts)

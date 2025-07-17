# SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from typing import Any

from pulumi import Input
from pulumi import ResourceOptions
from pulumi.dynamic import CheckFailure
from pulumi.dynamic import CheckResult
from pulumi.dynamic import Resource

from .base import AutoMOGraphQLProvider


class RoleBindingProvider(AutoMOGraphQLProvider):
    collection: str = "rolebinding"

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


class RoleBindingArgs:
    user_key: Input[str]
    ituser: Input[str]
    role: Input[str]

    def __init__(self, user_key: str, ituser: Input[str], role: Input[str]) -> None:
        self.user_key = user_key
        self.ituser = ituser
        self.role = role


class RoleBinding(Resource, name="RoleBinding"):
    def __init__(
        self, name: str, args: RoleBindingArgs, opts: ResourceOptions | None = None
    ):
        full_args = {"user_key": None, "ituser": None, "role": None, **vars(args)}
        super().__init__(RoleBindingProvider(), name, full_args, opts)

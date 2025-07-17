# SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
import random
import string
from collections.abc import Callable
from collections.abc import Iterator
from contextlib import AbstractContextManager
from contextlib import contextmanager

import pytest
from pulumi.automation import LocalWorkspaceOptions
from pulumi.automation import ProjectBackend
from pulumi.automation import ProjectSettings
from pulumi.automation import Stack
from pulumi.automation import create_stack
from pulumi.automation import fully_qualified_stack_name


def randomword(length: int) -> str:
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))


@pytest.fixture
def project_name(request: pytest.FixtureRequest) -> str:
    testname = request.node.name
    assert isinstance(testname, str)
    return testname


@pytest.fixture
def stack_name(project_name: str) -> str:
    return fully_qualified_stack_name("organization", project_name, randomword(10))


@pytest.fixture(autouse=True)
def pulumi_config_passphrase(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("PULUMI_CONFIG_PASSPHRASE", "hunter2")


StackBuilder = Callable[[Callable[[], None]], AbstractContextManager[Stack]]


@pytest.fixture
def stack_builder(project_name: str, stack_name: str) -> StackBuilder:
    @contextmanager
    def inner(pulumi_program: Callable[[], None]) -> Iterator[Stack]:
        stack = create_stack(
            stack_name=stack_name,
            project_name=project_name,
            program=pulumi_program,
            # Configure our backend storage to be the local filesystem
            # This is required to avoid having to run `pulumi login --local`
            opts=LocalWorkspaceOptions(
                project_settings=ProjectSettings(
                    name=project_name,
                    runtime="python",
                    backend=ProjectBackend(url="file://~"),
                )
            ),
        )
        yield stack
        stack.workspace.remove_stack(stack_name, force=True)

    return inner

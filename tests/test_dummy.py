# SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
import pytest


def test_dummy1() -> None:
    pass


async def test_dummy2() -> None:
    pass


@pytest.mark.integration_test
def test_dummy3() -> None:
    pass


@pytest.mark.integration_test
async def test_dummy4() -> None:
    pass

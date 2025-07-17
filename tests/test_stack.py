# SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from pulumi.automation import ConfigMap
from pulumi.automation import ConfigValue
from pulumi.automation import OpType

from .conftest import StackBuilder


def test_stack(
    stack_builder: StackBuilder,
) -> None:
    def pulumi_program() -> None:
        from pulumi import Config
        from pulumi import export

        config = Config()
        export("exp_static", "foo")
        export("exp_cfg", config.get("bar"))
        export("exp_secret", config.get_secret("buzz"))

    config: ConfigMap = {
        "bar": ConfigValue(value="abc"),
        "buzz": ConfigValue(value="secret", secret=True),
    }

    with stack_builder(pulumi_program) as stack:
        stack.set_all_config(config)

        # pulumi preview
        preview_result = stack.preview()
        assert preview_result.change_summary.get(OpType.CREATE) == 1

        # pulumi up
        up_res = stack.up()
        assert up_res.summary.kind == "update"
        assert up_res.summary.result == "succeeded"

        assert up_res.outputs.keys() == {"exp_static", "exp_cfg", "exp_secret"}
        assert up_res.outputs["exp_static"].value == "foo"
        assert up_res.outputs["exp_static"].secret is False

        assert up_res.outputs["exp_cfg"].value == "abc"
        assert up_res.outputs["exp_cfg"].secret is False

        assert up_res.outputs["exp_secret"].value == "secret"
        assert up_res.outputs["exp_secret"].secret is True

        # pulumi preview
        preview_result = stack.preview()
        assert preview_result.change_summary.get(OpType.SAME) == 1

        # pulumi refresh
        refresh_res = stack.refresh()
        assert refresh_res.summary.kind == "refresh"
        assert refresh_res.summary.result == "succeeded"

        # pulumi destroy
        destroy_res = stack.destroy()
        assert destroy_res.summary.kind == "destroy"
        assert destroy_res.summary.result == "succeeded"

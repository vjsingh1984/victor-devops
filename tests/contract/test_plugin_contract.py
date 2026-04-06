from pathlib import Path
from unittest.mock import Mock

import tomllib

from victor_sdk import VictorPlugin

from victor_devops.assistant import DevOpsAssistant
from victor_devops.plugin import DevOpsPlugin, plugin


def _entry_points() -> dict:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))
    return pyproject["project"]["entry-points"]


def test_pyproject_registers_plugin_instance_entry_point() -> None:
    entry_points = _entry_points()

    assert entry_points["victor.plugins"]["devops"] == "victor_devops.plugin:plugin"


def test_pyproject_registers_canonical_runtime_extension_entry_points() -> None:
    entry_points = _entry_points()

    assert entry_points["victor.prompt_contributors"]["devops"] == (
        "victor_devops.prompts:DevOpsPromptContributor"
    )
    assert entry_points["victor.mode_configs"]["devops"] == (
        "victor_devops.mode_config:DevOpsModeConfigProvider"
    )
    assert entry_points["victor.workflow_providers"]["devops"] == (
        "victor_devops.workflows:DevOpsWorkflowProvider"
    )
    assert entry_points["victor.capability_providers"]["devops"] == (
        "victor_devops.capabilities:DevOpsCapabilityProvider"
    )
    assert entry_points["victor.team_spec_providers"]["devops"] == (
        "victor_devops.teams:DevOpsTeamSpecProvider"
    )
    assert entry_points["victor.framework.teams.providers"]["devops"] == (
        "victor_devops.teams:DevOpsTeamSpecProvider"
    )


def test_plugin_implements_protocol_and_registers_vertical() -> None:
    context = Mock()

    assert isinstance(plugin, VictorPlugin)
    assert isinstance(plugin, DevOpsPlugin)
    assert plugin.name == "devops"

    plugin.register(context)

    context.register_vertical.assert_called_once_with(DevOpsAssistant)

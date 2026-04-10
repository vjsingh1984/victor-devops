"""DevOps vertical package with lazy exports for SDK-first installs."""

from __future__ import annotations

from importlib import import_module
from typing import Any

__all__ = [
    "DevOpsAssistant",
    "DevOpsPromptContributor",
    "DevOpsModeConfigProvider",
    "DevOpsSafetyExtension",
    "EnhancedDevOpsSafetyExtension",
    "EnhancedDevOpsConversationManager",
    "DevOpsSafetyRules",
    "DevOpsContext",
    "DevOpsToolDependencyProvider",
    "DevOpsCapabilityProvider",
    "DevOpsPlugin",
    "plugin",
    "DevOpsSandboxProvider",
    "DevOpsPermissionProvider",
    "DevOpsHookProvider",
]

_EXPORTS = {
    "DevOpsAssistant": ("victor_devops.assistant", "DevOpsAssistant"),
    "DevOpsPromptContributor": ("victor_devops.prompts", "DevOpsPromptContributor"),
    "DevOpsModeConfigProvider": ("victor_devops.mode_config", "DevOpsModeConfigProvider"),
    "DevOpsSafetyExtension": ("victor_devops.safety", "DevOpsSafetyExtension"),
    "EnhancedDevOpsSafetyExtension": (
        "victor_devops.safety_enhanced",
        "EnhancedDevOpsSafetyExtension",
    ),
    "EnhancedDevOpsConversationManager": (
        "victor_devops.conversation_enhanced",
        "EnhancedDevOpsConversationManager",
    ),
    "DevOpsSafetyRules": ("victor_devops.safety_enhanced", "DevOpsSafetyRules"),
    "DevOpsContext": ("victor_devops.conversation_enhanced", "DevOpsContext"),
    "DevOpsToolDependencyProvider": (
        "victor_devops.tool_dependencies",
        "DevOpsToolDependencyProvider",
    ),
    "DevOpsCapabilityProvider": ("victor_devops.capabilities", "DevOpsCapabilityProvider"),
    "DevOpsPlugin": ("victor_devops.plugin", "DevOpsPlugin"),
    "plugin": ("victor_devops.plugin", "plugin"),
    "DevOpsSandboxProvider": ("victor_devops.protocols", "DevOpsSandboxProvider"),
    "DevOpsPermissionProvider": ("victor_devops.protocols", "DevOpsPermissionProvider"),
    "DevOpsHookProvider": ("victor_devops.protocols", "DevOpsHookProvider"),
}


def __getattr__(name: str) -> Any:
    target = _EXPORTS.get(name)
    if target is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    module_name, attribute_name = target
    module = import_module(module_name)
    return getattr(module, attribute_name)

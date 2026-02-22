"""DevOps Vertical Package - Complete implementation with extensions.

Competitive use case: Replaces/augments Docker Desktop AI, Terraform Assistant, Pulumi AI.

This vertical provides:
- Docker and container management
- CI/CD pipeline configuration
- Infrastructure as Code (IaC) generation
- Kubernetes manifest creation
- Monitoring and observability setup
"""

from victor_devops.assistant import DevOpsAssistant
from victor_devops.prompts import DevOpsPromptContributor
from victor_devops.mode_config import DevOpsModeConfigProvider
from victor_devops.safety import DevOpsSafetyExtension
from victor_devops.tool_dependencies import DevOpsToolDependencyProvider
from victor_devops.capabilities import DevOpsCapabilityProvider

__all__ = [
    "DevOpsAssistant",
    "DevOpsPromptContributor",
    "DevOpsModeConfigProvider",
    "DevOpsSafetyExtension",
    "DevOpsToolDependencyProvider",
    "DevOpsCapabilityProvider",
]

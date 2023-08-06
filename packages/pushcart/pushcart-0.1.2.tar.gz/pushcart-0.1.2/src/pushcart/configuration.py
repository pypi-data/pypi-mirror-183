import json

import toml
import yaml
from traitlets import Dict, HasTraits, List, Unicode, observe, validate

from pushcart.configuration.validation.common import SystemFilePath


class Configuration(HasTraits):
    """
    Stores pipeline configuration as read from JSON, TOML and YAML files or strings.
    """

    from_dict = Dict(
        default_value={},
        help="Dictionary containing the configuration for the pipeline",
        allow_none=True,
        per_key_traits={
            "sources": List(trait=Dict(), allow_none=True),
            "transformations": List(trait=Dict(), allow_none=True),
            "destinations": List(trait=Dict(), allow_none=True),
        },
    )
    from_file = SystemFilePath(
        default_value=None,
        allow_none=True,
        search_paths=[
            "/Workspace/Repos/",
            "/Workspace",
            "/dbfs",
            "/tmp",
        ],
        help="File path to instantiate with. JSON, TOML and YAML supported.",
    )
    from_json_string = Unicode(
        default_value=None,
        allow_none=True,
        help="JSON string containing configuration",
    )
    from_toml_string = Unicode(
        default_value=None,
        allow_none=True,
        help="TOML string containing configuration",
    )
    from_yaml_string = Unicode(
        default_value=None,
        allow_none=True,
        help="YAML string containing configuration",
    )

    __config = {}

    @validate("from_dict")
    def _validate_from_dict(self, proposal: dict) -> dict:
        from_dict = proposal["value"]

        if not any(
            key in from_dict for key in ["sources", "transformations", "destinations"]
        ):
            raise ValueError(
                "At least one of: sources, transformations, destinations must be defined."
            )

        return proposal["value"]

    @observe("from_dict")
    def __from_dict(self, change) -> None:
        self.__config = change.new

    @validate("from_file")
    def _validate_from_file(self, proposal) -> str:
        from_file = proposal["value"]
        file_extensions = (".json", ".toml", ".yaml")

        if not from_file.endswith(file_extensions):
            raise ValueError(f"Unsupported file type: {from_file}")

        return proposal["value"]

    @observe("from_file")
    def __from_file(self, change) -> None:
        from_file = change.new

        if from_file.endswith(".json"):
            with open(from_file, "r") as f:
                self.from_dict = json.load(f)
            return

        if from_file.endswith(".toml"):
            self.from_dict = toml.load(from_file)
            return

        if from_file.endswith(".yaml") or from_file.endswith(".yml"):
            with open(from_file, "r") as f:
                self.from_dict = yaml.safe_load(f)
            return

    @observe("from_json_string")
    def __from_json_string(self, change) -> None:
        return self.from_dict(json.loads(change.new))

    def __from_toml_string(self, change) -> None:
        return self.from_dict(toml.loads(change.new))

    def __from_yaml_string(self, change) -> None:
        return self.from_dict(yaml.safe_load(change.new))

    def to_dict(self) -> dict:
        return self.__config

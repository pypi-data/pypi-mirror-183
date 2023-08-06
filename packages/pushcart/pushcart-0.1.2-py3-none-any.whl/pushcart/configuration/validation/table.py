import pathlib
import re

from traitlets import TraitType, Undefined


class TableName(TraitType):
    """
    Custom TraitType for storing the name of a Spark table, optionally including metastore and database
    """

    def __init__(self, default_value=Undefined, allow_none=False, **kwargs):
        self.regex_starts_with = re.compile(r"[A-Za-z_]")
        self.regex_allowed_chars = re.compile(r"^[A-Za-z0-9_.]*$")
        self.regex_ends_with = re.compile(r"\.$")

        super(TableName, self).__init__(
            default_value=default_value, allow_none=allow_none, **kwargs
        )

    def validate_table_name(self, value):
        """
        Checks:
        - that the value starts with a letter or underscore
        - that the value only contains letters, digits, underscores, and periods
        - that the value does not end with a period
        - that the length of the value after the last period character is max 64 characters
        """

        if not isinstance(value, str):
            return

        if not self.regex_starts_with.match(value):
            return

        if not self.regex_allowed_chars.match(value):
            return

        if self.regex_ends_with.match(value):
            return

        if len(value.split(".")[-1]) > 64:
            return

        return value

    def validate(self, obj, value):
        if not self.validate_table_name(value):
            self.error(obj)

        return value


class ViewName(TraitType):
    """
    Custom TraitType for storing the name of a Spark view
    """

    def __init__(self, default_value=Undefined, allow_none=False, **kwargs):
        self.regex_starts_with = re.compile(r"[A-Za-z_]")
        self.regex_allowed_chars = re.compile(r"^[A-Za-z0-9_]*$")

        super(ViewName, self).__init__(
            default_value=default_value, allow_none=allow_none, **kwargs
        )

    def validate_view_name(self, value):
        """
        Checks:
        - that the value starts with a letter or underscore
        - that the value only contains letters, digits or underscores
        - that the value does not end with a period
        - that the length of the value is max 64 characters
        """

        if not isinstance(value, str):
            return

        if not self.regex_starts_with.match(r"[A-Za-z_]"):
            return

        if not self.regex_allowed_chars.match(r"^[A-Za-z0-9_]*$"):
            return

        if len(value) > 64:
            return

        return value

    def validate(self, obj, value):
        if not self.validate_view_name(value):
            self.error(obj)

        return value


class DestinationDataPath(TraitType):
    def __init__(self, default_value=Undefined, allow_none=False, **kwargs):
        self.path_regex = re.compile(r"^(file:|dbfs:|s3:|abfss:)\/.*$")
        super(DestinationDataPath, self).__init__(
            default_value=default_value, allow_none=allow_none, **kwargs
        )

    def validate_path_syntax(self, path):
        """
        Use a regular expression to check whether the path is in one of file:/,
        dbfs:/, s3:/ or abfss:/ locations. If it is, it split the prefix from the rest
        of the path, then attempt to create a pathlib.Path object from the rest of the
        path. Check whether it is an absolute path and if true, return the path (with
        the prefix added back)
        """
        if not isinstance(path, str):
            return

        prefix = ""
        if match := self.path_regex.match(path):
            prefix, path = match.groups()

        try:
            p = pathlib.Path(path)
            if p.is_absolute():
                return prefix + path
        except ValueError:
            pass

    def validate(self, obj, value):
        if not self.validate_path_syntax(value):
            self.error(obj)

        return value

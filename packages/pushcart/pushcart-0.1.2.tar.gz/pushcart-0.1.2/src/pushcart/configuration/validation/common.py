import os

from traitlets import Undefined, Unicode


class SystemPath(Unicode):
    """
    Custom TraitType for storing a system path
    """

    def __init__(
        self,
        default_value=Undefined,
        allow_none=False,
        file=False,
        directory=False,
        search_paths=None,
        **kwargs,
    ):
        self.file = file
        self.directory = directory
        self.search_paths = search_paths

        if file and directory:
            raise ValueError("Path cannot be a file and a directory at the same time")

        super(SystemPath, self).__init__(
            default_value=default_value, allow_none=allow_none, **kwargs
        )

    def validate_system_abs_path(self, path):
        """
        Check whether the path is an existing file, directory, or any kind of path,
        depending on the values of the file and directory attributes. If the path is
        valid, it returns the path, otherwise it returns None
        """
        if (not self.file and not self.directory) and os.path.exists(path):
            return path
        if (self.file and not self.directory) and os.path.isfile(path):
            return path
        if (not self.file and self.directory) and os.path.isdir(path):
            return path

    def validate_system_path(self, value, search_paths=None):
        """
        First normalize path by removing any redundant separators and "." and ".."
        components. If the path is absolute, call the validate_system_abs_path method
        to validate the path. If the path is not absolute, iterate through the search
        paths and append the path to each search path to create an absolute path. Call
        the validate_system_abs_path method to validate each absolute path.
        """
        path = os.path.normpath(value)

        if not search_paths:
            search_paths = [os.getcwd()]

        if os.path.isabs(path):
            return self.validate_system_abs_path(path)
        else:
            for p in search_paths:
                abs_path = os.path.join(os.path.normpath(p), path)

                if found := self.validate_system_abs_path(abs_path):
                    return found

    def validate(self, obj, value):
        parsed_value = self.validate_system_path(value, search_paths=self.search_paths)
        if not parsed_value:
            self.error(obj)

        return parsed_value


class SystemFilePath(SystemPath):
    """
    Custom TraitType for storing an existing file path on the system
    """

    def __init__(
        self,
        default_value=Undefined,
        allow_none=False,
        search_paths=None,
        **kwargs,
    ):
        super(SystemFilePath, self).__init__(
            default_value=default_value,
            allow_none=allow_none,
            file=True,
            search_paths=search_paths,
            **kwargs,
        )


class SystemDirectoryPath(SystemPath):
    """
    Custom TraitType for storing an existing directory path on the system
    """

    def __init__(
        self,
        default_value=Undefined,
        allow_none=False,
        search_paths=None,
        **kwargs,
    ):
        super(SystemDirectoryPath, self).__init__(
            default_value=default_value,
            allow_none=allow_none,
            directory=True,
            search_paths=search_paths,
            **kwargs,
        )

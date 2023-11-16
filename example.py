from inspyred_hints.integrations.base_classes import HelpfulError



class MainError(HelpfulError):
    """
    Resolution hints:
        - A point to consider.
        - Another point worth considering.
    """
    def __init__(self, message, **kwargs):
        super().__init__(message, **kwargs)
        self.print_hints()


class MainErrorSubError(MainError):
    """
    Raise on some granular error.

    Attributes:
        message (str):
            The error message, also used as a parameter.

         delay (int|float):
             The delay in seconds before printing the error hints.

    Resolution hints:
        - A more granular point to consider.
        - Another even more granular point worth considering.
    """
    pass


class AppPermissionError(MainError):
    pass

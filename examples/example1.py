from inspyred_hints import print_hints


class GUIWindowError(Exception):
    """
    A generic error class for GUI window issues.

    Attributes:
        message (str):
            A descriptive error message, also used as an argument.

        delay (int|float):
            The delay in seconds before printing the hints. Default is 2 seconds.  

    Usage Example:
        >>> raise GUIWindowError('An unknown GUI Window error occurred.')
        Traceback (most recent call last):
        ...
        GUIWindowError: An unknown GUI window error occurred.
    """

    def __init__(self, message: str, delay=2):
        super().__init__(message)
        self.message = message
        print_hints(self, delay=delay)


class WindowAlreadyBuiltError(GUIWindowError):
    """
    An error class for when a window is attempted to be built
    more than once.

    Resolution hints:
        - If you are attempting to build a window that's already been closed, you will need  to  instantiate another instance.
        - If you are attempting to build a window that has not yet been run, try calling the :meth:`run` method` on the window instance to run it.

    Attributes:
        message (str):
            A descriptive error message, also used as an argument.

    Inherits:
        :class:`GUIWindowError`

    Usage example:
        >>> raise WindowAlreadyBuiltError('The target-window has already been built!')
    """
    pass

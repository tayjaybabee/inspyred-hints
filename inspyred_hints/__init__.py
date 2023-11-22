from __future__ import annotations

from time import sleep
from threading import Thread


def get_hints(obj, section_name: str = None, case_sensitive: bool = False):
    """
    Searches for the given section in the docstring;
        - If the section is found, it's returned as a list of strings.
        - If the section isn't found, an empty list is returned.

    Arguments:
        obj (Exception|HelpfulError):
            The docstring in which to search for the section.

        section_name (string):
            The name of the section to search for. Defaults to 'Resolution hints'.

        case_sensitive (bool):
            Whether the section search should be case-sensitive. Defaults to False.
    """
    docstr = obj.__doc__

    if docstr is None:
        return []

    section_name = section_name or "Resolution hints"

    if not case_sensitive:
        docstr = docstr.lower()
        section_name = section_name.lower()

    hints_section = find_hint_section(docstr, section_name)

    hints = hints_section.split("\n")

    # Drop the first line
    hints = hints[1:]

    return [hint.lstrip(" -") for hint in hints]


def find_hint_section(docstr, section_name):
    """
    Finds and returns the specified section from the given docstring.

    Parameters:
        docstr (str):
            The docstring to search.

        section_name (str):
            The name of the section to find.

    Returns:
        str: The text of the specified section from the docstring.

    Raises:
        ValueError:
            If the specified section isn't found in the docstring.
    """
    try:
        # Find the start of the target section
        start = docstr.index(section_name) + len(section_name)

        # Find  the end
        end = docstr.find("\n\n", start)

        if end == -1:
            end = len(docstr)

        # Grab the text from the target section.
        hints = docstr[start:end].strip()
    except ValueError as e:
        raise ValueError(f'Section "{section_name}" not found in docstring.') from e

    return hints


def asynchronous_hints(delay: (int | float)):
    def wrapper(func):
        def wrapper2(*args, **kwargs):
            t = Thread(target=func, args=args, kwargs=kwargs)
            t.start()
            sleep(delay)
            return t

        return wrapper2

    return wrapper


def print_hints(obj, delay=2):
    """
    Prints the hints extracted from the docstring of the given object.
    This function utilizes `get_hints` to extract 'Resolution hints' from the object's docstring.
    After a delay of 2 seconds, it prints the class name of the object and the extracted hints.

    Arguments:
        obj (object):
            The object whose hints are to be printed.

        delay (int|float):
            The delay in seconds before printing the hints. Default is 2 seconds.

    Returns:
        None

    Examples:
        >>> class Example:
        ...     '''This is an example class.
        ...
        ...     Resolution hints
        ...         - Use this approach
        ...         - Consider these factors
        ...     '''
        ...
        >>> print_hints(Example)
        # Waits for the given delay, then prints:
        #
        # Some hints for "Example":
        #   - Use this approach
        #   - Consider these factors

    Note:
        The function has a built-in delay (which defaults to 2 seconds)
        before printing the hints. You can override this delay by passing
        :int:`0` or :float:`0.0` as the value for the :param:`delay` parameter.
    """

    # Get the hints
    hints = get_hints(obj)

    thread = Thread(target=asynchronous_hints, daemon=True, args=[delay])

    thread.start()

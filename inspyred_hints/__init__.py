from time import sleep
from threading import Thread


def get_hints(obj):
    """
    Extracts a specific section from the docstring of the given object.
    This function searches for a section titled 'Resolution hints' within the docstring of the provided object.
    It then formats and returns the contents of this section as a list of strings.

    Args:
        obj (object): The object whose docstring is to be parsed.

    Returns:
        list of str: The formatted hints extracted from the docstring. Each hint is a string in the returned list.
        str: A message indicating the section was not found if 'Resolution hints' is not present in the docstring.

    Raises:
        ValueError: If the docstring does not contain the term 'Resolution hints'.

    Examples:
        >>> class Example:
        ...     '''This is an example class.
        ...
        ...     Resolution hints
        ...         - Hint 1
        ...         - Hint 2
        ...     '''
        ...
        >>> get_hints(Example)
        ['Hint 1', 'Hint 2']

    Note:
        The function assumes the hints section is formatted with each hint preceded by '        - '.
    """
    term = 'Resolution hints'

    # Grab docstring for object
    doc = obj.__doc__

    if not doc:
        raise ValueError(f'Docstring not found in the provided object.')

    # Get the index for the section.
    try:
        # Find the start of the target section
        start = doc.index(term) + len(term)

        # Find the end of the target section or end of the docstring if no other section follows.
        end = doc.find('\n\n', start)
        if end == -1:
            end = len(doc)

        # Grab the text from the target section.
        hints = doc[start:end].strip()

    except ValueError:
        return f'Section "{term}" not found in docstring.'

    # Format the hints before returning
    # Break up the hints into a list of strings by newlines.
    hints = hints.split('\n')

    # Ignore the first line.
    hints = hints[1:]

    # Strip the leading spaces and '-' from each line before returning.
    return [hint.lstrip(' -') for hint in hints]


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

    def print_hints_thread(delay):
        sleep(delay)

        print(f'\nSome hints for "{obj.__class__.__name__}":\n')

        for hint in hints:
            print(f'  - {hint}')

    thread = Thread(target=print_hints_thread, daemon=True, args=[delay])

    thread.start()

from inspyred_hints import get_hints, print_hints
from threading import Thread
import time


class HelpfulError(Exception):
    def __init__(self, message, delay=2, use_parent_hints=True):
        super().__init__(message)
        self.delay = delay
        self.use_parent_hints = use_parent_hints

    def print_hints(self):
        hints = get_hints(self)

        if not hints and self.use_parent_hints:
            # Pass the parent class to the `get_hints` function.
            hints = get_hints(self.__class__)

        lines = [f"\nSome hints for {self.__class__.__name__}:\n"]

        for hint in hints:
            lines.append(f"  - {hint}")

        # Create a new thread to print the hints after a delay.
        hint_thread = Thread(target=self._print_hints, args=[lines])
        hint_thread.start()

    def _print_hints(self, lines):

        # Delay before printing the hints.
        time.sleep(self.delay)

        # Print the hints.
        print("\n".join(lines))

    @property
    def delay(self):
        return self.__delay

    @delay.setter
    def delay(self, new):
        if not isinstance(new, (int, float)):
            raise TypeError('"delay" must be a float or an integer!')

        self.__delay = new if not new in [0, 0.0] else None

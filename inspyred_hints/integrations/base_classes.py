from inspyred_hints import get_hints, print_hints


class HelpfulError(Exception):
    def __init__(self, message, delay=2, use_parent_hints=True):
        super().__init__(message)
        self.delay = delay
        self.use_parent_hints = use_parent_hints

    def print_hints(self):

        section_title = 'Resolution hints'.lower()

        if self.__doc__:
            l_doc = self.__doc__.lower()
            # Check if the current class has resolution hints.
            if section_title in l_doc:
                return print_hints(self)
            else:
                if self.use_parent_hints:
                    parent = self.__class__.__bases__[0]
                    p_l_doc = parent.__doc__.lower()
                    if parent.__doc__ and self.use_parent_hints:
                        if section_title in p_l_doc:
                            return print_hints(parent)


    @property
    def delay(self):
        return self.__delay

    @delay.setter
    def delay(self, new):
        if not isinstance(new, (int, float)):
            raise TypeError('"delay" must be a float or an integer!')

        self.__delay = new if not new in [0, 0.0] else None

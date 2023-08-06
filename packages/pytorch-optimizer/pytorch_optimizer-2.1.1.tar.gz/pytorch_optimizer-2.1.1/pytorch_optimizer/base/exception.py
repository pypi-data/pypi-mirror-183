class NoSparseGradientError(Exception):
    """Raised when the gradient is sparse gradient

    :param optimizer_name: str. optimizer name.
    :param note: str. special conditions to note (default '').
    """

    def __init__(self, optimizer_name: str, note: str = ''):
        self.note: str = ' ' if note == '' else f' w/ {note} '
        self.message: str = f'[-] {optimizer_name}{self.note}does not support sparse gradient.'
        super().__init__(self.message)


class ZeroParameterSizeError(Exception):
    """Raised when the parameter size is 0"""

    def __init__(self):
        self.message: str = '[-] parameter size is 0'
        super().__init__(self.message)


class NoClosureError(Exception):
    """Raised when there's no closure function"""

    def __init__(self, optimizer_name: str):
        self.message: str = f'[-] {optimizer_name} requires closure.'
        super().__init__(self.message)

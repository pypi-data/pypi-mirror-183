from jsonpath_tp.compile.compile_error import JsonpathSyntaxError


class Parser:
    __slots__ = (
        "text",
        "offset",
        "__mark",
        "length"
    )

    def __init__(self, text: str):
        self.text: str = text.strip()
        self.offset: int = -1
        self.__mark: int = -1
        self.length = len(self.text)

    def __iter__(self):
        return self

    def __next__(self) -> str:
        self.offset += 1
        try:
            return self.text[self.offset]
        except IndexError:
            raise StopIteration()

    def next_none_whitespace_char(self) -> str:
        char = next(self)
        while char.isspace():
            char = next(self)
        return char

    def current_or_next_none_whitespace_char(self) -> str:
        char = self.current()
        while char.isspace():
            char = next(self)
        return char

    def current(self) -> str:
        return self.text[self.offset]

    def has_next(self) -> bool:
        return (self.offset + 1) < self.length

    def adjust_offset(self, adjustment: int):
        self.offset += adjustment

    def undo_next(self):
        self.adjust_offset(-1)

    def raise_jsonpath_systax_error(self, error_message: str):
        raise JsonpathSyntaxError(
            error_message,
            filename=None,
            lineno=1,
            offset=self.offset + 1,
            text=self.text,
        )

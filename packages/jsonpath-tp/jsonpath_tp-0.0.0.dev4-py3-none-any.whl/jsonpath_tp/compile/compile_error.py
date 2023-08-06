import os


class JsonpathSyntaxError(SyntaxError):
    __slots__ = (
        "error_message",
        "filename",
        "lineno",
        "offset",
        "text",
    )
    """
        filename
          The name of the file the syntax error occurred in.
        lineno
          Which line number in the file the error occurred in. This is 1-indexed: the first line in the file has a 
          lineno of 1.
        offset
          The column in the line where the error occurred. This is 1-indexed: the first character in the line has an 
          offset of 1.
        text
          The source code text involved in the error.
    """

    def __init__(self,
                 error_message,
                 *,
                 filename,
                 lineno,
                 offset,
                 text
                 ):
        super().__init__(error_message, (filename, lineno, offset, text))
        self.error_message = error_message
        self.filename = filename
        self.lineno = lineno
        self.offset = offset
        self.text = text

    def pretty_error_message(self) -> str:
        marker = '^'
        offset_adjustment = self.offset + 6
        adjusted_marker = marker.rjust(offset_adjustment)
        n = os.linesep
        error_message = f"JsonpathSyntaxError: {self.error_message}{n}{n}path: {self.text}{n}{adjusted_marker}"
        return error_message

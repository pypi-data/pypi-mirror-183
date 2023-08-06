from typing import Callable, Iterator

from treepath import JsonArgTypes, Trace, JsonTypes

from jsonpath_tp.compile.compile import compile_jsonpath
import treepath
from treepath.path.utils.not_set import not_set


def get(
        jsonpath_expression: str,
        data: JsonArgTypes,
        default=not_set,
        store_default=False,
        trace: Callable[[Trace], None] = None,
        globals=None,
        locals=None
) -> JsonTypes:
    """
    Returns the first value in the data that satisfies the path expression.   When no result is found, a
    MatchNotFoundError is raised unless a default value is given, In which case the default value is returned.

    @param jsonpath_expression: The path expression that define the search criteria.
    @param data: The data to search through.  The data must be either a tree structure that adheres to
        https://docs.python.org/3/library/json.html or a Match object from a previous search.
    @param default:  An optional value to return when no result is found.
    @param store_default: An optional boolean to allow all missing parts of the path to be created just in time to
        support the assignment of the default.  By default, store_default is False.
    @param trace: An optional callable to report detail iteration data too.
    @return: The value that satisfies the path expression, else MatchNotFoundError is raised unless default is given.
    @raise MatchNotFoundError:  Raised when no result is found and no default value is given.
    """
    expression = compile_jsonpath(jsonpath_expression, globals=globals, locals=locals)
    return treepath.get(expression, data, default=default, store_default=store_default, trace=trace)


def find(
        jsonpath_expression: str,
        data: JsonArgTypes,
        trace: Callable[[Trace], None] = None,
        globals=None,
        locals=None

) -> Iterator[JsonTypes]:
    """
    Construct a lazy iterator of all values in the data that satisfies the path expression.

    @param jsonpath_expression: The path expression that define the search criteria.
    @param data: The data to search through.  The data must be either a tree structure that adheres to
        https://docs.python.org/3/library/json.html or a Match object from a previous search.
    @param trace: An optional callable to report detail iteration data too.
    @return: A lazy iterator containing all values that satisfies the path expression.
    """
    expression = compile_jsonpath(jsonpath_expression, globals=globals, locals=locals)
    return treepath.find(expression, data, trace=trace)

import builtins


class FunctionResolver:
    __slots__ = (
        "__globals",
        "__locals"
    )

    def __init__(self, globals_=None, locals_=None):
        self.__globals = globals_
        self.__locals = locals_

    def resolve_function(self, function_name: str):
        if self.__locals is not None and function_name in self.__locals:
            function = self.__locals[function_name]
            self.__validate_callable("locals", function_name, function)
        elif self.__globals is not None and function_name in self.__globals:
            function = self.__globals[function_name]
            self.__validate_callable("globals", function_name, function)
        elif hasattr(builtins, function_name):
            function = getattr(builtins, function_name)
            self.__validate_callable("builtins", function_name, function)
        else:
            raise TypeError(
                f"'{function_name}()' cannot be found in locals(), globals() or builtins namespaces.")
        return function

    @staticmethod
    def __validate_callable(source: str, function_name: str, function):
        if not callable(function):
            raise TypeError(f"Found '{function_name}' in '{source}', but it is not callable.  "
                            f"Expecting a single argument function.")

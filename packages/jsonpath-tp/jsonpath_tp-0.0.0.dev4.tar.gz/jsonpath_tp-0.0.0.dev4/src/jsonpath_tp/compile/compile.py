from typing import Optional, Callable, Any

from treepath import path, RootPathBuilder, gwc, has, has_not, has_all, has_any
from treepath.path.builder.path_predicate import PathPredicate
from treepath.path.traverser.match import Match

from jsonpath_tp.compile.function_resolver import FunctionResolver
from jsonpath_tp.compile.regular_expression import build_re_match

"""
   https://www.ietf.org/archive/id/draft-goessner-dispatch-jsonpath-00.html#name-detailed-definition
   https://goessner.net/articles/JsonPath/index.html#e2

   JSONPath = root *(step)
   root = "$"

   step = step_dot_notation
        / step_square_bracket_notation

   step_dot_notation = step_single_dot_notation
                     / step_double_dot_notation
   
   step_double_dot_notation = ".." text
   step_single_dot_notation = "." text ; child (dot notation)
   
   

   step_square_bracket_notation = "[" square_bracket_options "]"

                                
   square_bracket_options = filter_expression
                                / script_expression
                                / quote
                                / wildcard
                                / array_index_expression

   filter_expression = "?(" predicate ")"
   script_expression = "(" script ")"     
   array_index_expression = array_index       
                          / array_slice   
   array_index =       *1DIGIT *("," *1DIGIT)
   array_slice =       *1DIGIT *2(":" *1DIGIT)
     
   quote = "'" text "'"
         / '"' text '"'
   wildcard = '*'        
   script = <To be defined in the course of standardization>
   predicate = <To be defined in the course of standardization>
   text_key = +(ALPHA / DIGIT / "-" / "_" )
   text = any character   
   
              predicate = "(" predicate ")"
                     / not predicate
                     / boolean_expression "and" predicate
                     / boolean_expression "or" predicate
                     / boolean_expression

           boolean_expression = path_expression operator value *("," single_arg_function_name)
                                path_expression *("," single_arg_function_name)


           path_expression = "@" step

           value = quote
                   / DIGIT

"""
from jsonpath_tp.compile.parser import Parser


def compile_jsonpath(jsonpath_text: str, globals=None, locals=None) -> RootPathBuilder:
    parser = Parser(jsonpath_text)
    function_resolver = FunctionResolver(globals_=globals, locals_=locals)
    jsonpath_compiler = JsonpathCompiler(parser=parser, function_resolver=function_resolver)
    resolved_path = jsonpath_compiler.compile()
    return resolved_path


cjp = compile_jsonpath


class JsonpathCompiler:
    __slots__ = (
        "parser",
        "function_resolver"
    )

    def __init__(self, *, parser, function_resolver):
        self.parser = parser
        self.function_resolver = function_resolver

    def compile(self) -> RootPathBuilder:
        try:
            root_path_builder = self.__root()
            root_path_builder = self.__walking_step(root_path_builder)
            if self.parser.has_next():
                char = self.parser.next_none_whitespace_char()
                path_str = str(root_path_builder)
                if path_str.endswith('..'):
                    self.__raise_unexpected_char(char, "'ALPHA-NUMERIC', '[' or nothing")
                else:
                    self.__raise_unexpected_char(char, "'.', '[' or nothing")

            return root_path_builder
        except StopIteration:
            self.parser.raise_jsonpath_systax_error("Unexpected end of line")

    def __root(self) -> RootPathBuilder:
        char = next(self.parser)
        if '$' == char:
            return path
        else:
            self.__raise_unexpected_char(char, "'$'")

    def __try_single_step(self, root_path_builder: RootPathBuilder) -> RootPathBuilder:
        if not self.parser.has_next():
            return root_path_builder
        char = self.parser.next_none_whitespace_char()
        if char == '.':
            path_builder = self.__step_dot_notation(root_path_builder)
        elif char == '[':
            path_builder = self.__step_square_bracket_notation(root_path_builder)
        else:
            self.parser.undo_next()
            path_builder = root_path_builder

        return path_builder

    def __walking_step(self, root_path_builder: RootPathBuilder) -> RootPathBuilder:
        current_path_builder = root_path_builder
        next_path_builder = self.__try_single_step(current_path_builder)
        while current_path_builder is not next_path_builder:
            current_path_builder = next_path_builder
            next_path_builder = self.__try_single_step(current_path_builder)
        return current_path_builder

    def __step_dot_notation(self, root_path_builder: RootPathBuilder) -> RootPathBuilder:
        char = next(self.parser)
        if '.' == char:
            return self.__step_double_dot_notation(root_path_builder)
        else:
            self.parser.undo_next()
            return self.__step_single_dot_notation(root_path_builder)

    def __step_double_dot_notation(self, root_path_builder: RootPathBuilder) -> RootPathBuilder:
        return self.__step_word(root_path_builder.rec, is_raise_unexpected=False)

    def __step_single_dot_notation(self, root_path_builder: RootPathBuilder) -> RootPathBuilder:
        return self.__step_word(root_path_builder)

    def __step_word(self, root_path_builder: RootPathBuilder, is_raise_unexpected=True) -> RootPathBuilder:
        text = self.__text_key()
        if text:
            return root_path_builder[text]

        if not self.parser.has_next():
            return root_path_builder

        char = self.parser.next_none_whitespace_char()
        if char == '*':
            return root_path_builder.wc
        if char == '[':
            return self.__step_square_bracket_notation(root_path_builder)
        elif is_raise_unexpected:
            self.__raise_unexpected_char(char, "'[', '*', 'ALPHA-NUMERIC', '-' or '_'")
        else:
            self.parser.undo_next()
            return root_path_builder

    def __step_square_bracket_notation(self, root_path_builder: RootPathBuilder) -> RootPathBuilder:
        char = self.parser.next_none_whitespace_char()
        augmented_root_path_builder = None
        if char == '?':
            augmented_root_path_builder = self.__filter_expression(root_path_builder)
        elif char == '(':
            self.parser.raise_jsonpath_systax_error("Script expression is not supported.")
        elif char == '"' or char == "'":
            augmented_root_path_builder = self.__quote_expression(root_path_builder)
        elif char == '*':
            augmented_root_path_builder = self.__wildcard(root_path_builder)
        elif char.isdigit() or char == '-' or char == ':':
            self.parser.undo_next()
            augmented_root_path_builder = self.__array_expression(root_path_builder)
        else:
            self.__raise_unexpected_char(char, "'$', '(', '\"', ''', '-' or 'DIGIT'")

        char = self.parser.current_or_next_none_whitespace_char()
        if char != ']':
            self.__raise_unexpected_char(char, "']'")
        return augmented_root_path_builder

    def __quote_expression(self, root_path_builder: RootPathBuilder) -> RootPathBuilder:
        first_text = self.__quote()
        char = self.parser.current_or_next_none_whitespace_char()
        if first_text is not None and char == ']' or char == ',':
            return self.__quote_index(root_path_builder, first_text)
        else:
            self.__raise_unexpected_char(char, "',' or ']'")

    def __quote_index(self, root_path_builder: RootPathBuilder, first_text) -> RootPathBuilder:
        char = self.parser.current_or_next_none_whitespace_char()
        if char == ']':
            return root_path_builder[first_text]

        indices = list()
        indices.append(first_text)
        while char == ',':
            next(self.parser)  # eat the ','
            text = self.__quote()
            char = self.parser.current_or_next_none_whitespace_char()
            indices.append(text)
        return root_path_builder[tuple(indices)]

    def __array_expression(self, root_path_builder: RootPathBuilder) -> RootPathBuilder:
        first_digit = self.__digit()
        char = self.parser.current_or_next_none_whitespace_char()
        if first_digit is not None and char == ']' or char == ',':
            return self.__array_index(root_path_builder, first_digit)
        elif char == ':':
            return self.__array_slice(root_path_builder, first_digit)
        else:
            self.__raise_unexpected_char(char, "',', ':' or ']`")

    def __array_index(self, root_path_builder: RootPathBuilder, first_digit) -> RootPathBuilder:
        char = self.parser.current_or_next_none_whitespace_char()
        if char == ']':
            return root_path_builder[first_digit]

        indices = list()
        indices.append(first_digit)
        while char == ',':
            digit = self.__digit()
            char = self.parser.current_or_next_none_whitespace_char()
            if digit is None:
                self.__raise_unexpected_char(char, "'DIGIT'")
            indices.append(digit)

        return root_path_builder[tuple(indices)]

    def __array_slice(self, root_path_builder: RootPathBuilder, start) -> RootPathBuilder:
        end = None
        step = None
        char = self.parser.current_or_next_none_whitespace_char()
        if char == ':':
            end = self.__digit()
            char = self.parser.current_or_next_none_whitespace_char()
            if char == ':':
                step = self.__digit()
        return root_path_builder[start:end:step]

    def __quote(self) -> str:
        start_quote = self.parser.current_or_next_none_whitespace_char()
        if not (start_quote == '"' or start_quote == "'"):
            self.__raise_unexpected_char(start_quote, "''' or '\"'")
        text = self.__text_quote(start_quote)
        return text

    def __wildcard(self, root_path_builder: RootPathBuilder) -> str:
        next(self.parser)  # eat star
        return root_path_builder[gwc]

    def __filter_expression(self, root_path_builder: RootPathBuilder) -> RootPathBuilder:
        char = next(self.parser)
        augmented_root_path_builder = None
        if char == '(':
            augmented_root_path_builder = root_path_builder[gwc][self.__predicate()]
        else:
            self.__raise_unexpected_char(char, "'('")

        char = self.parser.current_or_next_none_whitespace_char()
        if char != ')':
            self.__raise_unexpected_char(char, "')'")

        next(self.parser)  # eat )

        return augmented_root_path_builder

    def __predicate(self, is_not=False, is_and=False, is_or=False) -> Callable[[Match], Any]:
        python_word = self.__python_word()
        char = self.parser.next_none_whitespace_char()
        left_predicate = None
        if python_word == 'not':
            self.parser.undo_next()
            left_predicate = has_not(self.__predicate(is_not=True))
        elif python_word:
            left_predicate = self.__function_expression(python_word)
        elif char == '@':
            left_predicate = self.__boolean_expression()
        elif char == '(':
            left_predicate = self.__predicate_tuple()
        else:
            self.__raise_unexpected_char(char, "'@', 'not' or '('")

        char = self.parser.current_or_next_none_whitespace_char()
        if not is_not and not is_and and not is_or and char == 'o':
            return self.__or_predicate(left_predicate, is_and=is_and)
        elif not is_not and not is_and and char == 'a':
            left_predicate = self.__and_predicate(left_predicate, is_or=is_or)
            char = self.parser.current_or_next_none_whitespace_char()
            if not is_or and char == 'o':
                return self.__or_predicate(left_predicate, is_and=is_and)
            else:
                return left_predicate
        else:
            return left_predicate

    def __and_predicate(self, left_predicate, is_or=False):
        self.__assert_string('nd')
        right_predicate = self.__predicate(is_and=True, is_or=is_or)
        char = self.parser.current_or_next_none_whitespace_char()
        if char != 'a':
            return has_all(left_predicate, right_predicate)

        predicates = [left_predicate, right_predicate]
        while char == 'a':
            self.__assert_string('nd')
            next_predicate = self.__predicate(is_and=True, is_or=is_or)
            predicates.append(next_predicate)
            char = self.parser.current_or_next_none_whitespace_char()

        return has_all(*predicates)

    def __or_predicate(self, left_predicate, is_and=False):
        self.__assert_string('r')
        right_predicate = self.__predicate(is_and=is_and, is_or=True)
        char = self.parser.current_or_next_none_whitespace_char()
        if char != 'o':
            return has_any(left_predicate, right_predicate)

        predicates = [left_predicate, right_predicate]
        while char == 'o':
            self.__assert_string('r')
            next_predicate = self.__predicate(is_and=is_and, is_or=True)
            predicates.append(next_predicate)
            char = self.parser.current_or_next_none_whitespace_char()

        return has_any(*predicates)

    def __predicate_tuple(self) -> Callable[[Match], Any]:
        predicate = self.__predicate()

        char = self.parser.current_or_next_none_whitespace_char()
        if char != ')':
            self.__raise_unexpected_char(char, "')'")

        next(self.parser)  # eat )

        return predicate

    def __function_expression(self, function_name) -> Callable[[Any], Any]:
        char = self.parser.current()
        if char != '(':
            self.__raise_unexpected_char(char, "'('")

        function = None
        try:
            function = self.function_resolver.resolve_function(function_name)
        except TypeError as te:
            self.parser.raise_jsonpath_systax_error(str(te))

        char = self.parser.next_none_whitespace_char()
        if char != '@':
            self.__raise_unexpected_char(char, "'@'")

        path_expression = self.__try_single_step(path)

        char = self.parser.next_none_whitespace_char()
        if char != ')':
            self.__raise_unexpected_char(char, "')'")

        return self.__right_side_boolean_expression(path_expression, function=function)

    def __boolean_expression(self) -> Callable[[Match], Any]:
        path_expression = self.__walking_step(path)
        return self.__right_side_boolean_expression(path_expression)

    def __right_side_boolean_expression(self, path_expression, function=None) -> Callable[[Match], Any]:
        char = self.parser.next_none_whitespace_char()
        if char == ')':
            pass
        elif char == '<':
            char = next(self.parser)
            if char == '=':
                value = self.__value()
                path_expression = path_expression <= value
            else:
                self.parser.undo_next()
                value = self.__value()
                path_expression = path_expression < value
        elif char == '=':
            char = next(self.parser)
            if char == '~':
                next(self.parser)  # eat '~'
                operator_function = self.__regex()
                path_expression = PathPredicate(path_expression, operator_function)
            elif char == '=':
                value = self.__value()
                path_expression = path_expression == value
            else:
                self.__raise_unexpected_char(char, "'=' or '~'")
        elif char == '!':
            char = next(self.parser)
            if char != '=':
                self.__raise_unexpected_char(char, "'='")
            value = self.__value()
            path_expression = path_expression != value
        elif char == '>':
            char = next(self.parser)
            if char == '=':
                value = self.__value()
                path_expression = path_expression >= value
            else:
                self.parser.undo_next()
                value = self.__value()
                path_expression = path_expression > value
        elif char == 'a':
            pass
        elif char == 'o':
            pass
        else:
            self.__raise_unexpected_char(char, " ')', ',', '<', '<=', '==','!=','>', '>=', 'and' or 'or")

        if function:
            return has(path_expression, function)
        else:
            return has(path_expression)

    def __value(self):
        char = self.parser.next_none_whitespace_char()
        value = None
        if char == '"' or char == "'":
            value = self.__text_quote(char)
        elif char.isdigit() or char == '-':
            self.parser.undo_next()
            value = self.__digit()
        else:
            self.__raise_unexpected_char(char, "'\"', ''', '-' or 'DIGIT'")
        return value

    def __text_key(self) -> str:
        if not self.parser.has_next():
            return ''

        char = next(self.parser)
        start_offset = self.parser.offset
        try:
            while char.isalnum() or char in '-_':
                char = next(self.parser)
        except StopIteration:
            pass
        text = self.parser.text[start_offset:self.parser.offset]
        self.parser.undo_next()  # The last char is for the next token
        return text

    def __text_quote(self, not_char) -> str:
        text_list = list()
        char = next(self.parser)
        while char != not_char:
            if char == '\\':
                next_char = next(self.parser)
                if next_char == not_char:
                    char = next_char
                else:
                    self.parser.undo_next()
            text_list.append(char)
            char = next(self.parser)
        next(self.parser)  # eat the not_char
        return "".join([char for char in text_list])

    def __digit(self) -> Optional[int]:
        char = self.parser.next_none_whitespace_char()
        start_offset = self.parser.offset
        if char == '-':
            char = next(self.parser)

        while char.isdigit():
            char = next(self.parser)

        digit_str = self.parser.text[start_offset:self.parser.offset]
        if len(digit_str) == 0:
            return None
        if digit_str == '-':
            self.__raise_unexpected_char(char, "'DIGIT'")
        digit = int(digit_str)
        return digit

    def __python_word(self):
        char = self.parser.next_none_whitespace_char()
        start_offset = self.parser.offset
        text = None
        if char.isalpha() or char in '_':
            while char.isalnum() or char in '_':
                char = next(self.parser)
            text = self.parser.text[start_offset:self.parser.offset]
        self.parser.undo_next()
        return text

    def __regex(self) -> str:
        start_quote = self.parser.current_or_next_none_whitespace_char()
        regex = self.__quote()
        re_match = build_re_match(regex, start_quote)
        return re_match

    def __assert_string(self, text):
        for expected_char in text:
            actual_char = next(self.parser)
            if actual_char != expected_char:
                self.__raise_unexpected_char(actual_char, f"'{expected_char}'")

    def __raise_unexpected_char(self, unexpected_char, expected):
        self.parser.raise_jsonpath_systax_error(f"Unexpected char: '{unexpected_char}', expecting: {expected}")

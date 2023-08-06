import re

from treepath.path.utils.decorator import pretty_repr


def build_re_match(regex: str, quote) -> re.match:
    re_match = re.compile(regex).match
    pretty = pretty_repr(lambda: f"=~ {quote}{regex}{quote}")
    return pretty(re_match)

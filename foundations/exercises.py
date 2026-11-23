"""Python Foundations: fill the TODOs, then run python foundations/check.py.
No external dependencies needed except optional torch for the last exercise.
Do not edit the tests to make them pass.
"""

def reverse_word(word: str) -> str:
    """Return word with characters reversed using slicing."""
    # TODO: use [start:stop:step]
    raise NotImplementedError


def make_slots(n: int) -> list:
    """Create a list of length n containing None in every position."""
    # TODO
    raise NotImplementedError


def make_matrix(rows: int, cols: int) -> list[list[int]]:
    """Create independent rows, each containing cols zeros."""
    # TODO: do not alias inner mutable lists
    raise NotImplementedError


class Counter:
    """Each instance stores its OWN count, initially zero."""

    def __init__(self):
        # TODO: initialize an instance attribute
        raise NotImplementedError

    def increment(self):
        # TODO: increment that instance attribute
        raise NotImplementedError


def get_or_zero(seen: dict, key: str):
    """Get an existing value, or zero, WITHOUT inserting a new key."""
    # TODO: dict.get
    raise NotImplementedError


def pair_up(a: list, b: list) -> list[tuple]:
    """Pair items at the same index; stop at shorter input."""
    # TODO: zip
    raise NotImplementedError


def reverse_list(values: list) -> list:
    """Return a new reversed list; original unchanged."""
    # TODO: reversed, then list
    raise NotImplementedError


def sort_by_second(pairs: list[tuple]) -> list[tuple]:
    """Return a NEW list sorted by the second field in each pair."""
    # TODO: sorted(..., key=lambda ...)
    raise NotImplementedError


def normalize_words(text: str) -> str:
    """Lowercase words and join them with '-'; collapse extra whitespace."""
    # example: " Hello   Python WORLD " -> "hello-python-world"
    # TODO: lower, split, join
    raise NotImplementedError


def format_state(i: int, j: int) -> str:
    """Return exactly 'i=1, j=3' when i=1 and j=3."""
    # TODO: f-string; must RETURN, not print
    raise NotImplementedError


def last_token(x):
    """For a Torch tensor of shape (B,T,D), return shape (B,D)."""
    # TODO: x[:, ?, :]
    raise NotImplementedError


def keep_last_token_axis(x):
    """For a Torch tensor of shape (B,T,D), return shape (B,1,D)."""
    # TODO: slice, not integer index
    raise NotImplementedError

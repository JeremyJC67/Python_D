"""Reference solutions. Only open AFTER an independent attempt and debugging.

These are examples, not unique answers.
"""

def reverse_word(word: str) -> str:
    return word[::-1]

def make_slots(n: int) -> list:
    return [None] * n

def make_matrix(rows: int, cols: int) -> list[list[int]]:
    return [[0] * cols for _ in range(rows)]

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

def get_or_zero(seen: dict, key: str):
    return seen.get(key, 0)

def pair_up(a: list, b: list) -> list[tuple]:
    return list(zip(a, b))

def reverse_list(values: list) -> list:
    return list(reversed(values))

def sort_by_second(pairs: list[tuple]) -> list[tuple]:
    return sorted(pairs, key=lambda item: item[1])

def normalize_words(text: str) -> str:
    return "-".join(text.lower().split())

def format_state(i: int, j: int) -> str:
    return f"i={i}, j={j}"

def last_token(x):
    return x[:, -1, :]

def keep_last_token_axis(x):
    return x[:, -1:, :]


if __name__ == "__main__":
    assert reverse_word("python") == "nohtyp"
    assert make_slots(2) == [None, None]
    m = make_matrix(2, 2)
    m[0][0] = 1
    assert m[1][0] == 0
    a = Counter()
    b = Counter()
    a.increment()
    assert (a.count, b.count) == (1, 0)
    assert get_or_zero({}, "absent") == 0
    assert pair_up([1, 2], ["a"]) == [(1, "a")]
    assert reverse_list([1, 2]) == [2, 1]
    assert sort_by_second([(9, 3), (2, 1)]) == [(2, 1), (9, 3)]
    assert normalize_words(" A  b ") == "a-b"
    assert format_state(1, 3) == "i=1, j=3"
    print("Reference Python tests passed")
    try:
        import torch
    except ImportError:
        print("torch not installed: skipped optional Tensor tests")
    else:
        x = torch.randn(2, 5, 32)
        assert last_token(x).shape == (2, 32)
        assert keep_last_token_axis(x).shape == (2, 1, 32)
        print("Reference Tensor tests passed")

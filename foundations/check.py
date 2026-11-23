"""Run from repository root: python foundations/check.py
Exercises are deliberately incomplete until YOU fill their TODOs.
Tests run independently, reporting all failures rather than stopping at first one.
"""

import exercises as ex

def test_reverse_word():
    assert ex.reverse_word("python") == "nohtyp"
    assert ex.reverse_word("") == ""

def test_make_slots():
    assert ex.make_slots(3) == [None, None, None]
    assert ex.make_slots(0) == []

def test_make_matrix():
    m = ex.make_matrix(2, 3)
    assert m == [[0, 0, 0], [0, 0, 0]]
    m[0][0] = 9
    assert m[1][0] == 0, "BUG: inner rows are aliased!"

def test_counter():
    a = ex.Counter()
    b = ex.Counter()
    a.increment()
    a.increment()
    b.increment()
    assert (a.count, b.count) == (2, 1)

def test_get_or_zero():
    data = {"apple": 4}
    assert ex.get_or_zero(data, "apple") == 4
    assert ex.get_or_zero(data, "banana") == 0
    assert "banana" not in data, "dict.get should not insert missing keys"

def test_pair_up():
    assert ex.pair_up([1, 2, 3], ["a", "b"]) == [(1, "a"), (2, "b")]

def test_reverse_list():
    values = [4, 5, 6]
    assert ex.reverse_list(values) == [6, 5, 4]
    assert values == [4, 5, 6], "Must not mutate the input"

def test_sort_by_second():
    pairs = [(1, 5), (3, 2), (2, 8)]
    assert ex.sort_by_second(pairs) == [(3, 2), (1, 5), (2, 8)]
    assert pairs == [(1, 5), (3, 2), (2, 8)], "Must not mutate input"

def test_normalize_words():
    assert ex.normalize_words(" Hello   Python WORLD ") == "hello-python-world"
    assert ex.normalize_words("") == ""

def test_format_state():
    assert ex.format_state(1, 3) == "i=1, j=3"

def test_tensor():
    try:
        import torch
    except ImportError:
        print("SKIP tensor tests (install torch to enable)")
        return
    x = torch.randn(2, 5, 32)
    assert ex.last_token(x).shape == (2, 32)
    assert ex.keep_last_token_axis(x).shape == (2, 1, 32)
    assert torch.equal(ex.last_token(x), x[:, 4, :])

TESTS = [
    test_reverse_word,
    test_make_slots,
    test_make_matrix,
    test_counter,
    test_get_or_zero,
    test_pair_up,
    test_reverse_list,
    test_sort_by_second,
    test_normalize_words,
    test_format_state,
    test_tensor,
]

if __name__ == "__main__":
    failures = 0
    for test in TESTS:
        try:
            test()
            print(f"PASS {test.__name__}")
        except Exception as error:
            failures += 1
            print(f"FAIL {test.__name__}: {type(error).__name__}: {error}")
    print(f"\n{len(TESTS) - failures}/{len(TESTS)} passed")
    if failures:
        raise SystemExit(1)

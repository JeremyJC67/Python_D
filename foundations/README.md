# Python Foundations: one-pass guide (中文 + English terms)

Goal: develop Python language fluency for LeetCode Top 150, ML coding and research implementations. **Reading this guide does not count as passing an exercise.** Study once, then code without looking and test your work.

## 1. Slicing and reversing

Syntax: sequence[start:stop:step]. The stop is excluded. A negative step walks backward; omitted start/stop use direction-appropriate defaults.

~~~python
word = "python"
assert word[1:4] == "yth"
assert word[::2] == "pto"
assert word[::-1] == "nohtyp"
assert word[5:1:-1] == "noht"
nums = [10, 20, 30]
assert nums[::-1] == [30, 20, 10]
~~~

word[::-1] is **not** an in-place mutation. For reversed iteration without first making a reversed list, use reversed(nums). To materialize its elements: list(reversed(nums)).

## 2. Create a list of a known size

~~~python
n = 5
slots = [None] * n          # placeholders
zeros = [0] * n             # numeric defaults
empty = []                  # length 0, NOT length n
matrix = [[0] * 4 for _ in range(3)]  # independent rows
~~~

Avoid matrix = [[0] * 4] * 3 for mutable rows: all three rows refer to the same inner list. If you need genuine random numbers, use random.randint inside a comprehension. PyTorch alternatives: torch.zeros(shape), torch.randn(shape), torch.empty(shape). torch.empty allocates uninitialized storage, not meaningful random data.

## 3. Classes, self, instance attributes, and C++ parallels

~~~python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        count = 100        # local variable for this call
        self.count += 1    # persistent instance attribute

a = Counter()
b = Counter()
a.increment()
a.increment()
b.increment()
assert (a.count, b.count) == (2, 1)
~~~

* Counter = class; a and b = separate instances.
* self means the instance whose method is running; a.increment() is approximately Counter.increment(a).
* self.count is similar to C++ this->count; a bare count is a local name when assigned inside a method.
* __init__ initializes an instance. Strictly, __new__ is responsible for creation. __init__ is **not private**.
* Python has no C++-style enforced public/private sections. name is normally public; _name is a non-public convention; __name uses name mangling (not absolute privacy).
* For methods, the first argument is conventionally named self; Python passes it automatically for an instance method call.

## 4. PyTorch: inheritance versus composition

~~~python
import torch
from torch import nn

class MyModel(nn.Module):           # inheritance: MyModel IS an nn.Module
    def __init__(self):
        super().__init__()          # initialize base Module
        self.linear = nn.Linear(32, 32)  # composition: own a Linear layer

    def forward(self, x):
        return self.linear(x)       # apply layer to actual tensor

model = MyModel()
y = model(torch.randn(2, 32))
assert y.shape == (2, 32)
~~~

The constructor nn.Linear(32, 32) specifies feature dimensions and creates trainable parameters. self.linear(x) applies the already-created layer to data. MyModel does not inherit from nn.Linear: it **contains** an nn.Linear submodule. nn.Module registers submodule parameters and calling model(x) dispatches through Module.__call__ to forward.

## 5. dict.get and bracket lookup

~~~python
seen = {"apple": 3}
assert seen.get("apple", 0) == 3
assert seen.get("banana", 0) == 0
assert "banana" not in seen       # get does not insert the key
assert seen["apple"] == 3
# seen["banana"] would raise KeyError
~~~

dictionary.get(key, default) returns the value if the key exists, otherwise default (None if omitted). A present key with value None returns None, not default.

## 6. APIs: zip, sorted, reversed, strings

~~~python
a = [1, 2, 3]
b = ["a", "b"]
assert list(zip(a, b)) == [(1, "a"), (2, "b")]  # stops at shorter input

nums = [3, 1, 2]
new_nums = sorted(nums)     # new list, original nums unchanged
assert new_nums == [1, 2, 3]
assert nums == [3, 1, 2]
nums.sort()                 # sorts list in place, returns None
assert nums == [1, 2, 3]

assert list(reversed(nums)) == [3, 2, 1]  # reversed() is an iterator
assert nums[::-1] == [3, 2, 1]            # slicing creates new list

assert "ABC".lower() == "abc"
assert "a1".isalnum()
assert not "! ".isalnum()
assert "a   b".split() == ["a", "b"]       # default: whitespace
assert "a,b".split(",") == ["a", "b"]
assert "-".join(["a", "b"]) == "a-b"
~~~

split is a string method that produces a list. join is called on the separator string and takes an iterable of strings; it does not accept integers unless converted first.

## 7. sorted(..., key=lambda ...)

~~~python
pairs = [(1, 5), (3, 2), (2, 8)]

def second(item):
    return item[1]                 # tuple's second element

assert sorted(pairs, key=second) == [(3, 2), (1, 5), (2, 8)]
assert sorted(pairs, key=lambda item: item[1]) == [(3, 2), (1, 5), (2, 8)]
~~~

lambda item: item[1] is an unnamed function: input item -> return item[1]. sorted calls this function for each pair and sorts by its returned key, not by the whole tuple. Other options: reverse=True for descending order; pairs.sort(key=...) for in-place sorting.

## 8. Tensor indexing: x[:, -1, :]

For x.shape == (B, T, D) == (2, 5, 32):
* axis 0: batch; : = ALL batches;
* axis 1: sequence; -1 = LAST token position (not reversal);
* axis 2: hidden features; : = ALL features.

~~~python
import torch
x = torch.randn(2, 5, 32)
assert x[:, -1, :].shape == (2, 32)   # indexing by integer removes T axis
assert x[:, -1:, :].shape == (2, 1, 32)  # slice preserves T axis
assert x[:, :, -1].shape == (2, 5)    # last hidden feature at ALL times
assert x.flip(dims=[1]).shape == (2, 5, 32)  # actually reverse sequence axis
~~~

Do not confuse -1 (last index) with ::-1 (negative slice step). PyTorch tensor slicing does not necessarily support negative steps; use torch.flip when reversing.

## 9. Print, return and debugging

~~~python
i, j = 1, 3
print(i, j)                          # prints two values
print([i, j])                        # displays a list
print(f"i={i}, j={j}")               # formatted string, not list
print(f"token={str(' ')!r}")          # repr shows invisible whitespace
~~~

print() writes to stdout and returns None. return ends a function and sends a value back to caller. To debug: choose minimal failing input, print relevant state BEFORE changes, compare expected/actual, change ONE cause, add assertions, rerun.

Use experiments as small, controlled tests. These same habits transfer to ML coding, tensor shapes, and test-time RL research.

## 10. Exercises and review protocol

1. Fill TODOs in exercises.py WITHOUT opening solutions.py.
2. Run: python foundations/check.py (from repository root).
3. Fix errors using traceback and print; rerun until all tests pass.
4. Compare with solutions.py only afterward.
5. Repeat difficult tasks from a blank file after 1, 3 and 7 days; track actual attempts in REVIEW_LOG.md.

Training map: Python foundations 15-20 min/day; LeetCode Top 150 ~1 task/day when possible; ML coding 3x/week; retain independent deep-work blocks for TTRL. No task is considered completed before an independently executed correct solution.

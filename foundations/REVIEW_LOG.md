# Python Foundations: review log

Use this as a real progress record. **No exercises are marked complete until independently solved and tested.**

## Review checkpoints

| Date | Exercise | Independent? | Passed tests? | Mistake category | Next review |
|---|---|---|---|---|---|
| YYYY-MM-DD | reverse_word | no | no | slicing | YYYY-MM-DD |

Review after 1, 3, and 7 days for concepts that caused errors. If a problem was solved only after looking at solutions.py, mark Independent? = no and retry it later from scratch.

## Typical mistake categories

- Brackets: [] list/index/slice, () function call, {} dict/set/f-string
- Names: reserved keyword, overwritten built-in (len, list, sum), variable naming
- Scope: local variable versus self.attribute
- Control: if/for/while; break/continue/return
- Iterators: zip/reversed are iterables, not automatically materialized lists
- Mutation: list.sort modifies while sorted makes a new list; nested-list aliases
- Tensor dimensions: axis index versus reversing, integer index removes dimension
- Debugging: mismatch between expected value, printed state and actual return

## Daily 20-minute practice

1. 3 minutes: translate one Chinese requirement into Python syntax.
2. 10 minutes: fill 1-2 tasks in exercises.py **without reference solutions**.
3. 5 minutes: run check.py, debug failures with print/type/shape/assert.
4. 2 minutes: write error category and the corrected one-line pattern here.

## Parallel tracks

- LeetCode Top Interview 150: focus on independent implementation, not count.
- ML Coding (3 sessions/week): tensor indexing, stable softmax, sampling, gradient/autograd, training loop.
- TTRL research: separate uninterrupted deep-work blocks. Do not treat reading code as equivalent to independently implementing it.

## Next independent challenges

- Two Sum II: two pointers on sorted array; produce 1-based indices.
- Is Subsequence: why a scan pointer in t must never reset.
- Top-K Sampling: sorted/ranked logits, numeric stability, sampling, edge cases.
- PyTorch: implement a tiny nn.Module containing nn.Linear, then inspect forward shapes.

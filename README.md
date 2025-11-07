simple-aoc-template
===================

A simple template for solving advent of code with python.

To get started add your session cookie to `src/aoc/data/session.txt`.
Then run:

```
pip install -e .
```

Say your solving the puzzle for day 2 of 2024. Then
copy the `template.py` into `src/aoc/year_2024/day_2.py`
and replace the `data = get_input(day=..., year=...)` with
`data = get_input(day=2, year=2024)`.

Then run
```
./rerun python src/aoc/year_2024/day_2.py
```

To repeatedly run your script whenever you edit it.

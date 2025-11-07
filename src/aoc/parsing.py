import re


def nums(txt: str) -> list[float | int]:
    """
    >>> nums("game 1: 3")
    [1.0, 3.0]
    >>> nums("hello +1: -5 blue")
    [1.0, -5.0]
    """

    def intorfloat(x: str) -> int | float:
        try:
            return int(x)
        except Exception:
            return float(x)

    return list(map(intorfloat, re.findall(r"(?:[-+]?[0-9]+(?:\.[0-9]*)?)", txt)))

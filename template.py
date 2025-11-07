import math
from collections import Counter, defaultdict, deque
import heapq
from dataclasses import dataclass
from enum import Enum
from time import sleep
import re

import numpy as np

from aoc import get_input
from aoc.parsing import nums
from aoc.complex_grid import Grid, directions

data = get_input(day=..., year=...)
data = data.splitlines()

s = 0
for i in range(len(data)):
    line = data[i]
    s += 1
print(s)

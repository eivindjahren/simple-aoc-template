import warnings
from collections import deque
from collections import UserDict


directions = [1, 1j, -1, -1j, 1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j]


class Grid(UserDict):
    def __init__(self, data: str, border=None):
        super().__init__()
        lines = data.splitlines()
        self.n = len(lines)
        self.m = len(lines[-1])
        if border:
            self[-1 - 1j] = border
            self[self.n + self.m * 1j] = border
        for i in range(self.n):
            line = lines[i]
            if len(line) != self.m:
                warnings.warn("Not rectangular")
            if border:
                self[i - 1j] = border
                self[i + len(line) * 1j] = border
            for j in range(len(line)):
                c = line[j]
                self[i + j * 1j] = c

        if border:
            for j in range(self.m):
                self[-1 + j * 1j] = border
                self[self.n + j * 1j] = border

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            for j in range(0, self.m):
                s += str(self.get(i + j * 1j, "."))
            s += "\n"
        s += "\n"
        return s

    def bfs(
        self,
        start=(0, 0),
        starts=None,
        wall=("#",),
        directions=(1, 1j, -1j, -1),
        allowed=lambda *_: True,
        visited=None,
    ):
        if starts is not None:
            queue = deque([(s, 0) for s in starts])
        else:
            queue = deque([(start, 0)])
        if visited is None:
            visited = dict()
        while queue:
            node, steps = queue.popleft()
            if node in visited or node not in self or self[node] in wall:
                continue
            visited[node] = steps
            for d in directions:
                next_node = node + d
                if next_node in self and allowed(node, next_node, steps):
                    queue.append((next_node, steps + 1))
        return visited

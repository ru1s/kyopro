class UnionFind:

    def __init__(self, n : int) -> None:
        self.n = n
        self.cnt = n
        self.rank = [0]*n
        self.sizes = [1]*n
        self.parents = [i for i in range(n)]

    def find(self, x : int) -> int:
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x : int, y : int) -> None:
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parents[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.cnt -= 1
        self.sizes[rx] += self.sizes[ry]
        return
    
    def same(self, x : int, y : int) -> bool:
        return self.find(x) == self.find(y)
    
    def count(self) -> int:
        return self.cnt
    
    def size(self, x : int) -> int:
        return self.sizes[self.find(x)]
    
    def search(self) -> dict:
        res = {}
        for i in range(self.n):
            res.setdefault(self.find(i), []).append(i)
        return res
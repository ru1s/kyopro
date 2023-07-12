class UnionFind:

    def __init__(self, n : int) -> None:
        self.n = n
        self.cnt = n
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
        if rx != ry:
            self.parents[ry] = rx
            self.cnt -= 1
        return
    
    def same(self, x : int, y : int) -> bool:
        return self.find(x) == self.find(y)
    
    def serch(self) -> dict:
        tmp = {}
        for i in range(self.n):
            tmp.setdefault(self.find(i), []).append(i)
        return tmp

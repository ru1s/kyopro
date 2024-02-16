from bisect import bisect_right

class MergeSegmentTree:

    def __init__(self, default_list : list):
        list_len = len(default_list)
        self.N = list_len
        self.a = [[] for _ in range(self.N)] + [[x] for x in default_list]
        self.asum = [[] for _ in range(self.N)] + [[x] for x in default_list]
        for i in range(list_len-1, 0, -1):
            l1, l2 = 0, 0
            while l1 < len(self.a[i<<1]) and l2 < len(self.a[(i<<1)+1]):
                if self.a[i<<1][l1] < self.a[(i<<1)+1][l2]:
                    self.a[i].append(self.a[i<<1][l1])
                    l1 += 1
                else:
                    self.a[i].append(self.a[(i<<1)+1][l2])
                    l2 += 1
            while l1 < len(self.a[i<<1]):
                self.a[i].append(self.a[i<<1][l1])
                l1 += 1
            while l2 < len(self.a[(i<<1)+1]):
                self.a[i].append(self.a[(i<<1)+1][l2])
                l2 += 1
            
            s = 0
            for j in range(len(self.a[i])):
                s += self.a[i][j]
                self.asum[i].append(s)
        

    def sumK(self, k : int, lb : int, rb : int):
        res = 0
        lb += self.N
        rb += self.N
        while lb < rb:
            if lb & 1:
                idx = bisect_right(self.a[lb], k)
                if idx:
                    res += self.asum[lb][idx-1]
                lb += 1
            if rb & 1:
                idx = bisect_right(self.a[rb-1], k)
                if idx:
                    res += self.asum[rb-1][idx-1]
            lb >>= 1
            rb >>= 1
        return res


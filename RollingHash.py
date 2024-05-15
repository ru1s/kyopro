class RollingHash:
    def __init__(self, base1 = 10007, base2 = 1009, mod = 10**9+7):
        self.mod = mod
        self.base1 = base1
        self.base1_rev = pow(base1, mod-2, mod)
        self.base2 = base2
        self.base2_rev = pow(base2, mod-2, mod)

    def append(self, hash : tuple, c : str):
        res1 = (hash[0]*self.base1 + ord(c)) % self.mod
        res2 = (hash[1]*self.base2 + ord(c)) % self.mod
        return (res1, res2, hash[-1]+1)
    
    def appendleft(self, hash : tuple, c : str):
        res1 = (hash[0]*pow(self.base1, hash[-1], self.mod) + ord(c)) % self.mod
        res2 = (hash[1]*pow(self.base2, hash[-1], self.mod) + ord(c)) % self.mod
        return (res1, res2, hash[-1]+1)

    def extend(self, hash : tuple, s : str):
        for c in s:
            hash = self.append(hash, c)
        return hash
    
    def merge(self, hash1 : tuple, hash2 : tuple):
        res1 = (hash1[0]*pow(self.base1, hash2[-1], self.mod) + hash2[0]) % self.mod
        res2 = (hash1[1]*pow(self.base2, hash2[-1], self.mod) + hash2[1]) % self.mod
        return (res1, res2, hash1[-1] + hash2[-1])
    
    def pop(self, hash : tuple, c : str):
        res1 = (hash[0] - ord(c))*self.base1_rev % self.mod
        res2 = (hash[1] - ord(c))*self.base2_rev % self.mod
        return (res1, res2, hash[-1]-1)
    
    def popleft(self, hash : tuple, c : str):
        res1 = (hash[0] - ord(c)*pow(self.base1, hash[-1]-1, self.mod)) % self.mod
        res2 = (hash[1] - ord(c)*pow(self.base2, hash[-1]-1, self.mod)) % self.mod
        return (res1, res2, hash[-1]-1)
    
    def get_hash(self, s : str):
        res = (0, 0, 0)
        for c in s:
            res = self.append(res, c)
        return res
    
    def squeeze(self, hash : tuple):
        return hash[0]*self.mod + hash[1]
class Segment_Tree:

    def __init__(self, default_list : list, element : int = -10**18, tree_type = max):
        list_len = len(default_list)
        self.element = element
        self.N = list_len
        self.function = tree_type
        self.a = [0]*list_len + default_list
        for i in range(list_len-1, 0, -1):
            self.a[i] = self.function(self.a[i<<1], self.a[(i<<1)+1])
        
    def set(self, ind, val):
        ind += self.N
        self.a[ind] = val
        while ind > 1:
            self.a[ind>>1] = self.function(self.a[ind], self.a[ind^1])
            ind >>= 1
        
    def update(self, ind, val):
        ind += self.N
        self.a[ind] = self.function(self.a[ind], val)
        while ind > 1:
            self.a[ind>>1] = self.function(self.a[ind], self.a[ind^1])
            ind >>= 1

    def get(self, lb : int, rb : int):
        lb += self.N
        rb += self.N
        ans = self.element
        while lb < rb:
            if lb & 1:
                ans = self.function(ans, self.a[lb])
                lb += 1
            if rb & 1:
                ans = self.function(ans, self.a[rb-1])
            lb >>= 1
            rb >>= 1
        return ans
    
    def get_val(self, ind):
        return self.a[ind+self.N]
    
    def get_list(self):
        return self.a[self.N:]
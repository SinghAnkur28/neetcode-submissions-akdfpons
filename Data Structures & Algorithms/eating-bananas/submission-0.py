class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        res = max(piles)
        l, r = 1, res        
        arr = [0]*len(piles)
        k = 0
        # if h == len(piles):
        #     return max(piles)
        while l<=r:
            m = (l+r)//2
            for i in range(len(arr)):
                arr[i] = math.ceil(piles[i]/m)

            t = sum(arr)
            if t<=h:
                res = m
                r = m-1
            elif t>h:
                l = m+1

        return res
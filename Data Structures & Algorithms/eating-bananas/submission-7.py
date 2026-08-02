class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        
        while l<r:
            m = (l+r)//2
            t = 0

            for i in range(len(piles)):
                t += math.ceil(piles[i]/m)

            # if t==h:
            #     return m
            if t<=h:
                r = m
            else:
                l = m+1
        return l

        
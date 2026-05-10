class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        l,r = 1, res

        while l<r:
            m = (r+l)//2

            t = sum(math.ceil(a/m) for a in piles)

            if t<=h:
                r = m
                res = m
            elif t>h:
                l = m+1

        return res        
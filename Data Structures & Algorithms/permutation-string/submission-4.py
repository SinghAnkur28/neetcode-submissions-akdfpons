class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        hm1 = {}
        hm2 = {}
        for i in range(len(s1)):
            hm1[s1[i]] = 1 + hm1.get(s1[i],0)

        

        l = 0
        for r in range(len(s2)):
            hm2[s2[r]] = 1 + hm2.get(s2[r], 0)
                
            if r-l+1 > len(s1):
                hm2[s2[l]] -= 1
                if hm2[s2[l]] == 0:
                    del hm2[s2[l]]
                l += 1
            
            if r-l+1 == len(s1):
                if hm1 == hm2:
                    return True
            
        return False



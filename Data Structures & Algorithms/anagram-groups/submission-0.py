class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hm = {}

        for s in strs:
            count = [0] * 26
            for i in s:
                count[(ord(i) - ord("a"))] += 1
                
            if(tuple(count) not in hm):
                hm[tuple(count)] = []
            
            hm[tuple(count)].append(s)

        return(hm.values())
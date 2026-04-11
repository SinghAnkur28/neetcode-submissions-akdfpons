class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = {}
        word2 = {}

        if len(s) != len(t):
            return False

        for i,j in zip(s,t):
            if i in word1:
                word1[i] += 1
            if j in word2:
                word2[j] += 1
            if j not in word2:
                word2[j] = 1
            if i not in word1:
                word1[i] = 1

        return (word1 == word2)

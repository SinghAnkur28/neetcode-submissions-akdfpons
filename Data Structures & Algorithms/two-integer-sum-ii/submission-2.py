class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        L, R = 0, len(numbers)-1
        ch = 0
        while L<=R:
            ch = numbers[L] + numbers[R]
            if ch < target:
                L += 1
            elif ch > target:
                R -= 1
            elif ch == target:
                return [L+1,R+1]

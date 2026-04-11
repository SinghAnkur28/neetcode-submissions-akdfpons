class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i in range(len(nums)):
            a = (target - nums[i])
            if a in hm:
                return(hm.get(a), i)
            else:
                hm[nums[i]] = i

        
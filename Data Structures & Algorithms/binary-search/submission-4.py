class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        l = 0
        r = len(nums)-1

        while r>=l:
            mid = l + ((r-l) // 2)
            num = nums[mid]
            if num == target:
                return mid
            elif num > target:
                r = mid-1
            else:
                l = mid+1

        return -1

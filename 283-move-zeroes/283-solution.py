from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        # """
        i, j = 0, 0
        length = len(nums)
        while i < length:
            # find zero
            while i < length and nums[i] != 0:
                i += 1

            # find next non zero
            # j = i
            while j < length and nums[j] == 0:
                j += 1

            if i < length and j < length:
                # swap them
                nums[i], nums[j] = nums[j], nums[i]

            i += 1


nums = [0,1,0,3,12]
Solution().moveZeroes(nums)


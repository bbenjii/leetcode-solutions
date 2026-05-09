from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = float('inf')
        min2 = float('inf')

        for index, number in enumerate(nums):
            if number <= min1:
                min1 = number
            elif number <= min2:
                min2 = number
            else:
                return True


        return False




sol = Solution()

nums = [1,2,3,4,5]
nums = [2,1,5,0,4,6]
nums = [20,100,10,12,5,13]
print(sol.increasingTriplet(nums))

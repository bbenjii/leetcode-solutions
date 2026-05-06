from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # build prefix array, can build it directly into the output array
        length = len(nums)
        output = [0] * length
        prefix_product = 1

        for i in range(length):
            output[i] = prefix_product
            prefix_product *= nums[i]

        suffix_product = 1
        # compute the suffix product while traversing the og array backwards.
        # and directly multiplying the suffix_product with the corresponding suffix_product from the output/suffix array
        for i in range(length-1, -1, -1):
            output[i] *= suffix_product
            suffix_product *= nums[i]

        return output



sol = Solution()
nums = [1, 2, 3, 4]
Output = [24,12,8,6]

# nums = [-1,1,0,-3,3]
# output = [0,0,9,0,0]
sol.productExceptSelf(nums)

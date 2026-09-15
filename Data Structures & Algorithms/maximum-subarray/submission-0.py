class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        sumsub = nums[0]
        maxsum = nums[0]

        n = len(nums)

        for i in range(1, n):

            # Decide whether to continue the subarray
            # or start a new subarray
            if sumsub + nums[i] < nums[i]:
                sumsub = nums[i]
            else:
                sumsub = sumsub + nums[i]

            # Update maximum sum
            if sumsub > maxsum:
                maxsum = sumsub

        return maxsum
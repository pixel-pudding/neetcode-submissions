class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        currMax = nums[0]
        currMin = nums[0]

        maxprod = nums[0]

        for i in range(1, len(nums)):

            # Negative number swaps the role of max and min
            if nums[i] < 0:
                currMax, currMin = currMin, currMax

            currMax = max(nums[i], currMax * nums[i])
            currMin = min(nums[i], currMin * nums[i])

            maxprod = max(maxprod, currMax)

        return maxprod
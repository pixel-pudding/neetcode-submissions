class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #nlogn sol would be to sort 
        nums.sort()
        return nums[k-1]
        
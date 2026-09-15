class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #naive solution is to compute al the subarrays 
        maxprod=-1000000000000000000000
        n=len(nums)
        for i in range(0,n,1):
            prod=1 #computing product of each subarray 
            for j in range(i,n,1):
                prod=prod*nums[j]
                if(prod>maxprod):
                    maxprod=prod
        return maxprod
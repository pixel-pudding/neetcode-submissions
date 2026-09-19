class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        p1=nums[n-1] #pointer to the last element
         #swap with adjacent elements 
        for i in range(0,n,1):
            for j in range(i+1,n,1):
                #this points to the next element
                if(nums[i]==0):
                    nums[i],nums[j]=nums[j],nums[i] #swap 
                    

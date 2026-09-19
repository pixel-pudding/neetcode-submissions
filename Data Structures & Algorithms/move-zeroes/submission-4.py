class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        #better solution is to keep two pointers 
        i=0 #to keep track of 0 elements 
        for num in range(0,n,1):
            if(nums[num]==0):
                nums[i],nums[num]=nums[num],nums[i] #swap 
                i+=1 #move the pointer
                    

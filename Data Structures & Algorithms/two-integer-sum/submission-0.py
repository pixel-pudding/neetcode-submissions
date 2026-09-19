class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #naive approach is 2 pointers 
        ans=[] #to store the final answer here
        n=len(nums) #total numbers 
        for i in range(0,n,1):
            for j in range(i+1,n,1):
                if(nums[i]+nums[j]==target):
                    ans.append(i)
                    ans.append(j)
                    return ans
        return [-1,-1]
            

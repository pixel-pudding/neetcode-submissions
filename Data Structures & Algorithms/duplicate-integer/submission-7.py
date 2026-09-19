class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      #better approach is to use hashmap to keep track of frequency 
        freq=dict()
        n=len(nums)
        for i in range(0,n,1):
            if(nums[i] in freq):
                freq[nums[i]]+=1 #increase the count 
            else:
                 freq[nums[i]]=1 #we saw element for the first time 
        for number in freq:
            if(freq[number]>1):
                return True #number appears more than once
        return False
        
      
    

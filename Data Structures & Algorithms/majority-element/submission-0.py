class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        #we will use a hashmap to maintain the freq of each element 
        mp=dict()
        n=len(nums)
        for i in range(0,n,1):
            if(nums[i] in mp):
                mp[nums[i]]+=1 #increase the count 
            else:
                mp[nums[i]]=1 #we are seeing it for the first time 
        for number in mp:
            if(mp[number]>(n/2)):
                return number

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #better approach is to use a hashmap to storee the numbers already seen
        n=len(nums)
        ans=[] #to store the final answer here
        seen=dict()
        #map it as value:index
        for i in range(0,n,1):
            need=target-nums[i] #complement number we aer searching for
            if(need in seen):
                ans.append(i)
                ans.append(seen[need]) #the value of each is the index
                return(ans)
            else:
                seen[nums[i]]=i #add it to the dictionary
        return [-1,-1]

    

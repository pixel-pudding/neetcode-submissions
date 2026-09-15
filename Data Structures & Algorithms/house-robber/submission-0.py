class Solution:
    def rob(self, nums: List[int]) -> int:
        #constraint is that we cannot rob from two adjacent houses 
        #so we need to choose whether it is more benficial to take a house or skip a house 
        #let us assume we start from the first house in the neighbourhood 
        n=len(nums ) #number of houses 
        dp=[-1]*n #initialise the dp array 
        def solve(i):
            #define the recursive dp function 
            #base case: last house
            if(i>=n):
                return 0 #we have reached the last house, no more houses left to rob 
            if(dp[i]!=-1):
                return dp[i] #check if already calculated 
            rob=solve(i+2)+nums[i] #rob the current house 
            skip=solve(i+1) #skip the current house 
            choose=max(rob,skip ) #decide whether it is better to rob or skip 
            dp[i]=choose #update the dp table 
            return dp[i]
        return solve(0) #start from the first house
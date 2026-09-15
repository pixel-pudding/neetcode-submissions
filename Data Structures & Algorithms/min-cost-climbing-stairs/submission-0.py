class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #initialise dp array 
        n=len(cost) #total number of steps 

        dp=[-1]*n #we have n steps 
        #lets us consider moving up in the forward direction 
         
        def solve(i):
            #defining the recursive dp function 
            if(i>=n):
                return 0 
                #base case where we have reached the top of the steps 
            if(dp[i]!=-1):
                return dp[i] #check if already calculated 
            one=solve(i+1)+cost[i] #cost of taking one step
            two=solve(i+2) + cost[i] #cost of taking 2 steps 
            step=min(one,two) #choose which is of lesser cost 
            dp[i]=step #accordingly update the dp array 
            return dp[i]
        return min(solve(0),solve(1)) #start from the cheaper step


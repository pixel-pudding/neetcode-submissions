class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1) #initialise the dp array 
        def solve(n):
            #recursive dp 
            if(n==1):
                return 1 #only 1 step 
            if(n==2):
                return 2 #only 2 steps, only 2 ways 
            if(dp[n]!=-1):
                return dp[n]
            dp[n]=solve(n-1)+solve(n-2) #we can either climb 1 step at a time or 2 
            return dp[n]
        return solve(n) #solve for the given number of steps
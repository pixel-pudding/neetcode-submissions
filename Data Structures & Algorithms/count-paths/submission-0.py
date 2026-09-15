class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #m is rows 
        #n is columns 
        #Intialise 2d dp array 
        dp=[[-1]*n for _ in range(m)]
        #let i be row
        #let j be col 
        def solve(i,j):
            #definiing the recursive dp 
            if(i==m-1 and j==n-1):
                #we have reached the end 
                return 1 
            if(i>m-1 or j>n-1):
                return 0 #we have moved out of the board 
            if(dp[i][j]!=-1):
                return dp[i][j] #check if already calculated 
            #solve the dp 
            down=solve(i+1,j) #we move downwards in the row
            right=solve(i,j+1) #we move right in the col 
            dp[i][j]=down+right #update total moves
            return dp[i][j]

        return solve(0,0) #start from the first cell on the board
        
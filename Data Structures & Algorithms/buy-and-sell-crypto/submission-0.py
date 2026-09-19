class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #sell can happen after buying 
        #naive approach is nested loop to traverse 
        n=len(prices) #total number of days 
        maxprof=0
        prof=0
        for current in range(0,n,1):
            buy=prices[current] #we buy the stock today 
            for future in range(current+1,n,1):
                sell=prices[future] #we sell the stock on some day in future 
                prof=sell-buy
                if(prof>maxprof):
                    maxprof=prof
        return maxprof
        
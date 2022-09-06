class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
          # create new array and sort
        # pick max and min 
        buy = prices[0]
        profit = 0
        
        for i in range(len(prices)):
            # find lowest price
            if buy > prices[i]:
                buy = prices[i]
            # if the current price minus our lowest price is
            #greater than profit then , update profit
            elif prices[i] - buy > profit:
                profit = prices[i] - buy 
                
        return profit
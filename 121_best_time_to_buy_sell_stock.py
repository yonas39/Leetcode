class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ############ method-1 (slow but pass the time limit) ############
        # buy_price = 1000000000
        # profit = 0

        # for i in range(len(prices)):
        #     if prices [i] < buy_price:
        #         buy_price = prices[i]
        #         temp = max(prices[i:]) - buy_price 
        #         if temp > profit:
        #             profit = temp
        # return profit
        
        ############# Method-2 faster #################
        ############# minimum faster method############
        buy_price=float('inf')
        profit=0
        
        for i in range(len(prices)):
            #adjust the buy_price if get a better deal 
            if prices[i] < buy_price:
                buy_price = prices[i]
                
            #adjust the profit if get a better deal 
            if prices[i] - buy_price > profit:
                profit= prices[i] - buy_price

        return profit


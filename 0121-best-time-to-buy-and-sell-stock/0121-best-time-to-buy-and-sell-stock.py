class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        double_li=[[0 for i in range(len(prices))]]*len(prices)
        # print(double_li)
        #it hang timeout
        # max_=0
        # if prices.index
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         double_li[i][j]=prices[j]-prices[i]
        #         if double_li[i][j] > max_:
        #             max_=double_li[i][j]
        #     if max(double_li[i]) < 0 :
        #         return 0 
        # return max_
        min_price = float('inf')  
        max_profit = 0  

        for price in prices:
            if price < min_price:
                min_price = price  
            elif price - min_price > max_profit:
                max_profit = price - min_price  

        return max_profit
        

        
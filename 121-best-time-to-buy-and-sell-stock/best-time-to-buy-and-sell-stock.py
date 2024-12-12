class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        profit = 0
        
        for price in prices:
            if price < buy:
                buy = price
            else:
                potential_profit = price - buy
                if potential_profit > profit:
                    profit = potential_profit
                    
        return profit
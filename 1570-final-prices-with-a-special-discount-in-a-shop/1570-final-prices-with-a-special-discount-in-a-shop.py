class Solution:
    def finalPrices(self, prices):
        ans = []
        for i in range(len(prices)):
            flag = 1
            for j in range(i+1, len(prices)):
                print(f'item price is {prices[i]}, discount is {prices[j]}')
                if prices[i] >= prices[j]:
                    ans.append(prices[i] - prices[j])
                    flag = 0
                    break
            if flag ==1:
                ans.append(prices[i])
        return ans
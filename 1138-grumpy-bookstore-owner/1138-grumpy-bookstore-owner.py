class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        summ, max_ans, max_index = 0, 0, 0
        for index, i in enumerate(range(len(customers)- minutes+1)):
            window_customers = customers[i:i+minutes]
            window_grumpy = grumpy[i:i+minutes]
            summ = 0
            for g_index in range(len(window_grumpy)):
                
                if window_grumpy[g_index] == 1:
                    summ += window_customers[g_index]
                if max_ans < summ:
                    max_ans = summ
                    max_index = index

        for i in range(max_index , max_index+minutes):
            grumpy[i] = 0
        max_ans =0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                max_ans += customers[i]

        return max_ans
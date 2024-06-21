from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied_customers = sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0)
        print(satisfied_customers)

        max_additional_customers = 0
        for i in range(len(customers)-minutes+1):
            additional_satisfied = sum(customers[j] for j in range(i, i+minutes) if grumpy[j] == 1)
            if max_additional_customers < additional_satisfied:
                max_additional_customers = additional_satisfied

        return satisfied_customers + max_additional_customers
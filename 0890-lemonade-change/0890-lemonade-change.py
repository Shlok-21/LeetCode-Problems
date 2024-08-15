from collections import defaultdict
class Solution:
    def lemonadeChange(self, customers: List[int]) -> bool:
        change = defaultdict(int)
        for i in range(len(customers)):

            print(f'Bills : {change}')

            if customers[i] == 5:
                change[5] += 1
            elif customers[i] == 10:
                if change[5] < 1:
                    return False
                else:
                    change[5] -= 1
                    change[10] += 1
            elif customers[i] == 20:
                if (change[5]>=1 and change[10]>=1):
                    change[5]-=1
                    change[10]-=1
                    change[20]+=1
                elif (change[5] >=3):
                    for i in range(3):
                        change[5]-=1
                    change[20] += 1
                
                else:
                    return False

        return True
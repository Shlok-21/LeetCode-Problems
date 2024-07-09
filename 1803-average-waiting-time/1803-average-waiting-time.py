class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        chef_timer = customers[0][0]
        waiting = []
        for i in customers:
            if chef_timer < i[0]:
                chef_timer = i[0]+i[1]
                waiting.append(i[1])
            elif chef_timer >= i[0]:
                chef_timer += i[1]
                waiting.append(chef_timer - i[0])
            print(chef_timer)
        return sum(waiting)/ len(waiting)
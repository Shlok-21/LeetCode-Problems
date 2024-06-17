class Solution:
    def wateringPlants(self, plants, capacity: int) -> int:
        refill = capacity
        steps = 0
        for i in range(len(plants)-1):
            steps +=1
            print(f'now at plant {plants[i]} with steps {steps}')
            capacity -= plants[i]
            print(f'capacity is now {capacity} \n')
            
            if capacity < plants[i+1]:
                steps += (i+1)*2
                capacity = refill

        return(steps+1)
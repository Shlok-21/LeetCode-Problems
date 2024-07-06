class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x : x[1], reverse= True)
        units = 0
        for i in boxTypes:
            if truckSize >= i[0]:
                units += i[0] * i[1]
                truckSize -= i[0]
            else:
                units += truckSize * i[1]
                return units
        return units
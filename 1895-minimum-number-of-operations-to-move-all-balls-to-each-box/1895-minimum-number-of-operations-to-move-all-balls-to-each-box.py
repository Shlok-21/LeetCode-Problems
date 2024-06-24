class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        if '1' not in boxes:
            return [0]*len(boxes)         
        position = defaultdict(list)
        for index, bit in enumerate(boxes):
            position[bit].append(index)
        print(position)

        ans = []
        for i in range(0, len(boxes)):
            distance = position.get('1')
            ans.append(sum([x-i if i <x else i-x for x in distance]))
        return ans
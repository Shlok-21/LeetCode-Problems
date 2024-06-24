class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        ans = []
        for index, size in enumerate(groupSizes):
            groups[size].append(index)
        print(groups)
        for size, members in groups.items():
            for i in range(0, len(members), size):
                ans.append(members[i:i+size])
        return ans
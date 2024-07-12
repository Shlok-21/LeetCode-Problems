class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        score = 0
        if x > y:
            max_check = 'ab'
            min_check = 'ba'
            maxx = x
            minn = y
        else:
            max_check = 'ba'
            min_check = 'ab'
            maxx = y
            minn = x

        # Stack approach
        stack= []
        for char in s:
            if char == max_check[1] and stack and stack[-1] == max_check[0]:
                score +=maxx
                stack.pop()
            else:
                stack.append(char)

        new_stack = []
        for char in stack:
            if char == min_check[1] and new_stack and new_stack[-1] == min_check[0]:
                score+= minn
                new_stack.pop()
            else:
                new_stack.append(char)
        return score
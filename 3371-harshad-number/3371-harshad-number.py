class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        if int(x % sum([int(y) for y in (str(x))])) == 0:
            return sum([int(y) for y in (str(x))])
        else:
            return -1
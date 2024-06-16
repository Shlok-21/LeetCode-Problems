class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len({x: sentence.count(x) for x in sentence}) == 26
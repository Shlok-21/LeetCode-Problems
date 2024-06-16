class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len({x: sentence.count(x) for x in sentence}) == 26:
            return True
        else:
            return False  
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == 'type':
            checker = 0
        elif ruleKey == 'color':
            checker = 1
        else:
            checker = 2
        
        count = 0

        for item in items:
            if item[checker] == ruleValue:
                count+=1
        
        return count

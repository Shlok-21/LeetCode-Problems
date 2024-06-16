class Solution:
    def finalString(self, s: str) -> str:
        typed = []
        for i in s:
            if i.lower() == 'i':
                typed = typed[::-1]
            else:
                typed.append(i)
        return ''.join(typed)
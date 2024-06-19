class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # check if opposite moves (u,d) and (r,l) are equal then only true
        return (moves.count('U') == moves.count('D')) and (moves.count('R') == moves.count('L'))

        '''center = [0,0]
        for i in moves:
            if i =='U':
                center[0] +=1
            elif i =='D':
                center[0] -=1
            elif i =='L':
                center[1] -=1
            elif i =='R':
                center[1] +=1

        return True if center == [0,0] else False'''
        
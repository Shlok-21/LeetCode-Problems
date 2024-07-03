class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        atk_queen = []
        original = king.copy()
        inplace = [0,1,2,3,4,5,6,7]

        #check east
        while king[0] in inplace and king[1] in inplace:
            if king in queens:
                atk_queen.append(king)
                break
            king[1]+=1
        king = original.copy()
        print(king[0], king[1])

        #check west
        while king[0] in inplace and king[1] in inplace:
            if king in queens:
                atk_queen.append(king)
                break
            king[1]-=1

        king = original.copy()

        #check north
        while king[0] in inplace and king[1] in inplace:
            if king in queens:
                atk_queen.append(king)
                break
            king[0]-=1
        king = original.copy()

        #check south
        while king[0] in inplace and king[1] in inplace:
            if king in queens:
                atk_queen.append(king)
                break
            king[0]+=1

        king = original.copy()
        
        #check south-east
        while king[0] in inplace and king[1] in inplace:
            if king in queens:
                atk_queen.append(king)
                break
            king[0]+=1
            king[1]+=1
        king = original.copy()

                
        #check south-west
        while king[0] in inplace and king[1] in inplace:
            
            if king in queens:
                atk_queen.append(king)
                break
            king[0]+=1
            king[1]-=1
        king = original.copy()

        #check north-west
        while king[0] in inplace and king[1] in inplace:
            
            if king in queens:
                atk_queen.append(king)
                break
            king[0]-=1
            king[1]-=1
        king = original.copy()

        #check north-east
        while king[0] in inplace and king[1] in inplace:
            if king in queens:
                atk_queen.append(king)
                break
            king[0]-=1
            king[1]+=1
        king = original.copy()

        return atk_queen
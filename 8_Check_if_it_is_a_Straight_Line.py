class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        
        if (coordinates[1][0] - coordinates[0][0]) != 0:
            slope =  (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])
        else:
            slope = 2**31 - 1
        
        for i in range(2, len(coordinates)):
            if (coordinates[i][0] - coordinates[i-1][0]) != 0:
                slope1 = (coordinates[i][1] - coordinates[i-1][1])/(coordinates[i][0] - coordinates[i-1][0])
            else:
                slope1 = 2**31 - 1
            if slope1 != slope:
                return False
        
        return True
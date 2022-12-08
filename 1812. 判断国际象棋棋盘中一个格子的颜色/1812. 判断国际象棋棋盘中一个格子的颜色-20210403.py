class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if ((ord(coordinates[0])-ord('a'))%2==1 and int(coordinates[1])%2==1) or ((ord(coordinates[0])-ord('a'))%2==0 and int(coordinates[1])%2==0):
            return True
        else:
            return False
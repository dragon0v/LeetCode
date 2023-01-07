class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        if any([length>=10000, width>=10000, height>=10000, length*width*height>=10**9]):
            B = True
        else:
            B = False
        if mass>=100:
            H = True
        else:
            H = False
        if B and H:
            return "Both"
        else:
            if B:
                return "Bulky"
            if H:
                return "Heavy"
        return "Neither"
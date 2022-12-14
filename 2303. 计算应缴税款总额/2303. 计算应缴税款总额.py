class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        last = 0
        for b in brackets:
            if b[0]<=income:
                tax += b[1]*(b[0]-last)/100
                last = b[0]
            else:
                tax += b[1]*(income-last)/100
                return tax
        return tax
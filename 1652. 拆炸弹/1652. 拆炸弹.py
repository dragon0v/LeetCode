class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k==0:
            return [0] * len(code)
        
        n = len(code)
        if k>0:
            return [sum([code[(i+j+1)%n] for j in range(k)]) for i in range(n)]
        return [sum([code[(i-j-1)%n] for j in range(-k)]) for i in range(n)]
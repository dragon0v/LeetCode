class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = B = 0
        n = len(secret)
        secret = list(secret)
        guess = list(guess)
        i = 0
        while i < len(secret):
            if secret[i]==guess[i]:
                A += 1
                secret.pop(i)
                guess.pop(i)
                i -= 1
            i += 1
        c = Counter(guess)
        for each in secret:
            if each in c.keys() and c[each] > 0:
                c[each] -= 1
                B += 1
        
        return "%dA%dB"%(A,B)
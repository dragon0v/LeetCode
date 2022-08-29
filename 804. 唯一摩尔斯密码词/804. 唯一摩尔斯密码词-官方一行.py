class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        seen = {''.join(MORSE[ord(c)-ord('a')] for c in word) for word in words}
        return len(seen)

s = Solution()
t = s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
print(t)
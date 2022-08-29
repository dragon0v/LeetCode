class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        res = set()
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            t = ""
            for i in range(len(word)):
                t += table[ord(word[i])-ord('a')]
            res.add(t)
        return len(res)
        
s = Solution()
t = s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
print(t)
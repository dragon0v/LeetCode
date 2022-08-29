class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        def f(word):
            s1 = "qwertyuiop"
            s2 = "asdfghjkl"
            s3 = "zxcvbnm"
            
            def check(word,s):
                c = word[0]
                if c in s:
                    for each in word[1:]:
                        if each not in s:
                            return False
                    return True
                else:
                    return False
            return check(word,s1) or check(word,s2) or check(word,s3)
        
        for each in words:
            if(f(each.lower())):
                res.append(each)
        return res
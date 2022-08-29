from collections import Counter
from typing import *
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph += ' '
        banned.append('')
        b = " !?',;."
        words = [] #多此一举，直接counter，append改成counter+就行
        cw = ''
        for c in paragraph:
            if c not in b:
                cw += c.lower()
            else:
                if cw not in banned:
                    words.append(cw)
                cw = ''

        print(words)
        c = Counter(words)
        return c.most_common(1)[0][0]


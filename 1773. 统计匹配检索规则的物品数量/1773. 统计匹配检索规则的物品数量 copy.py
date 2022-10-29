from collections import Counter, defaultdict


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d = {'type':0, 'color':1, 'name':2}
        idx = d[ruleKey]
        c = defaultdict(int)
        for it in items:
            c[it[idx]] += 1

        return c[ruleValue]
        
        

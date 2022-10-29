from collections import Counter


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        types = Counter()
        colors = Counter()
        names = Counter()
        for it in items:
            types[it[0]] += 1
            colors[it[1]] += 1
            names[it[2]] += 1
        d = {'type':types, 'color':colors, 'name':names}
        return d[ruleKey][ruleValue]
        
        

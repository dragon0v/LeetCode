class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        index = {"type": 0, "color": 1, "name": 2}[ruleKey]  # index 0,1,2
        return sum(item[index] == ruleValue for item in items)  # 省一个dict

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/count-items-matching-a-rule/solutions/1931950/tong-ji-pi-pei-jian-suo-gui-ze-de-wu-pin-3qod/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
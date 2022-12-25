class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        # 其实不需要枚举全部，得到的第一个答案就是
        n = len(words)
        for i in range(n//2 + 1):
            if words[(startIndex+i)%n] == target:
                return i
            if words[(startIndex-i)%n] == target:
                return i

        return -1
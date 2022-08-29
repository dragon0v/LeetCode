class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # 滑动窗口
        # 右端点一直右移，记录左右端点中不同字符个数，超过k则左端点右移
        def maxConsecutive(key):
            i,j = 0, 0
            res = 0
            altered = 0
            
            while j < len(answerKey):
                res = max(res,j-i+1)
                if answerKey[j] == key:
                    j += 1
                else:
                    if altered<k:
                        altered += 1
                    else:
                        while answerKey[i]==key:
                            i += 1
                        i += 1
            return max(res,j-i+1)

        return max(maxConsecutive('T'),maxConsecutive('F'))
                
# 不对的
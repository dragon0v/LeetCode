class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        flag = False
        # python的for循环在循环中改变i值，循环次数不受影响 -> 因为range是生成器
        # 要想修改循环次数就得用while
        for i in range(n):
            if flag:
                flag = False
                continue
            if arr[i] == 0:
                for j in range(n-1,i,-1):
                    print(arr[j],arr[j-1])
                    arr[j] = arr[j-1]
                flag = True

# 直观做法，超时
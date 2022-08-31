class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # 模拟栈，看栈最后的元素是否和当前popped相同，相同则循环弹出
        mystack = []
        i = 0
        for c in pushed:
            mystack.append(c)
            while mystack and mystack[-1]==popped[i]:
                mystack.pop(-1)
                i += 1
        
        return mystack==[]
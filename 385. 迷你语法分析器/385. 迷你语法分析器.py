# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        # 维护一个栈，每当出现[就向栈中新增一个NI，出现]就将栈顶的NI加入栈顶第二个NI
        st = []
        pending = ''
        for c in s:
            if c=='[':
                if st:
                    if pending:
                        st[-1].add(NestedInteger(int(pending)))
                        pending = ''
                st.append(NestedInteger())
            elif c==']':
                if pending:
                    st[-1].add(NestedInteger(int(pending)))
                    pending = ''
                # pop from st
                if len(st)>1:
                    st[-2].add(st.pop())
                else:
                    print(st)
            elif c==',':
                if pending:
                    st[-1].add(NestedInteger(int(pending)))
                    pending = ""
            else:
                pending+=c

        print(st,len(st),pending)
        return st[-1] if st else NestedInteger(int(pending))

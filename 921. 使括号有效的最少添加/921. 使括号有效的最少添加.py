class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        for c in s:
            if c==')':
                if st and st[-1] == '(':
                    st.pop()
                    continue
            st.append(c)
            
        
        return len(st)
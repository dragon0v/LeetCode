class Solution:
    def sortCharacters(self,text):
        n = len(text)
        count = [0 for _ in range(128)]
        order = [0 for _ in range(n)]
        for c in text:
            count[ord(c)] += 1
        for i in range(1,128):
            count[i] += count[i-1]
        for i in range(n-1,-1,-1):
            count[ord(text[i])] -= 1
            order[count[ord(text[i])]] = i
        return order
    
    def computeCharClasses(self, text, order):
        n = len(text)
        res = [0 for _ in range(n)]
        res[order[0]] = 0
        for i in range(1,n):
            if (text[order[i]] != text[order[i - 1]]):
                res[order[i]] = res[order[i - 1]] + 1
            else:
                res[order[i]] = res[order[i - 1]]
        return res


    def sortDoubled(self, text, length, order, classfiy):
        n = len(text)
        count = [0 for _ in range(n)]
        newOrder = [0 for _ in range(n)]
        for i in range(n):
            count[classfiy[i]] += 1
        for i in range(1,n):
            count[i] += count[i - 1]
        for i in range(n-1,-1,-1):
            start = (order[i] - length + n) % n
            cl = classfiy[start]
            count[cl] -= 1
            newOrder[count[cl]] = start
        return newOrder

    def updateClasses(self, newOrder, classfiy, length):
        n = len(newOrder)
        newClassfiy = [0 for _ in range(n)]
        newClassfiy[newOrder[0]] = 0
        for i in range(1,n):
            curr = newOrder[i]
            prev = newOrder[i - 1]
            mid = curr + length
            midPrev = (prev + length) % n
            if (classfiy[curr] != classfiy[prev] or classfiy[mid] != classfiy[midPrev]):
                newClassfiy[curr] = newClassfiy[prev] + 1
            else:
                newClassfiy[curr] = newClassfiy[prev]
        return newClassfiy

    def buildSuffixArray(self, text):
        order = self.sortCharacters(text)
        classfiy = self.computeCharClasses(text, order)
        n = len(text)
        i = 1
        while i<n:
            order = self.sortDoubled(text, i, order, classfiy)
            classfiy = self.updateClasses(order, classfiy, i)
            i <<= 1
        return order


    def largestMerge(self, word1: str, word2: str) -> str:
        # 根据官方题解C++版本翻译
        # 2200ms，时间空间都后5%
        # TODO 那为什么要用后缀数组，他好在哪里？
        m,n = len(word1), len(word2)
        str = word1 + "@" + word2 + "*"
        suffixArray = self.buildSuffixArray(str)
        rank = [0 for i in range(m + n + 2)]
        for i in range(m + n + 2):
            rank[suffixArray[i]] = i
        merge = []
        i = j = 0
        while (i < m or j < n):
            if (i < m and rank[i] > rank[m + 1 + j]):
                merge.append(word1[i])
                i += 1
            else:
                merge.append(word2[j])
                j += 1
        return ''.join(merge)
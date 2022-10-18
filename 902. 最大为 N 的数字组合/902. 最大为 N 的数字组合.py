class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        # 朴素dp，没有用到digits非递减的条件，所以超时了
        digits = list(map(int,digits))
        # print(digits)
        res = {0}
        news = set()
        for _ in range(len(str(n))):
            for d in digits:
                for r in res:
                    new = r*10 + d
                    if new<=n:
                        news.add(new)

                res.update(news)
                news = set()
        
        print(res)

        return len(res)-1
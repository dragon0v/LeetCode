class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        # 按题意排序即可
        pos = set(positive_feedback)
        neg = set(negative_feedback)
        score = []
        for r in report:
            t = r.split(' ')
            ts = 0
            for w in t:
                if w in pos:
                    ts += 3
                elif w in neg:
                    ts -= 1
            score.append(ts)
        
        ss = sorted(zip(score,student_id), key=lambda x: (-x[0],x[1]))
        # print(ss)
        
        return list(map(lambda x:x[1],ss[:k]))
        # return [i for _,i in ss[:k]]
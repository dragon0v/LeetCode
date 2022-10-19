class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        t = []  # 这轮没吃上的学生
        while len(students)>0:
            flag = False  # 这轮没一个人吃上
            for i,s in enumerate(students):
                if s==sandwiches[0]:
                    sandwiches.pop(0)
                    # students.pop(i)
                    flag = True
                else:
                    t.append(s)
            if not flag:
                return len(t)
            else:
                students = t
                t = []
        return 0
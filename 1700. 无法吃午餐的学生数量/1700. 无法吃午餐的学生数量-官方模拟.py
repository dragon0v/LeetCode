class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # 问题简化：三明治必须按顺序吃，但是人的顺序可以任意（因为一直可以循环）
        s1 = sum(students)  # 吃1的学生数量
        s0 = len(students) - s1  # 吃0的学生数量
        for x in sandwiches:
            if x == 0 and s0:
                s0 -= 1
            elif x == 1 and s1:
                s1 -= 1
            else:
                # 停止条件：x=0但没有吃0的学生了，所以停止
                break
        return s0 + s1

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/number-of-students-unable-to-eat-lunch/solutions/1900373/wu-fa-chi-wu-can-de-xue-sheng-shu-liang-fv3f5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
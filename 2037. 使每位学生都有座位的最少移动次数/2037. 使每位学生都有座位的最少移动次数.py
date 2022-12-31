class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # 贪心，排序后将学生和座位一一对应是最优的
        seats.sort()
        students.sort()
        return sum(abs(x-y) for x,y in zip(seats,students))
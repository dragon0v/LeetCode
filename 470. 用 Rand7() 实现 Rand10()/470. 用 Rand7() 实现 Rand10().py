# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        '''
          1 2 3 4 5 6 7
        1 1 2 3 4 5 6 7
        2 2 4 6 8 0 2 4
        3 3 6 9 2 5 8 1
        4 4 8 2 6 0 4 8
        5 5 0 5 0 5 0 5
        6 6 2 8 4 0 6 2
        7 7 4 1 8 5 2 9
        调用两次rand7相乘得到49个乘积，取前40个，每4个代表一个数字即可
        这是不行的，因为会有相同的数字
        所以考虑个位数
        一共3,8,2......个1-0
        所以发现乘积也不合适
        应该用加法
        	a	1	2	3	4	5	6	7
        b								
        1		2	3	4	5	6	7	8
        2		3	4	5	6	7	8	9
        3		4	5	6	7	8	9	0
        4		5	6	7	8	9	0	1
        5		6	7	8	9	0	1	2
        6		7	8	9	0	1	2	3
        7		8	9	0	1	2	3	4
        去掉右上角的  
        6	7	8
        7	8	9
        8	9	0      后

        每个数字的出现次数为4次，0-9的概率相同
        
        
        '''
        # 这个:=一点意义都没有啊，不如直接while(1)，a=,b=
        while(a:=rand7(),b:=rand7()):
            if not (a>4 and b<4):
                return (a+b)%10 + 1
        # 不用while的递归如下 
        # a,b = rand7(),rand7()
        # if (a>4 and b<4):
        #     rand10()
        # return (a+b)%10 + 1
        
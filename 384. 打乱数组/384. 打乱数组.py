class Solution:

    def __init__(self, nums: List[int]):
        self.ori = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.ori


    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        # Fisher-Yates 洗牌算法

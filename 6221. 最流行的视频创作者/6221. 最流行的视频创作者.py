class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        # 某种sort，实用向的题
        # TODO 
        z = list(zip(views,ids,creators))
        print(z)
        # z.sort(key=lambda x,y,z:[x,-y])
        return z[-1]
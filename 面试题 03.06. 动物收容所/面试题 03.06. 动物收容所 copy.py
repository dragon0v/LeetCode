from typing import List
class AnimalShelf:

    def __init__(self):
        self.animals = []

    def __iter__(self):
        return self

    def __next__(self):
        return self.animals[0] if len(self.animals)>0 else [-1,-1]


    def enqueue(self, animal: List[int]) -> None:
        self.animals.append(animal)

    def dequeueAny(self) -> List[int]:
        return next(self)

    def dequeueDog(self) -> List[int]:
        for i in range(len(self.animals)):
            if self.animals[i][1]==1:
                return self.animals.pop(i)
        return [-1,-1]

    def dequeueCat(self) -> List[int]:
        for i in range(len(self.animals)):
            if self.animals[i][1]==0:
                return self.animals.pop(i)
        return [-1,-1]


# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()
AS = AnimalShelf()
AS.enqueue([0,1])
print(AS.dequeueAny())
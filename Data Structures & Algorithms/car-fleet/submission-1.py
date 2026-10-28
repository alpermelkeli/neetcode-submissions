import heapq


class SpecialStack:
    def __init__(self):
        self.stack = []
        self.top = -1
    
    def pushTime(self, time: float):
        if self.top == -1:
            self.stack.append(time)
            self.top += 1
            return self.top + 1 # Return current size of stack 

        if self.stack[self.top] < time:
            self.stack.append(time)
            self.top += 1
            return self.top + 1 # Return current size of stack 

    def getSize(self):
        return self.top + 1





class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)
        carStack = SpecialStack()
        carHeap = []
        for (pos, sp) in cars:
            heapq.heappush(carHeap, (-pos, self.calculateTime(pos,sp, target)))

        while len(carHeap) > 0:
            carStack.pushTime(carHeap[0][1])
            heapq.heappop(carHeap)
        return carStack.getSize()
    

    def calculateTime(self, pos, sp, target):
        return (target - pos) / sp

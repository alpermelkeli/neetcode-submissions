import heapq
import math
from typing import List

class Point:
    def __init__(self, coordinate: List[int]):
        self.coordinate = coordinate
        self.distance = math.sqrt(pow(coordinate[0], 2) + pow(coordinate[1], 2))

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for coordinate in points:
            point = Point(coordinate)
            entry = (-point.distance, point.coordinate)  # coordinate zaten hashable degil ama tie-break olarak liste karşılaştırılabilir, bkz. not

            if len(heap) < k:
                heapq.heappush(heap, entry)
            else:
                heapq.heappushpop(heap, entry)

        return [coord for _, coord in heap]
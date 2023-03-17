from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        record = [False] * len(rooms)
        toVisit = [0]

        while len(toVisit) > 0:
            enterRoom = toVisit.pop(0)
            if not record[enterRoom]:
                record[enterRoom] = True
                for key in rooms[enterRoom]:
                    if not record[key]:
                        toVisit.append(key)

        for _ in record:
            if not _:
                return False
        return True


rooms = [[1, 3], [3, 0, 1], [2], [0]]

solution = Solution()
print(solution.canVisitAllRooms(rooms=rooms))

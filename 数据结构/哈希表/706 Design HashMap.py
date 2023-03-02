class MyHashMap1:

    def __init__(self):
        self.hash = [(-1, 0)] * 1000001

    def put(self, key: int, value: int) -> None:
        self.hash[key] = (key, value)

    def get(self, key: int) -> int:
        if self.hash[key][0] == -1:
            return -1
        else:
            return self.hash[key][1]

    def remove(self, key: int) -> None:
        self.hash[key] = (-1, 0)


class MyHashMap:

    def __init__(self):
        self.hash = [(-1, 0)] * 10007

    def put(self, key: int, value: int) -> None:
        index = key % 10007
        delta = 1
        while self.hash[index][0] != -1 and self.hash[index][0] != key:
            index = (index + delta ** 2) % 10007
            delta += 1
        self.hash[index] = (key, value)

    def get(self, key: int) -> int:
        index = key % 10007
        delta = 1
        while self.hash[index][0] != key:
            if self.hash[index][0] == -1:
                return -1
            index = (index + delta ** 2) % 10007
            delta += 1
        return self.hash[index][1]

    def remove(self, key: int) -> None:
        index = key % 10007
        delta = 1
        while self.hash[index][0] != key:
            if self.hash[index][0] == -1:
                return
            index = (index + delta ** 2) % 10007
            delta += 1
        self.hash[index] = (-1, 0)


hashMap = MyHashMap()
hashMap.remove(key=14)
print(hashMap.hash)
hashMap.get(key=4)
hashMap.put(key=7, value=3)
hashMap.put(key=11, value=1)

'''
["MyHashMap","put","put","get","get","put","get","remove","get"]
[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]
'''

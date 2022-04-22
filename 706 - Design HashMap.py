"""

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

    MyHashMap() initializes the object with an empty map.
    void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
    int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
    void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
From Leetcode : https://leetcode.com/problems/design-hashmap/

"""

class MyHashMap:

    def __init__(self):
        self.map = []
        

    def put(self, key: int, value: int) -> None:
        if len(self.map) > 0:
            for id, pair in enumerate(self.map):
                #print(pair)
                if pair[0] == key:
                    self.map[id] = [pair[0], value]
                    return 
        self.map.append([key, value])
            
        

    def get(self, key: int) -> int:
        for pair in self.map:
            if pair[0] == key:
                return pair[1]
            
        return -1
        

    def remove(self, key: int) -> None:
        for pair in self.map:
            if pair[0] == key:
                self.map.remove(pair)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

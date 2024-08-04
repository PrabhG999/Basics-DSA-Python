from collections import OrderedDict


class LRUCache():
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key]=value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)


def main():
    # Create an LRUCache instance with capacity 2
    lRUCache = LRUCache(2)

    # Perform operations as per the example
    lRUCache.put(1, 1)  # cache is {1=1}
    lRUCache.put(2, 2)  # cache is {1=1, 2=2}
    print(lRUCache.get(1))  # return 1, cache is {2=2, 1=1}

    lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    print(lRUCache.get(2))  # returns -1 (not found)

    lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {3=3, 4=4}
    print(lRUCache.get(1))  # returns -1 (not found)
    print(lRUCache.get(3))  # return 3, cache is {4=4, 3=3}
    print(lRUCache.get(4))  # return 4, cache is {3=3, 4=4}


if __name__ == "__main__":
    main()

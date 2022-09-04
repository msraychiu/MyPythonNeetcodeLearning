class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key + str(timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        while timestamp > 0:
            item = self.map.get(key + str(timestamp))
            if item is not None:
                return item
            else:
                timestamp -= 1
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

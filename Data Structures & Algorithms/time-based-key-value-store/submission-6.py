class TimeMap:

    def __init__(self):
        self.times = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.times:
            self.times[key] = {}
        if timestamp not in self.times[key]:
            self.times[key][timestamp] = []
        self.times[key][timestamp].append(value)
        print("doing a set", key, value, timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ""
        curr = -1
        list_times = self.times[key]
        for i in list_times:
            if i <= timestamp:
                curr = max(curr, i)
        if curr == -1:
            return ""
        return self.times[key][curr][-1]



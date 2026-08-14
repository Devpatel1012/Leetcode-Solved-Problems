class LRUCache(object):

    def __init__(self, capacity):
        self.cache = dict()
        self.size = capacity
        self.used = []
        

    def get(self, key):
        if key in self.cache:
            self.used.remove(key)
            self.used.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.used.remove(key)
            self.used.append(key)
        else:
            if len(self.cache)>=self.size:
                lru = self.used[0]
                self.cache.pop(lru)
                self.used.remove(lru)


            self.cache[key] = value
            self.used.append(key)

                

        



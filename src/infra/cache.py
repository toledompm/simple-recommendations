class custom_lru_cache:
    def __init__(self, func):
        self.cache = []
        self.func = func

    def __call__(self):
        if len(self.cache) > 0:
            return self.cache
        result = self.func()
        self.cache = result
        return result

    def clear_cache(self):
        self.cache = []

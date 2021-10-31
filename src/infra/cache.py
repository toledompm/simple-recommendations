import collections


class custom_lru_cache:
    def __init__(self, func, maxsize=32):
        self.cache = collections.OrderedDict()
        self.func = func
        self.maxsize = maxsize

    def __call__(self, *args):
        cache = self.cache
        if args in cache:
            cache.move_to_end(args)
            return cache[args]
        result = self.func(*args)
        cache[args] = result
        if len(cache) > self.maxsize:
            cache.popitem(last=False)
        return result

    def cache_remove(self, *args):
        if isinstance(args, collections.Iterable):
            for arg in args:
                if arg in self.cache:
                    self.cache.pop(args)
        else:
            if args in self.cache:
                self.cache.pop(args)

    def clear_cache(self):
        self.cache = collections.OrderedDict()

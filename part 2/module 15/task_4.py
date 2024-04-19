print('Задача 4. Кэширование запросов')

# Создайте класс LRU Cache, который хранит ограниченное количество объектов и,
# при превышении лимита, удаляет самые давние (самые старые) использованные элементы.
#
# Реализуйте методы добавления и извлечения элементов с
# использованием декораторов property и setter.

from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = OrderedDict()

    @property
    def cache(self):
        if self._cache:
            return next(iter(self._cache))

    @cache.setter
    def cache(self, new_elem):
        key, value = new_elem
        if key in self._cache:
            del self._cache[key]
        elif len(self._cache) >= self._capacity:
            self._cache.popitem(last=False)
        self._cache[key] = value

    def get(self, key):
        if key in self._cache:
            value = self._cache.pop(key)
            self._cache[key] = value
            return value

    def print_cache(self):
        print("LRU Cache:")
        for key, value in self._cache.items():
            print(f"{key} : {value}")


cache = LRUCache(3)
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")
cache.print_cache()
print(cache.get("key2"))
cache.cache = ("key4", "value4")
cache.print_cache()

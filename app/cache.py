from interfaces import Fuel

cache: list[Fuel] = []


def add_to_cache(obj: Fuel):
    cache.append(obj)


def clear_cache():
    cache.clear()

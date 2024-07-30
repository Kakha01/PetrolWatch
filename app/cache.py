from interfaces import Fuel

fuels_cache: list[Fuel] = []

fuels_cache_categorised: dict[str, list[Fuel]] = {}


def categorize_fuels(fuels: list[Fuel]):
    fuels_categorised: dict[str, list[Fuel]] = {}

    for fuel in fuels:
        if fuel["company_name"] in fuels_categorised:
            fuels_categorised[fuel["company_name"]].append(fuel)
        else:
            fuels_categorised[fuel["company_name"]] = [fuel]

    fuels_cache_categorised.clear()
    fuels_cache_categorised.update(fuels_categorised)


def add_to_cache(fuel: Fuel):
    fuels_cache.append(fuel)


def extend_cache(fuels: list[Fuel]):
    fuels_cache.extend(fuels)


def clear_fuel_cache():
    fuels_cache.clear()

from typing import TypedDict, NamedTuple, Callable, Literal


class Fuel(TypedDict):
    company_name: str
    fuel_name: str
    fuel_price: str
    fuel_type: str


class FuelSource(NamedTuple):
    url: str
    data_type: Literal["html"] | Literal["json"]
    extractor: Callable

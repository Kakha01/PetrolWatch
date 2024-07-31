from typing import TypedDict, NamedTuple, Callable, Literal, Any


class Fuel(TypedDict):
    name: str
    price: str
    type: str


class FuelSource(NamedTuple):
    url: str
    company_name: str
    data_type: Literal["html"] | Literal["json"]
    extractor: Callable[[Any], list[Fuel]]

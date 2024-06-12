import re
from typing import Callable
 
class Utils:
    @staticmethod
    def sluggify(s: str) -> str:
        """
        Converts a string to a slug representation based on fuel type.

        Args:
            s (str): The input string to be converted.
        
        Returns:
            str: The slug representation of the input string based on fuel type.
        """
        
        types = FuelType.get_types()
    
        for fuel_check, fuel_type in types.items():
            if fuel_check(s):
                return fuel_type
    
        return "unknown"


class FuelType:
    @staticmethod
    def is_euro_regular(s: str) -> bool:
        return bool(re.search(r"(euro|evro).*(regulari?)", s, re.I))

    @staticmethod
    def is_regular(s: str) -> bool:
        return bool(re.search(r"(regulari?)", s, re.I))

    @staticmethod
    def is_euro_diesel(s: str) -> bool:
        return bool(re.search(r"(euro|evro).*(dieseli?|dizeli)", s, re.I))

    @staticmethod
    def is_diesel(s: str) -> bool:
        return bool(re.search(r"(dieseli?|dizeli)", s, re.I))

    @staticmethod
    def is_super(s: str) -> bool:
        return bool(re.search(r"(superi?)", s, re.I))

    @staticmethod
    def is_premium(s: str) -> bool:
        return bool(re.search(r"(premiumi?)", s, re.I))
    
    @staticmethod
    def get_types() -> dict[Callable[[str], bool], str]:
        return {
            FuelType.is_euro_diesel: "euro_diesel",
            FuelType.is_diesel: "diesel",
            FuelType.is_euro_regular: "euro_regular",
            FuelType.is_regular: "regular",
            FuelType.is_super: "super",
            FuelType.is_premium: "premium"
        }
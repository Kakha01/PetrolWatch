import re
 
class Utils:
    @staticmethod
    def sluggify_fuel(fuel: str) -> str | None:
        fuel_type_match = Utils.extract_fuel_type(fuel)
        
        if not fuel_type_match:
            return None

        euro, fuel_type = fuel_type_match

        if euro:
            return f"{euro}_{fuel_type}"
        
        return fuel_type

    @staticmethod
    def extract_fuel_type(fuel: str) -> tuple[str | None, str] | None:
        euro_regex = r"(euro|evro)"
        fuel_regex = r"(regular|diesel|dizel|super|premium)"

        euro_match = re.search(euro_regex, fuel, re.IGNORECASE)
        fuel_match = re.search(fuel_regex, fuel, re.IGNORECASE)
        
        if not fuel_match:
            return None

        return (
            Utils.normalize_euro(euro_match.group()) if euro_match else None,
            Utils.normalize_fuel(fuel_match.group())
        )

    @staticmethod
    def normalize_euro(euro: str) -> str:
        """
        replace "evro" if it exists with "euro" and convert to lowercase
        """
        return re.sub("evro", "euro", euro.lower())
    
    @staticmethod
    def normalize_fuel(fuel: str) -> str:
        """ 
        replace "dizel" if it exists with "diesel" and convert to lowercase 
        """
        return re.sub("dizel", "diesel", fuel.lower())

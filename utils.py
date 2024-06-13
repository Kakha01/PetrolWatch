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
        regex = r"(euro|evro)?.*(regular|diesel|dizel|super|premium)"
        fuel_type_match = re.search(regex, fuel, re.IGNORECASE)
        
        if not fuel_type_match:
            return None

        euro, fuel_type = fuel_type_match.groups()

        return (
            Utils.normalize_euro(euro) if euro else None,
            Utils.normalize_fuel(fuel_type)
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
        
    

print(Utils.sluggify_fuel("evro regulari"))

import re
 
class Utils:
    
    FUEL_TYPE_REGEX = r"(regular|diesel|dizel|super|premium)"
    FUEL_GRADE_REGEX = r"(euro|evro)"

    """ Mapping Georgian latinized words for fuel types and grades """
    FUEL_TYPE_MAPPING = {
        "dizel": "diesel",
    }

    FUEL_GRADE_MAPPING = {
        "evro": "euro",
    }

    @staticmethod
    def sluggify_fuel(fuel: str) -> str | None:
        fuel_type = Utils.extract_fuel_type(fuel)
        
        if not fuel_type:
            return None

        fuel_grade = Utils.extract_fuel_grade(fuel)

        if not fuel_grade:
            return fuel_type
        
        return f"{fuel_grade}_{fuel_type}"

    @staticmethod
    def extract_fuel_type(input: str) -> str | None:
        fuel_type_match = re.search(Utils.FUEL_TYPE_REGEX, input, re.IGNORECASE)

        if not fuel_type_match:
            return None

        return Utils.normalize_fuel_type(fuel_type_match.group())

    @staticmethod
    def extract_fuel_grade(input: str) -> str | None:
        fuel_grade_match = re.search(Utils.FUEL_GRADE_REGEX, input, re.IGNORECASE)

        if not fuel_grade_match:
            return None

        return Utils.normalize_fuel_grade(fuel_grade_match.group())

    @staticmethod
    def normalize_fuel_grade(fuel_grade: str) -> str:
        fuel_grade_l = fuel_grade.lower()
        return Utils.FUEL_GRADE_MAPPING.get(fuel_grade_l, fuel_grade_l)
    
    @staticmethod
    def normalize_fuel_type(fuel_type: str) -> str:
        fuel_type_l = fuel_type.lower()
        return Utils.FUEL_TYPE_MAPPING.get(fuel_type_l, fuel_type_l)
     

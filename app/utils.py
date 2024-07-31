import re
from typing import Optional

FUEL_TYPE_REGEX = r"(regular|diesel|dizel|super|premium)"
FUEL_GRADE_REGEX = r"(euro|evro)"

# Mapping Georgian latinized words for fuel types and grades
FUEL_MAPPING = {"dizel": "diesel", "evro": "euro"}


def sluggify_fuel(fuel: str) -> Optional[str]:
    fuel_type = extract_fuel_type(fuel)
    if not fuel_type:
        return None

    fuel_grade = extract_fuel_grade(fuel)
    return f"{fuel_grade}_{fuel_type}" if fuel_grade else fuel_type


def extract_fuel_term(input: str, regex: str) -> Optional[str]:
    match = re.search(regex, input, re.IGNORECASE)
    return normalize_fuel_term(match.group()) if match else None


def normalize_fuel_term(term: str) -> str:
    return FUEL_MAPPING.get(term.lower(), term.lower())


def extract_fuel_type(input: str) -> Optional[str]:
    return extract_fuel_term(input, FUEL_TYPE_REGEX)


def extract_fuel_grade(input: str) -> Optional[str]:
    return extract_fuel_term(input, FUEL_GRADE_REGEX)


def capitalize_words(input: str) -> str:
    return " ".join(word.capitalize() for word in input.split())

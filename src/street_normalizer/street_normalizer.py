import re
from .references import street_abbreviations, normalized_street_suffixes, unit_designators, chars_to_remove, names


# Actual Methods:
def normalize_street_suffixes(initial_value: str) -> str:
    cleaned = initial_value.upper().strip()
    for key in normalized_street_suffixes:
        for value in normalized_street_suffixes[key]:
            pattern = r"\b" + re.escape(value) + r"\b"
            cleaned = re.sub(pattern, key, cleaned)
    return cleaned


def normalize_unit_designators(initial_value: str) -> str:
    cleaned = initial_value.upper().strip()
    for key in unit_designators:
        pattern = r"\b" + re.escape(key) + r"\b"
        cleaned = re.sub(pattern, unit_designators[key], cleaned)
    return cleaned


def normalize_street_abbreviations(initial_value: str) -> str:
    cleaned = initial_value.upper().strip()
    for key in street_abbreviations:
        for value in street_abbreviations[key]:
            pattern = r"\b" + re.escape(value) + r"\b"
            cleaned = re.sub(pattern, key, cleaned)
    return cleaned


def remove_extra_chars(initial_value: str) -> str:
    cleaned = initial_value.upper().strip()
    for char in chars_to_remove:
        cleaned = cleaned.replace(f"{char}", "")
    return cleaned


def cleaner(initial_value: str) -> str:
    return normalize_street_abbreviations(normalize_street_suffixes(normalize_unit_designators(remove_extra_chars(initial_value))))


def city_cleaner(city: str) -> str:
    if "," not in city:
        return city.strip().upper()
    return city[:city.index(",")].upper().strip()


def name_cleaner(name: str) -> str:
    cleaned = name.upper().strip()
    for key in names.keys():
        pattern = r"\b" + re.escape(key) + r"\b"
        cleaned = re.sub(pattern, names[key], cleaned)
    return cleaned.strip()

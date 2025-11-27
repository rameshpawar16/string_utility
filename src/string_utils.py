def reverse_string(text: str)->str:
    return text[::-1]

def to_upper(text: str)->str:
    return text.upper()

def to_lower(text: str)->str:
    return text.lower()

def count_vowels(text: str)->int:
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

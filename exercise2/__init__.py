def reverse_string(s: str) -> str:
    """
    Return the input string in reverse order.
    """
    return s[::-1]


def count_vowels(s: str) -> int:
    """
    Return the number of vowels (a, e, i, o, u) in the input string.
    Case-insensitive: both uppercase and lowercase vowels should be counted.
    """
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)


def is_palindrome(s: str) -> bool:
    """
    Check if the input string is a palindrome.
    A palindrome reads the same backward as forward.
    Spaces and case are ignored.
    """
    # Remove spaces and convert to lowercase
    s_clean = "".join(s.split()).lower()
    return s_clean == s_clean[::-1]


def capitalize_words(s: str) -> str:
    """
    Capitalize the first letter of each word in the input string.
    """
    return " ".join(word.capitalize() for word in s.split())

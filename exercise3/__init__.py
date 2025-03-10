from typing import Union

# Defining a Temperature type for cleaner type hints
Temperature = Union[int, float]


def celsius_to_fahrenheit(celsius: Temperature) -> float:
    """
    Convert temperature from Celsius to Fahrenheit.

    Formula: F = C × 9/5 + 32

    Returns:
        Temperature in Fahrenheit (rounded to 2 decimal places)
    """
    fahrenheit = celsius * 9 / 5 + 32
    return round(fahrenheit, 2)


def fahrenheit_to_celsius(fahrenheit: Temperature) -> float:
    """
    Convert temperature from Fahrenheit to Celsius.

    Formula: C = (F - 32) × 5/9

    Returns:
        Temperature in Celsius (rounded to 2 decimal places)
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 2)


def celsius_to_kelvin(celsius: Temperature) -> float:
    """
    Convert temperature from Celsius to Kelvin.

    Formula: K = C + 273.15

    Returns:
        Temperature in Kelvin (rounded to 2 decimal places)
    """
    kelvin = celsius + 273.15
    return round(kelvin, 2)


def kelvin_to_celsius(kelvin: Temperature) -> float:
    """
    Convert temperature from Kelvin to Celsius.

    Formula: C = K - 273.15

    Returns:
        Temperature in Celsius (rounded to 2 decimal places)

    Raises:
        ValueError: If kelvin is less than 0 (below absolute zero)
    """
    if kelvin < 0:
        raise ValueError("Kelvin temperature cannot be below absolute zero.")
    celsius = kelvin - 273.15
    return round(celsius, 2)


"""
This module contains a function for generating random names in Portuguese.
"""
import random 
from typing import Optional
from names import men_names, women_names, surnames

def generate_name(gender: Optional[int] = None) -> str:
    """
    Generates a random name in Portuguese.

    Parameters:
        gender (int): The gender of the name to generate. 0 for male, 1 for female.

    Returns:
        str: The generated name.
    """
    try:
        if not gender:
            gender = random.randint(0, 1)
        names = random.choices(men_names if gender == 0 else women_names, k=1)
        last_name = random.choices(surnames, k=1)[0]
        return f"{names[0]} {last_name}"
    except ValueError:
        return "Invalid gender parameter. Please specify 0 for male or 1 for female."
    except IndexError:
        return "An error occurred while accessing the list of names or surnames."
    except Exception as e:
        return f"An error occurred: {e}"

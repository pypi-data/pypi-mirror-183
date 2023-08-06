
"""
This module contains a function for generating random names in Portuguese.
"""
import random
from unidecode import unidecode
from typing import Optional
from names import men_names, women_names, surnames

class Person:
    def __init__(self, first_name: str, last_name: str, gender: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = self.get_email()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_email(self) -> str:
        # Replace spaces in the first name with dots, convert to lowercase, and remove special characters
        first_name = unidecode(self.first_name.replace(" ", ".").lower())
        # Convert last name to lowercase and remove special characters
        last_name = unidecode(self.last_name.lower())
        return f"{first_name}.{last_name}@example.com"

def generate_name(gender: Optional[int] = None) -> str:
    """
    Generates a random name in Portuguese.

    Parameters:
        gender (int): The gender of the name to generate. 0 for male, 1 for female.

    Returns:
        Name: An object containing the generated name.
    """
    try:
        if not gender:
            gender = random.randint(0, 1)
        firts_name = random.choices(men_names if gender == 0 else women_names, k=1)[0]
        last_name = random.choices(surnames, k=1)[0]
        return Person(firts_name, last_name, gender)
    except ValueError:
        return "Invalid gender parameter. Please specify 0 for male or 1 for female."
    except IndexError:
        return "An error occurred while accessing the list of names or surnames."
    except Exception as e:
        return f"An error occurred: {e}"

person = generate_name(1)
print(person)
print(person.email)
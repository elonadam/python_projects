import json
from cocktail import Cocktail  # Assuming the Cocktail class is defined in cocktail.py
import re

class CocktailManager:
    """
    Manages a collection of cocktails and handles operations like adding, editing, and deleting recipes.
    Recipes are stored in a JSON file.
    """

    def __init__(self, file_name="cocktail_book.json"):
        self.file_name = file_name
        self.cocktail_book = self.load_from_file()

    def add_cocktail(self, cocktail):
        """
        Adds a cocktail to the cocktail book.
        :param cocktail: Cocktail object
        """
        if cocktail.name in self.cocktail_book:
            print(f"Cocktail '{cocktail.name}' already exists.")
            raise ValueError("Cocktail already exists.")
        else:
            self.cocktail_book[cocktail.name] = cocktail.to_dict()
            self.save_to_file()
            print(f"Cocktail '{cocktail.name}' added to the cocktail book.")

    def remove_cocktail(self, name):
        """
        Removes a cocktail by name.
        :param name: str, name of the cocktail to remove
        """
        if name in self.cocktail_book:
            del self.cocktail_book[name]
            self.save_to_file()
            print(f"Cocktail '{name}' removed from the cocktail book.")
        else:
            print(f"Cocktail '{name}' not found in the cocktail book.")

    def edit_cocktail(self, name, updated_data):
        """
        Edits an existing cocktail in the cocktail book by its name.
        :param name: str, name of the cocktail to edit
        :param updated_data: dict, key-value pairs of attributes to update
        """
        if name in self.cocktail_book:
            for key, value in updated_data.items():
                if key in self.cocktail_book[name]:
                    self.cocktail_book[name][key] = value
                    print(f"Updated '{key}' for cocktail '{name}'.")
                else:
                    print(f"Attribute '{key}' does not exist for cocktail '{name}'.")
            self.save_to_file()
        else:
            print(f"Cocktail '{name}' not found in the cocktail book.")

    def get_cocktail(self, name):
        """
        Retrieves a specific cocktail by its name.
        :param name: str, name of the cocktail to retrieve
        :return: Dictionary of the cocktail, or None if not found.
        """
        return self.cocktail_book.get(name, f"Cocktail '{name}' not found.")

    # def get_all_cocktails(self):
    #     """
    #     Returns all cocktails in the cocktail book.
    #     :return: cocktail_book dictionary.
    #     """
    #     return self.cocktail_book

    def save_to_file(self):
        """
        Saves the cocktail book to a JSON file.
        """
        try:
            with open(self.file_name, "w") as file:
                json.dump(self.cocktail_book, file, indent=4)
            print("Cocktail book saved to file.")
        except Exception as e:
            print(f"Error saving cocktail book: {e}")

    def load_from_file(self):
        """
        Loads the cocktail book from a JSON file.
        :return: Dictionary containing all cocktails.
        """
        try:
            with open(self.file_name, "r") as file:
                print("Cocktail book loaded from file.")
                return json.load(file)
        except FileNotFoundError:
            print("No saved cocktail book found. Starting fresh.")
            return {}
        except Exception as e:
            print(f"Error loading cocktail book: {e}")
            return {}

    def extract_cocktail_names(self):
        """
        Extracts the names of cocktails from the provided dictionary.
        """
        return list(self.cocktail_book.keys())

    def calculate_and_update_abv(self):
        """
        Calculates the ABV for each cocktail in the cocktail_book and updates it in memory and the JSON file.
        """
        # Predefined ABV values for common ingredients
        INGREDIENT_ABV = {'white rum': 40,
                          'dark rum': 40,
                          'blue curacao': 21,
                          'fresh lime juice': 0,
                          'fresh lemon juice': 0,
                          'simple syrup': 0,
                          'rich syrup': 0,
                          'lime juice': 0,
                          'egg white': 0,
                          'lemon juice': 0,
                          'orgeat syrup': 0,
                          'triple sec': 30,
                          'gin': 40,
                          'tequila': 40,
                          'vodka': 40,
                          'campari': 25,
                          'sweet vermouth': 15,
                          'soda water': 0,
                          'sugar syrup': 0,
                          'cognac': 40,
                          'amaretto': 28,
                          'absinthe': 50,
                          'cointreau': 40,
                          'dry vermouth': 40,
                          'rye whiskey': 40,
                          'orange curacao': 40,
                          'lillet blonde': 40,
                          'apricot brandy': 40,
                          'raspberry liqueur': 40,
                          'maraschino liqueur': 40,
                          'grenadine': 40,
                          'amaro nonino': 40,
                          'aperol': 40,
                          'vanilla vodka': 40,
                          'passion fruit liqueur': 17,
                          'passion fruit syrup': 0,
                          'passoa': 17,
                          'gin or vodka': 40,
                          "bourbon or rye whiskey": 40,
                          'prosecco': 17, 'jamaican rum': 17, 'mezcal': 17, 'yellow chartreuse': 17, 'green chartreuse': 17, 'coffee liqueur': 17, 'old tom gin': 17, 'golden rum': 17, 'cynar': 16.5}

        # Iterate through each cocktail and calculate ABV
        for name, details in self.cocktail_book.items():
            # Get the ingredients list
            ingredients = details.get("ingredients", [])
            total_volume = 0  # Total liquid volume of the cocktail
            alcohol_volume = 0  # Total alcohol content in the cocktail

            for ingredient in ingredients:
                # Handle non-standard measurements like "dash"
                if "dash" in ingredient:
                    volume = 1  # Assume 1 ml for a dash
                    ingredient_name = ingredient.split("dash")[-1].strip().lower()
                else:
                    # Extract volume and ingredient name using regex
                    match = re.match(r"(\d+)\s*ml\s*(.+)", ingredient)
                    if match:
                        volume = int(match.group(1))
                        ingredient_name = match.group(2).strip().lower()
                    else:
                        continue

                    # If the ingredient has a known ABV, add to alcohol volume
                    if ingredient_name in INGREDIENT_ABV:
                        ingredient_abv = INGREDIENT_ABV[ingredient_name] / 100  # Convert ABV to decimal
                        alcohol_volume += ingredient_abv * volume
                    else:
                        print(f"No ABV found for {ingredient_name}")

                    # Add to total volume
                    total_volume += volume

            # Calculate the ABV for the cocktail
            if total_volume > 0:
                cocktail_abv = (alcohol_volume / total_volume) * 100
            else:
                cocktail_abv = 0  # Handle case where total volume is 0

            # Update the cocktail's ABV
            details["abv"] = round(cocktail_abv, 2)

        # Save the updated cocktail data back to the JSON file
        self.save_to_file()

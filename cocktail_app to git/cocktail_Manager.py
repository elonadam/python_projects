import json
from cocktail import Cocktail  # Assuming the Cocktail class is defined in cocktail.py


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

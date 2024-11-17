class Cocktail:
    """
    Represents a single cocktail recipe.
    """

    def __init__(self, name, abv, is_easy_to_make, ingredients, instructions, personal_notes=None, is_favorite=False,
                 times_made=0, method="Shaken"):
        """
        Initialize a Cocktail instance.

        :param name: str, name of the cocktail
        :param abv: float, Alcohol By Volume percentage
        :param is_easy_to_make: bool, True if it's easy to make, False otherwise
        :param ingredients: list of str, list of ingredients
        :param instructions: str, preparation instructions
        :param personal_notes: str, optional personal notes about the cocktail
        :param is_favorite: bool, whether the cocktail is marked as favorite
        :param times_made: int, count of how many times the cocktail has been made
        :param method: str, preparation method ("Shaken" or "Stirred")
        """
        self.name = name
        self.abv = abv
        self.is_easy_to_make = is_easy_to_make
        self.ingredients = ingredients
        self.instructions = instructions
        self.personal_notes = personal_notes or ""
        self.is_favorite = is_favorite
        self.times_made = times_made
        self.method = method

    def increment_times_made(self):
        """
        Increments the count of times this cocktail has been made.
        """
        self.times_made += 1

    def toggle_favorite(self):
        """
        Toggles the favorite status of the cocktail.
        """
        self.is_favorite = not self.is_favorite

    def display_details(self):
        """
        Prints all details of the cocktail.
        """
        details = f"""
        Name: {self.name}
        ABV: {self.abv}%
        Easy to Make: {'Yes' if self.is_easy_to_make else 'No'}
        Ingredients: {', '.join(self.ingredients)}
        Instructions: {self.instructions}
        Personal Notes: {self.personal_notes}
        Favorite: {'Yes' if self.is_favorite else 'No'}
        Times Made: {self.times_made}
        Method: {self.method}
        """
        print(details)

    def to_dict(self):
        """
        Converts the cocktail's attributes into a dictionary format for storage.
        """
        return {
            "name": self.name,
            "abv": self.abv,
            "is_easy_to_make": self.is_easy_to_make,
            "ingredients": self.ingredients,
            "instructions": self.instructions,
            "personal_notes": self.personal_notes,
            "is_favorite": self.is_favorite,
            "times_made": self.times_made,
            "method": self.method
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a Cocktail instance from a dictionary.
        """
        return cls(
            name=data["name"],
            abv=data["abv"],
            is_easy_to_make=data["is_easy_to_make"],
            ingredients=data["ingredients"],
            instructions=data["instructions"],
            personal_notes=data.get("personal_notes", ""),
            is_favorite=data.get("is_favorite", False),
            times_made=data.get("times_made", 0),
            method=data.get("method", "Shaken")
        )

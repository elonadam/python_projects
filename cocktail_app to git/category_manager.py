

class CategoryManager:
    def __init__(self, cocktail_manager):
        """
        Initialize the CategoryManager with a reference to CocktailManager.
        """
        self.cocktail_manager = cocktail_manager

    def list_cocktails(self):
        """
        Lists all cocktails in the cocktail book.
        """
        if not self.cocktail_book:
            print("No cocktails in the cocktail book.")
        else:
            for name, recipe in self.cocktail_book.items():
                print(f"Name: {name}, ABV: {recipe['abv']}%, Method: {recipe['method']}")

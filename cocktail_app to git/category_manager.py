

# //current have
# //['Mojito', 'Negroni', 'Rubicon', 'Old Fashioned', 'Martini', 'Wet martini', 'Margarita', 'Cosmopolitan', 'Daiquiri', 'Whiskey Sour',
# //'Pina Colada', 'Bellini', 'Black Russian', 'Bloody Mary', 'Caipirinha', 'Champagne Cocktail', 'Corpse Reviver #2',
# //'French 75', 'Mai Tai', 'Pisco Sour', 'Sazerac', 'Sidecar', 'Tom Collins', 'Vesper', 'Zombie', 'Boulevardier',
# //'French Martini', 'Hemingway Special', 'Singapore Sling', 'Last Word', 'Paper Plane', 'Spicy Fifty', "Planter's Punch",
# //'Long Island Iced Tea', 'Porn Star Martini', 'Gin Basil Smash', 'Naked and Famous', 'Amaretto Sour', 'Espresso Martini']

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

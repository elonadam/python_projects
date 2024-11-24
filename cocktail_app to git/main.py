# Create an instance of CocktailManager


# TODO 1 abv auto calculate
# TODO 2 different buttons
# TODO 3 maybe separate gui from real functions
# TODO 4 font color cant be white
# TODO 5 142 line error
# TODO 6 to make my closet with my alchol and then new attribute to each cocktail, which alcogol is needed "vodka,gin"
# TODO 7 function that look what you have and suggest by that cocktials
# https://chatgpt.com/share/67393297-258c-8008-affd-6ba5924a9672
#TODO 9 fix that abv

"""
No ABV found for cranberry juice
No ABV found for bourbon
No ABV found for coconut cream
No ABV found for pineapple juice
No ABV found for white peach puree
No ABV found for tomato juice
No ABV found for cachaֳ§a
No ABV found for chilled champagne
No ABV found for champagne
No ABV found for pisco
No ABV found for pineapple juice
No ABV found for fresh pineapple juice
No ABV found for fresh grapefruit juice
No ABV found for cherry liqueur
No ABV found for pineapple juice
No ABV found for bourbon whiskey
No ABV found for elderflower cordial
No ABV found for honey syrup
No ABV found for sugar cane juice
No ABV found for passion fruit purֳ©e
No ABV found for vanilla syrup
No ABV found for prosecco (served on the side)
No ABV found for egg white (optional for froth)
No ABV found for freshly brewed espresso
"""




from cocktail_Manager import CocktailManager
from category_manager import CategoryManager
from cocktail import Cocktail
from gui import CocktailAppGUI
manager = CocktailManager("cocktail_book.json")
manager.calculate_and_update_abv()
#
# manager = CocktailManager()
#
cocktaill = Cocktail #delete later
if __name__ == "__main__":
    manager = CocktailManager()  # Handles recipes
    app = CocktailAppGUI(manager)  # Starts the GUI
    category_manager = CategoryManager(manager)

    print(manager.extract_cocktail_names())

# Create an instance of CocktailManager


# TODO 1 abv auto calculate
# TODO 2 different buttons
# TODO 3 maybe separate gui from real functions
# TODO 4 font color cant be white
# TODO 5 142 line error
# TODO 6 to make my closet with my alchol and then new attribute to each cocktail, which alcogol is needed "vodka,gin"
# TODO 7 function that look what you have and suggest by that cocktials
# https://chatgpt.com/share/67393297-258c-8008-affd-6ba5924a9672

from cocktail_Manager import CocktailManager
from category_manager import CategoryManager
from cocktail import Cocktail
from gui import CocktailAppGUI

#
# manager = CocktailManager()
#

if __name__ == "__main__":
    manager = CocktailManager()  # Handles recipes
    app = CocktailAppGUI(manager)  # Starts the GUI
    category_manager = CategoryManager(manager)
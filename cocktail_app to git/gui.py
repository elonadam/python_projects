from tkinter import *
from tkinter import messagebox
from cocktail_Manager import CocktailManager  # Replace with your class import
from cocktail import Cocktail  # Replace with your class import

THEME_COLOR = "#F7E1D7"  # Light cream
BUTTON_COLOR_PRIMARY = "#D2691E"  # Chocolate brown
BUTTON_COLOR_SECONDARY = "#C58F6F"  # Soft brown
TEXT_COLOR = "#2C2C2C"  # Dark gray
FONT_HEADER = ("Georgia", 20, "bold")
FONT_BODY = ("Roboto", 14,)
FONT_BUTTON = ("Roboto", 16, "bold")


class CocktailAppGUI:

    def __init__(self, manager: CocktailManager):
        self.manager = manager

        # Window setup
        self.window = Tk()
        self.window.title("Bartender's Cocktail Book")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        # Add an "X" button to close the app
        self.window.protocol("WM_DELETE_WINDOW", self.close_app)

        # Canvas for displaying cocktails
        self.canvas = Canvas(bg="black", width=400, height=300, highlightthickness=0)
        self.canvas_text = self.canvas.create_text(
            200, 150, width=380, text="Welcome to your Cocktail Book!", font=FONT_HEADER
        )
        self.canvas.grid(row=0, column=0, columnspan=3, pady=20)

        # Add a logo to the main screen
        self.logo = PhotoImage(file="logo2.png")  # Ensure the image is in the same directory
        self.logo_label = Label(image=self.logo, bg=THEME_COLOR)
        self.logo_label.grid(row=0, column=0, columnspan=3, pady=20)

        # Icon for add_cocktail button
        add_cocktail_icon_path = "images/add sq.png"  # Make sure this path is correct
        add_cocktail_icon = PhotoImage(file=add_cocktail_icon_path)

        # Buttons
        self.add_button = Button(
            text="Add Cocktail", command=self.add_cocktail, highlightthickness=0, bg="#8B4513", fg="black",
            font=FONT_BUTTON,
            image=add_cocktail_icon,
            compound="top",
        )
        self.add_button.grid(row=0, column=0,padx=10, pady=10)

        self.view_button = Button(
            text="View Cocktails", command=self.view_cocktails, highlightthickness=0, bg="#8B4513", fg="black",
            font=FONT_BUTTON
        )
        self.view_button.grid(row=1, column=0,padx=10, pady=10)

        self.edit_button = Button(
            text="Edit Cocktail", command=self.edit_cocktail, highlightthickness=0, bg="#8B4513", fg="black",
            font=FONT_BUTTON
        )
        self.edit_button.grid(row=0, column=1, pady=20)

        self.search_button = Button(
            text="Search Cocktail", command=self.search_cocktail, highlightthickness=0, bg="#8B4513", fg="black",
            font=FONT_BUTTON
        )
        self.search_button.grid(row=1, column=1,padx =10, pady=10)

        # Make the grid layout responsive
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_columnconfigure(2, weight=1)
        self.window.grid_rowconfigure(3, weight=1)
        self.window.grid_rowconfigure(0, weight=1)

        # Start the GUI loop
        self.window.mainloop()

    def close_app(self):
        """
        Handles the closing of the application when the 'X' button is clicked.
        """
        if messagebox.askyesno("Exit", "Are you sure you want to exit the application?"):
            self.window.destroy()

    def create_scrollable_frame(self, popup):
        """
        Creates a scrollable frame inside a popup window.
        """
        canvas = Canvas(popup, bg="#F7E1D7", highlightthickness=0)
        scrollbar = Scrollbar(popup, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg="#F7E1D7")

        # Configure canvas scroll region to match the frame's size
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Pack canvas and scrollbar
        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        return scrollable_frame

    def create_input_field(self, popup, label_text, row):
        # I have a lot of the same labels so this func make it shorter by making template
        Label(popup, text=label_text, bg=THEME_COLOR, font=FONT_BODY).grid(row=row, column=0, sticky="w")
        entry = Entry(popup, width=30)
        entry.grid(row=row, column=1)
        return entry

    def add_cocktail(self):
        popup = Toplevel(self.window)
        popup.title("Add New Cocktail")
        popup.config(padx=20, pady=20, bg=THEME_COLOR)

        # Input fields
        name_entry = self.create_input_field(popup, "Name:", 0)
        abv_entry = self.create_input_field(popup, "ABV (%):", 1)
        ingredients_entry = self.create_input_field(popup, "Ingredients (comma-separated):", 2)
        instructions_entry = self.create_input_field(popup, "Instructions:", 3)

        Label(popup, text="Is Easy to Make (yes/no):", bg=THEME_COLOR, font=FONT_BODY).grid(row=4, column=0, sticky="w")
        easy_entry = Entry(popup, width=30)
        easy_entry.grid(row=4, column=1)

        Label(popup, text="Method:", bg=THEME_COLOR, font=FONT_BODY).grid(row=5, column=0, sticky="w")
        method_var = StringVar(value="Shaken")
        method_dropdown = OptionMenu(popup, method_var, "Shaken", "Stirred")
        method_dropdown.config(bg="white", font=FONT_BODY)
        method_dropdown.grid(row=5, column=1)

        # # Icon for add button
        # add_cocktail_icon_path = "images/add sq.png"  # Make sure this path is correct
        # add_cocktail_icon = PhotoImage(file=add_cocktail_icon_path)

        # Add button with icon
        add_button = Button(
            popup,
            text="Add",
            command=lambda: self.save_cocktail(
                name_entry.get(),
                abv_entry.get(),
                ingredients_entry.get(),
                instructions_entry.get(),
                easy_entry.get(),
                method_var.get(),
                popup),
            bg=BUTTON_COLOR_PRIMARY
        )
        # add_button.image = add_cocktail_icon  # Prevent garbage collection of the image
        # add_button.grid(row=6, column=0, pady=20)

        # Cancel button
        Button(
            popup,
            text="Cancel",
            command=popup.destroy,
            bg="gray",
            fg="white",
            font=FONT_BUTTON
        ).grid(row=7, column=0, columnspan=2)

        # # Configure row and column resizing for the scrollable content
        # popup.grid_rowconfigure(2, weight=1)
        # popup.grid_columnconfigure(0, weight=1)
        #

    def save_cocktail(self, name, abv, ingredients, instructions, easy, method, popup):
        """
        Saves a new cocktail to the CocktailManager.
        """
        try:
            # Parse inputs
            abv = float(abv)
            ingredients = [item.strip() for item in ingredients.split(",")]
            is_easy = easy.lower() in ["yes", "y", "true"]
            method = method.capitalize()

            # Create and add cocktail
            new_cocktail = Cocktail(
                name=name,
                abv=abv,
                ingredients=ingredients,
                instructions=instructions,
                is_easy_to_make=is_easy,
                method=method,
            )
            self.manager.add_cocktail(new_cocktail)
            messagebox.showinfo(title="Success", message=f"Cocktail '{name}' added!")
            popup.destroy()
        except ValueError:
            messagebox.showerror(title="Error", message="Invalid input. Please check your entries.")

    def view_cocktails(self):
        """
        Displays all cocktails in a new window.
        """
        # Create a new popup window
        popup = Toplevel(self.window)
        popup.title("Cocktail Book")
        popup.config(padx=20, pady=20, bg=THEME_COLOR)

        # List all cocktails
        if not self.manager.cocktail_book:
            Label(popup, text="No cocktails available!", bg=THEME_COLOR, fg="black", font=FONT_BODY).pack()
        else:
            for name, details in self.manager.cocktail_book.items():
                Label(
                    popup,
                    text=f"{name} - {details['method']} - {details['abv']}%",
                    bg=THEME_COLOR,
                    fg="black",
                    font=FONT_BODY,
                ).pack()

    def edit_cocktail(self):
        """
        Opens a popup to select and edit an existing cocktail.
        """
        if not self.manager.cocktail_book:
            messagebox.showinfo("Info", "No cocktails available to edit.")
            return

        # Popup to select a cocktail
        popup = Toplevel(self.window)
        popup.title("Edit Cocktail")
        popup.config(padx=20, pady=20, bg=THEME_COLOR)

        Label(popup, text="Select a Cocktail to Edit:", bg=THEME_COLOR, fg="black", font=FONT_BODY).grid(row=0,
                                                                                                         column=0,
                                                                                                         pady=10)

        # Dropdown to select a cocktail
        cocktail_names = list(self.manager.cocktail_book.keys())
        selected_cocktail = StringVar()
        selected_cocktail.set(cocktail_names[0])  # Default selection

        dropdown = OptionMenu(popup, selected_cocktail, *cocktail_names)
        dropdown.config(bg="#8B4513", fg="black", font=FONT_BODY)
        dropdown.grid(row=1, column=0, pady=10)

        # Continue button
        Button(
            popup,
            text="Edit",
            command=lambda: self.open_edit_form(selected_cocktail.get(), popup),
            bg="#8B4513",
            fg="white",
            font=FONT_BUTTON,
        ).grid(row=2, column=0, pady=20)

    def open_edit_form(self, cocktail_name, parent_popup):
        """
        Opens a form pre-filled with the selected cocktail's details for editing.
        """
        parent_popup.destroy()  # Close the selection popup

        # Get the selected cocktail details
        cocktail = self.manager.get_cocktail(cocktail_name)
        if not cocktail:
            messagebox.showerror("Error", f"Cocktail '{cocktail_name}' not found.")
            return

        # Open edit popup
        popup = Toplevel(self.window)
        popup.title(f"Edit {cocktail_name}")
        popup.config(padx=20, pady=20, bg=THEME_COLOR)

        # Pre-filled fields for each attribute
        Label(popup, text="Name:", bg=THEME_COLOR, fg="black", font=FONT_BODY).grid(row=0, column=0, sticky="w")
        name_entry = Entry(popup, width=30)
        name_entry.insert(0, cocktail["name"])
        name_entry.grid(row=0, column=1)

        Label(popup, text="ABV (%):", bg=THEME_COLOR, fg="black", font=FONT_BODY).grid(row=1, column=0, sticky="w")
        abv_entry = Entry(popup, width=30)
        abv_entry.insert(0, str(cocktail["abv"]))
        abv_entry.grid(row=1, column=1)

        Label(popup, text="Ingredients (comma-separated):", bg=THEME_COLOR, fg="black", font=FONT_BODY).grid(row=2,
                                                                                                             column=0,
                                                                                                             sticky="w")
        ingredients_entry = Entry(popup, width=30)
        ingredients_entry.insert(0, ", ".join(cocktail["ingredients"]))
        ingredients_entry.grid(row=2, column=1)

        Label(popup, text="Instructions:", bg=THEME_COLOR, fg="black", font=FONT_BODY).grid(row=3, column=0, sticky="w")
        instructions_entry = Entry(popup, width=30)
        instructions_entry.insert(0, cocktail["instructions"])
        instructions_entry.grid(row=3, column=1)

        Label(popup, text="Is Easy to Make (yes/no):", bg=THEME_COLOR, fg="black", font=FONT_BODY).grid(row=4, column=0,
                                                                                                        sticky="w")
        easy_entry = Entry(popup, width=30)
        easy_entry.insert(0, "Yes" if cocktail["is_easy_to_make"] else "No")
        easy_entry.grid(row=4, column=1)

        Label(popup, text="Method (Shaken/Stirred):", bg=THEME_COLOR, fg="black", font=FONT_BODY).grid(row=5, column=0,
                                                                                                       sticky="w")
        method_entry = Entry(popup, width=30)
        method_entry.insert(0, cocktail["method"])
        method_entry.grid(row=5, column=1)

        # Submit button to save changes
        Button(
            popup,
            text="Save Changes",
            command=lambda: self.save_changes(
                cocktail_name, name_entry.get(), abv_entry.get(), ingredients_entry.get(),
                instructions_entry.get(), easy_entry.get(), method_entry.get(), popup
            ),
            bg="#8B4513",
            fg="white",
            font=FONT_BUTTON,
        ).grid(row=6, column=0, columnspan=2, pady=20)

    def save_changes(self, old_name, name, abv, ingredients, instructions, easy, method, popup):
        """
        Saves the edited cocktail details to the CocktailManager.
        """
        try:
            # Parse inputs
            abv = float(abv)
            ingredients = [item.strip() for item in ingredients.split(",")]
            is_easy = easy.lower() in ["yes", "y", "true"]

            # Update the cocktail
            updated_data = {
                "name": name,
                "abv": abv,
                "ingredients": ingredients,
                "instructions": instructions,
                "is_easy_to_make": is_easy,
                "method": method.capitalize(),
            }
            self.manager.edit_cocktail(old_name, updated_data)

            # Show success message and close popup
            messagebox.showinfo(title="Success", message=f"Cocktail '{name}' updated successfully!")
            popup.destroy()
        except ValueError:
            messagebox.showerror(title="Error", message="Invalid input. Please check your entries.")

    def search_cocktail(self):
        """
        Opens a popup to search for cocktails by category.
        """
        popup = Toplevel(self.window)
        popup.title("Search Cocktail")
        popup.config(padx=20, pady=20, bg=THEME_COLOR)

        Label(popup, text="Choose a category:", bg=THEME_COLOR, fg="black", font=FONT_BODY).grid(row=0, column=0,
                                                                                                 pady=10)

        categories = ["All Cocktails", "Favorites", "Easy to Make", "Stirred", "Shaken", "Haven't Tried"]
        selected_category = StringVar()
        selected_category.set(categories[0])  # Default selection

        dropdown = OptionMenu(popup, selected_category, *categories)
        dropdown.config(bg="#8B4513", fg="black", font=FONT_BODY)
        dropdown.grid(row=1, column=0, pady=10)
        # Scrollable frame setup
        canvas = Canvas(popup, bg=THEME_COLOR, highlightthickness=0)
        scrollbar = Scrollbar(popup, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg=THEME_COLOR)

        # Bind the scrollable frame to the canvas
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Place the canvas and scrollbar
        canvas.grid(row=2, column=0, sticky="nsew")
        scrollbar.grid(row=2, column=1, sticky="ns")

        # Add search button
        Button(
            popup,
            text="Search",
            command=lambda: self.display_search_results(selected_category.get(), scrollable_frame),
            bg="#8B4513",
            fg="white",
            font=FONT_BUTTON,
        ).grid(row=3, column=0, pady=20)

        # Configure row and column resizing for the scrollable content
        popup.grid_rowconfigure(2, weight=1)
        popup.grid_columnconfigure(0, weight=1)

    def display_search_results(self, category, scrollable_frame):
        """
        Displays the search results as buttons based on the selected category.
        """
        # Clear any existing content in the scrollable frame
        for widget in scrollable_frame.winfo_children():
            widget.destroy()

        # Filter cocktails by category
        if category == "All Cocktails":
            results = list(self.manager.cocktail_book.keys())
        elif category == "Favorites":
            results = [name for name, details in self.manager.cocktail_book.items() if details["is_favorite"]]
        elif category == "Easy to Make":
            results = [name for name, details in self.manager.cocktail_book.items() if details["is_easy_to_make"]]
        elif category == "Stirred":
            results = [name for name, details in self.manager.cocktail_book.items() if details["method"] == "Stirred"]
        elif category == "Shaken":
            results = [name for name, details in self.manager.cocktail_book.items() if details["method"] == "Shaken"]
        elif category == "Haven't Tried":
            results = [name for name, details in self.manager.cocktail_book.items() if details["times_made"] == 0]
        else:
            results = []

        # Populate the scrollable frame with buttons for each cocktail
        if not results:
            Label(scrollable_frame, text="No cocktails found in this category.", bg=THEME_COLOR, fg="black",
                  font=FONT_BODY).pack(pady=10)
        else:
            for name in results:
                # Add a button for each cocktail
                Button(
                    scrollable_frame,
                    text=name,  # Display cocktail name on the button
                    command=lambda n=name: self.confirm_make_cocktail(n),  # Pass the cocktail name to the popup
                    bg="#8B4513",
                    fg="white",
                    font=FONT_BODY,
                    anchor="w"
                ).pack(fill="x", padx=10, pady=5)

    def confirm_make_cocktail(self, cocktail_name):
        """
        Asks the user if they want to make the selected cocktail and handles updates.
        """

        # Confirmation popup
        confirm_popup = Toplevel(self.window)
        confirm_popup.title("Confirm")
        confirm_popup.config(padx=20, pady=20, bg=THEME_COLOR)

        Label(
            confirm_popup,
            text=f"Do you want to make '{cocktail_name}'?",
            bg=THEME_COLOR,
            fg="black",
            font=FONT_BODY,
        ).pack(pady=10)

        Button(
            confirm_popup,
            text="Yes",
            command=lambda: self.make_cocktail(cocktail_name, confirm_popup),
            bg="#8B4513",
            fg="white",
            font=FONT_BODY,
        ).pack(side=LEFT, padx=10)

        Button(
            confirm_popup,
            text="No",
            command=confirm_popup.destroy,
            bg="#8B4513",
            fg="white",
            font=FONT_BODY,
        ).pack(side=RIGHT, padx=10)

    def make_cocktail(self, cocktail_name, parent_popup):
        """
        Displays the cocktail details in a popup and allows adding to favorites or personal notes.
        """
        parent_popup.destroy()

        # Get the cocktail details from the manager
        cocktail = self.manager.cocktail_book[cocktail_name]

        # Update times_made
        self.manager.edit_cocktail(cocktail_name, {"times_made": cocktail["times_made"] + 1})

        # Display the cocktail details
        detail_popup = Toplevel(self.window)
        detail_popup.title(f"{cocktail_name} Details")
        detail_popup.config(padx=20, pady=20, bg=THEME_COLOR)

        # Cocktail details
        details = (
            f"Name: {cocktail_name}\n"
            f"ABV: {cocktail['abv']}%\n"
            f"Ingredients: {', '.join(cocktail['ingredients'])}\n"
            f"Instructions: {cocktail['instructions']}\n"
            f"Favorite: {'Yes' if cocktail['is_favorite'] else 'No'}\n"
            f"Personal Notes: {cocktail.get('personal_notes', 'None')}"
        )

        Label(detail_popup, text=details, bg=THEME_COLOR, fg="black", font=FONT_BODY, justify="left").pack(pady=10)

        # Ask to add to favorites and personal notes
        Label(detail_popup, text="Add to Favorites?", bg=THEME_COLOR, fg="black", font=FONT_BODY).pack(pady=10)

        # Use Radio buttons for explicit Yes/No choice
        self.is_favorite_var = BooleanVar(value=cocktail["is_favorite"])

        Radiobutton(detail_popup, text="Yes", variable=self.is_favorite_var, value=True, bg=THEME_COLOR, fg="black",
                    font=FONT_BODY).pack(anchor="w")
        Radiobutton(detail_popup, text="No", variable=self.is_favorite_var, value=False, bg=THEME_COLOR, fg="black",
                    font=FONT_BODY).pack(anchor="w")

        # Personal notes entry
        Label(detail_popup, text="Add a Personal Note:", bg=THEME_COLOR, fg="black", font=FONT_BODY).pack(pady=10)
        personal_note = Entry(detail_popup, width=40)
        personal_note.insert(0, cocktail.get("personal_notes", ""))  # Pre-fill existing note
        personal_note.pack()

        # Save updates
        Button(
            detail_popup,
            text="Save",
            command=lambda: self.save_additional_updates(
                cocktail_name, self.is_favorite_var.get(), personal_note.get(), detail_popup
            ),
            bg="#8B4513",
            fg="white",
            font=FONT_BUTTON,
        ).pack(pady=20)

    def save_additional_updates(self, cocktail_name, is_favorite, note, popup):
        """
        Saves the additional updates (favorites and personal notes).
        """
        updates = {  # Save favorite status explicitly
            "is_favorite": is_favorite,
        }
        if note.strip():
            updates["personal_notes"] = note.strip()

        self.manager.edit_cocktail(cocktail_name, updates)
        messagebox.showinfo(title="Success", message=f"Cocktail '{cocktail_name}' updated successfully!")
        popup.destroy()

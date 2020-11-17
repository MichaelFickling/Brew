def make_menu(menu_list):
    menu_options = menu_list

    print("\nPlease select an option by entering a number:\n")
    # what did user input as menu choice
    for options in range(len(menu_options)):
        print(f"[{options + 1}] {menu_options[options]}")
    User_selection = input("Enter your selection\n")
    return User_selection

def menu_options():
    User_selection

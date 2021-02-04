from view import terminal as view
from controller import userStory1Controller, userStory2Controller, userStory3Controller, userStory4Controller, \
    userStory5Controller


def load_module(option):
    if option == 1:
        userStory1Controller.run()
    elif option == 2:
        userStory2Controller.run()
    elif option == 3:
        userStory3Controller.run()
    elif option == 4:
        userStory4Controller.run()
    elif option == 5:
        userStory5Controller.run()
    elif option == 0:
        return 0
    else:
        raise KeyError()


def display_menu():
    options = ["Exit program",
               "User Story 1",
               "User Story 2",
               "User Story 3",
               "User Story 4",
               "User Story 5"]
    view.print_menu("Main menu", options)


def menu():
    option = None
    while option != '0':
        display_menu()
        option = view.get_input("Select module")
        load_module(int(option))
    view.print_message("Good-bye!")

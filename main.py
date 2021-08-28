from src.application.recommendations import list_rules, recommend, save_rule


def menu():
    print(
        """
  1- save new rule
  2- list rules
  3- inform the chart
  4- exit
  """
    )

    option = input("Enter your choice: ")
    return option


def main():
    menu_dict = {"1": save_rule, "2": list_rules, "3": recommend, "4": exit}

    while True:
        # clear screen
        print("\033c", end="")
        option = menu()
        menu_dict[option]()


if __name__ == "__main__":
    main()

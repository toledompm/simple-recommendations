from src.application.recommendations import recommend


def menu():
    print(
        """
  1- inform the cart
  2- exit
  """
    )

    option = input("Enter your choice: ")
    return option


def main():
    menu_dict = {"1": recommend, "2": exit}

    while True:
        # clear screen
        print("\033c", end="")
        option = menu()
        menu_dict[option]()


if __name__ == "__main__":
    main()

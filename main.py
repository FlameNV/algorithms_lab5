from find_by_boyer_moore import FindByBoyerMoore


def main():
    input_string = FindByBoyerMoore("Welcome to the jungle baby")
    print(input_string.search("the"))


if __name__ == '__main__':
    main()

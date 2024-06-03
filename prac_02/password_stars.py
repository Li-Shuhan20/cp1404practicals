Min_LENGTH = 8


def main():
    password = get_password()
    asterisks = print_asterisks(password)
    print(f"{asterisks}")


def print_asterisks(password):
    return '*' * len(password)


def get_password():
    while True:
        password = input("Enter a password: ")
        if len(password) >= Min_LENGTH:
            return password
        else:
            print(f"Password must be at least {Min_LENGTH} characters long. Please try again.")


main()

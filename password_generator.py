from random import randint, shuffle, choice


class PasswordGenerator:

    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '^', '=', '*', '+']
        self.password_list = []

    def generate_password(self):

        password_letters = [choice(self.letters) for _ in range(randint(8, 10))]
        password_numbers = [choice(self.numbers) for _ in range(randint(2, 4))]
        password_symbols = [choice(self.symbols) for _ in range(randint(2, 4))]

        self.password_list = password_letters + password_numbers + password_symbols
        shuffle(self.password_list)

        password = "".join(self.password_list)

        return password


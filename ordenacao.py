import string


alphabet = list(string.ascii_uppercase)


def create_entry_file():
    """
    Generates input file (entrada.txt) based on the phrase given.
    """
    frase = "I N T E R C A L A C A O B A L A N C E A D A".upper().split()
    numbers = [str(alphabet.index(char)) for char in frase]

    with open('entrada.txt', 'w') as file:
        print('\n'.join(numbers), file=file)


def get_lines(file_path, line_numbers):
    """
    Returns a tuple with the lines contents based on the index given (list)
        in "line_numbers".

    file_path: path to the file with the content.
    """
    return (x for i, x in enumerate(file_path) if i in line_numbers)


# create_entry_file()

with open('entrada.txt', 'r') as file:
    cont = 3

    lines = get_lines(file, list(range(cont, cont+3)))
    for line in lines:
        print(line.strip())

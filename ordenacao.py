import string


text = "I N T E R C A L A C A O B A L A N C E A D A"
alphabet = list(string.ascii_uppercase)


def create_entry_file(text):
    """
    Generates input file (entrada.txt) based on the phrase given.
    """
    text = text.upper().split()

    numbers = [str(alphabet.index(char)) for char in text]

    with open('entrada.txt', 'w') as file:
        print('\n'.join(numbers), file=file)


def get_lines(file_path, line_numbers):
    """
    Returns a tuple with the lines contents based on the index given (list)
        in "line_numbers".

    file_path: path to the file with the content.
    """
    return (x for i, x in enumerate(file_path) if i in line_numbers)


# create_entry_file(text)

with open('entrada.txt', 'r') as file:
    #TODO: #1 Solve cont variable, list parameter in get_lines function
    cont = 3

    lines = get_lines(file, list(range(cont, cont+3)))
    for line in lines:
        print(line.strip())

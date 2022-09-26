import string


alphabet = list(string.ascii_uppercase)


def arquivo_entrada():
    frase = "I N T E R C A L A C A O B A L A N C E A D A".split()
    numbers = [str(alphabet.index(char)) for char in frase]

    with open('entrada.txt', 'w') as file:
        print('\n'.join(numbers), file=file)


def get_lines(file_path, line_numbers):
    return (x for i, x in enumerate(file_path) if i in line_numbers)


# arquivo_entrada()

with open('entrada.txt', 'r') as file:
    cont = 3

    lines = get_lines(file, list(range(cont, cont+3)))
    for line in lines:
        print(line.strip())

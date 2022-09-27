import os
import shutil
from typing import IO


def swap(input_list: list, first_index: int, second_index: int):
    val_primeiro = input_list[first_index]
    val_segundo = input_list[second_index]
    input_list[first_index] = val_segundo
    input_list[second_index] = val_primeiro


def order_list(input_list: list):
    tamanho = len(input_list)
    if tamanho <= 1:
        return input_list
    if tamanho == 2:
        return [min(input_list), max(input_list)]
    if input_list[0] > input_list[1]:
        swap(input_list, 0, 1)
    if input_list[0] > input_list[2]:
        swap(input_list, 0, 2)
    if input_list[1] > input_list[2]:
        swap(input_list, 1, 2)


def clear_folder(folder: str):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Falha ao deletar arquivo %s. Motivo: %s' % (file_path, e))


def write_to_file(handle: IO, input_list: list):
    stringified = [str(x) for x in input_list]
    handle.write('\n'.join(stringified) + '\n')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    results_folder = './resultados'
    clear_folder(results_folder)

    with open('entrada.txt') as f:
        list_aux = []
        ordered_lists = []
        file_handles = [
            open(f'{results_folder}/fita1.txt', 'w'),
            open(f'{results_folder}/fita2.txt', 'w'),
            open(f'{results_folder}/fita3.txt', 'w'),
        ]

        i = 0
        for line in f:
            list_aux.append(int(line.strip()))
            if len(list_aux) % 3 != 0: continue

            order_list(list_aux)
            index = i % 3
            write_to_file(file_handles[index], list_aux)

            list_aux.clear()
            i += 1

        if len(list_aux) > 0:
            write_to_file(file_handles[-1], list_aux)

        # Fecha todos arquivos, e ao mesmo tempo, abre outro handle para leitura
        for i in range(3):
            file_handles[i].close()
            file_handles[i] = open(file_handles[i].name, 'r')

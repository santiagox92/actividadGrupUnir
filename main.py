"""
License: Apache
Organization: UNIR
"""

import os
import sys
from translate import Translator

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False

def translate_to_english(word, source_lang="es", target_lang="en"):
    translator = Translator(from_lang=source_lang, to_lang=target_lang)
    return translator.translate(word)

def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print("Se debe indicar el fichero como primer argumento")
        print("El segundo argumento indica si se quieren eliminar duplicados")
        sys.exit(1)

    print(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    translated_words = [translate_to_english(word) for word in sort_list(word_list)]
    print(translated_words)

    print(sort_list(word_list))

def limpiar_valores(items):
    return list(filter(None, items))
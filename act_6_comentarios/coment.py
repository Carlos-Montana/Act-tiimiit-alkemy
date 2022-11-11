# Unidad escuela de data engineering de tiimiit - alkemy
# list to work
# lista_inicial = ['perro', 'elefante', 'dragón']
# lista_retorno = [5, 8, 6]


def count_words(names_animals: list) -> list:
    '''
    This function return a new list whith number of characters
    of each item in the list received

    Args:
        names_animals (list): list of names to counts characters

    Returns:
        list: new list whith number of characters
    '''
    return [len(name) for name in names_animals if type(name) is str]


if __name__ == '__main__':
    # begining script
    # This script send list to count number of characters of each items
    names_animals = ['perro', 'elefante', 'dragón', 'hola', 2]
    print(count_words(names_animals))
    print(count_words.__doc__)

lista = [10, 20, 30, 40, 50, 60]


def max_sec(sequence):
    c_list = []
    n_list = []
    for el in sequence:
        if c_list and el - 1 == c_list[-1]:
            c_list.append(el)
        else:
            c_list = []
            c_list.append(el)
        if len(c_list) > len(n_list):
            n_list = c_list
    if len(n_list) == 1:
        return []
    else:
        return n_list


print(max_sec(lista))

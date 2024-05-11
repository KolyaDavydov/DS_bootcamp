def data_types():
    elements = [0, '', 0.0, True, [], {}, (), set()]

    string = '['
    for el in elements:
        string += type(el).__name__ + ', '   
    print(string[0:-2] + ']')


if __name__ == '__main__':
    data_types()
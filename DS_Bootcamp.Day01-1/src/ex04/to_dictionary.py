def list_to_dict():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
        ]
   
    out_dict = {}
    for item, key in list_of_tuples:
        if key not in out_dict:
            out_dict[key] = []
        out_dict[key].append(item)
        
    for key in out_dict:
        for value in out_dict[key]:
            print(f'{key} : {value}')


if __name__ == "__main__":
    list_to_dict()
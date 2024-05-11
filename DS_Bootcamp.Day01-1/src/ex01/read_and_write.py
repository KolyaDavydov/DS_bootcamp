def read_and_write(f_in, f_out):
    with open(f_in, 'r') as file_in:
        with open(f_out, 'w') as file_out:
            file_out.write(file_in.read().replace('","', '"\t"')
                                         .replace('false,', 'false\t')
                                         .replace('true,', 'true\t')
                                         .replace('",', '\t'))


if __name__ == '__main__':
    file_input = 'ds.csv'
    file_output = 'ds.tsv'
    read_and_write(file_input, file_output)
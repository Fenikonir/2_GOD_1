def reverse():
    with open('input.dat', 'rb') as in_file:
        input_bin = in_file.read()
    with open('output.dat', 'wb') as out_file:
        out_file.write(input_bin[::-1])

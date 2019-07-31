def slimp(input):
    print(input)
    if input == '2':
        return input
    return slimp('2')


slimp('1')
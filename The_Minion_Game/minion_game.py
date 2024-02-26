def minion_game(string):
    vowels = ('a', 'e', 'o', 'i', 'u', 'A', 'E', 'O', 'I', 'U')
    Stuart, Kevin = 0, 0
    for i in range(0, len(string)):
        if string[i] in vowels:
            Kevin += len(string) - i
        else:
            Stuart += len(string) - i
    result(Stuart, Kevin)


def result(Stuart, Kevin):
    if Stuart == Kevin:
        print('Draw ')
    elif max(Stuart, Kevin) == Kevin:
        print('Kevin', Kevin)
    else:
        print( 'Stuart', Stuart)


if __name__ == '__main__':
    s = input()
    minion_game(s)
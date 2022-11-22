def fizz_buzz(n:int):
    """

    >>> fizz_buzz(6)
    1
    fizz
    buzz
    fizz
    5
    fizzbuzz

    :param n:
    :return:
    """
    for i in range(1, n + 1):  # i=6 n=6
        if i % 2 == 0 and i % 3 == 0:       #ou if i % 6 == 0:  OU  if i % (2*3) == 0:
            print('fizzbuzz')
        elif i % 2 == 0:
            print('fizz')
        elif i % 3 == 0:
            print('buzz')
        else:
            print(i)    #1  fizz  3  fizz   5  fizz
    # for i in range(1, n + 1):
    #     resultado = ''
    #     if i % 2 == 0:
    #         resultado = 'fizz'
    #     if i % 3 == 0:
    #         resultado += 'buzz'
    #     print(resultado if resultado != '' else i)

if __name__ == '__main__':
    fizz_buzz(10)

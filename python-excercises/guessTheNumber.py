def guessGame():
    import random
    random = random.randint(1,10)
    num = int(input('Prøv å gjett et tall mellom 1-10'))
    if num == random:
        print('ok')
    else:
        print('prøv igjen')
        guessGame()

guessGame()

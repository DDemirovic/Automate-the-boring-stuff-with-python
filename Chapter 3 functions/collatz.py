def collatz():
    print('Please type in any non-decimal number.')
    number = input()
    iteration = 0
    try:
        while int(number) != 1:
            print('Das ist der ', iteration, '. Durchlauf')
            iteration = iteration + 1
            if int(number) % 2 == 0:
                number = int(number)/2
                print(number)    
            else:
                number = int(number)*3 + 1
                print(number)
    except ValueError:
        print('Please do not type in words/decimal numbers.')
collatz()


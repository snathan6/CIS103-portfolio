import random

def powerball():
    num = []
    while len(num)<5:
        n = random.randint(0,69)
        if n not in num:
            num.append(n)
    return num

def mega():
    num = []
    while len(num)<5:
        n = random.randint(0,70)
        if n not in num:
            num.append(n)
    return num

def lucky():
    num=[]
    while len(num)<5:
        n = random.randint(0,45)
        if n not in num:
            num.append(n)
    return num

def lotto():
    num=[]
    while len(num)<6:
        n = random.randint(0,52)
        if n not in num:
            num.append(n)
    return num

def select():
    print('\n-----------Lottery Name----------')
    print('1. Power Ball')
    print('2. Mega Million')
    print('3. Lucky Day Lotto')
    print('4. Lotto')
    print('5. EXIT')

def playing():
    selection = input('Select the Lottery game you would like to play by number: ')
    return selection

def Lotteries(selection):
    if selection == '1':
        numbers = powerball()
        print('Your numbers are: ',numbers)
    elif selection == '2':
        numbers = mega()
        print('Your numbers are: ',numbers)
    elif selection == '3':
        numbers = lucky()
        print('Your numbers are: ',numbers)
    elif selection == '4':
        numbers = lotto()
        print('Your numbers are: ',numbers)
    elif selection == '5':
        print('Goodbye')
        return False
    else:
        print('Invalid. Please make a selection between corresponding games 1-4')
    return True

def main():
    ans = 'y'
    while(ans == 'y' or ans == 'Y'):
        select()
        userselection = playing()
        lp = Lotteries(userselection)
        if not lp:
            break
        ans = input('Again? y/n: ')

main()

def total(n):
    print(n, end='')
    if n <= 1:
        print(' = ', end='')
        return n
    else:
        print('+', end='')
        return n + total(n - 1)

def main():
    choice = 'y'
    while choice == 'y' or choice == 'Y':
        try:
            n = int(input("Enter a number: "))
            if n < 0:
                print("Number cannot be negative")
            else:
                print(total(n))
        except:
            print("Invalid input detected")
        choice = input("Another number (y/n): ")

main()

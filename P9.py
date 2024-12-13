def distance():
    try:
        m=float(input('Enter the distance in miles:'))
        k=m* 1.609344
        print('Distance in kilometers is: ',k)
        return
    except:
        print('unknown error')

def temp():
    try:
        f=float(input('Enter temperature in farenheit:'))
        c=(f-32) * 5/9
        print('Temperature in celsisus: ',c)
        return
    except:
        print('Unkown error')
def weight():
    try:
        lb=float(input('enter the weight in pounds:'))
        kg=lb * 0.45359237
        print('weight in kilograms is:',kg)
    except:
        print('Unknown error')
def main():
    a='y'
    while (a=='y' or a=='Y'):
        distance()
        temp()
        weight()
        a=input('Try Again? y/n:')

main()
        
        

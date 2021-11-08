import random

def get_lights(number):
    return [random.choice(['1','O']) for i in range(number)]

def getnumber():
    while True:
        try:
            number=int(input('Number of lights: '))
            return number
        except:
            print('Try Again')

def getchange(number):
    while True:
        try:
            index=int(input('Which one do you want to change?(press 0 to exit)'))
            if 0<=index and index<=number:
                return index
            else:
                print('Index out of range')
        except:print('Try Again')

def changelights(index,lights):
    if lights[index - 1] == '1':
        lights[index - 1] = 'O'
    else:
        lights[index - 1] = '1'

    if index ==1:
        if lights[1] == '1':
            lights[1] = 'O'
        else:
            lights[1] = '1'
    elif index==len(lights):
        if lights[index-2] == '1':
            lights[index-2] = 'O'
        else:
            lights[index-2] = '1'
    else:
        if lights[index-2]=='1':
            lights[index-2]='O'
        else:
            lights[index-2]='1'
        if lights[index]=='1':
            lights[index]='O'
        else:
            lights[index]='1'

def main():
    number = getnumber()
    lights = get_lights(number)
    while True:
        print('Lights: {}'.format(' '.join(lights)))
        if '1' not in lights:
            print('You won!')
            break
        index = getchange(number)
        if index==0:
            if '1' in lights:
                print('Try one more time :)')
                break
        else:
            changelights(index,lights)

main()

from builtins import input


def div_check(x, y):
    try:
        x / y
    except ZeroDivisionError:
        return True
    else:
        return False

if __name__ == '__main__':
    x = int(input('x: '))
    y = int(input('y: '))
    print(div_check(x, y))

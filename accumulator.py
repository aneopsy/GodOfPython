def accumulator(sum):
    def f(n):
        f.sum += n
        return f.sum
    f.sum = sum
    return f

if __name__ == '__main__':
    x = accumulator(0)
    x(1)
    x(10)
    print(x(0))
    print(x(-11))
    x(5)
    print(x(2.3))

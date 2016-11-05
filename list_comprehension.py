
funcs = [lambda i=i: i * i for i in range(10)]
for i in range(10):
    print funcs[i]()

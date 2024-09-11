def add_everything_up(a, b):
    try:
        print(a + b)
    except TypeError:
        a = str(a)
        c = a + b
        print(c)

add_everything_up(1, '2')

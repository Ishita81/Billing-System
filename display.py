CONSOLE_WIDTH = 80

def heading(string: str = "DEPARTMENTAL STORE") -> None:
    print(string.center(CONSOLE_WIDTH))
    underline = ''.join(['_'for i in string])
    print(underline.center(CONSOLE_WIDTH))

def subheading(string: str) -> None:
    print()
    print(string)

    for i in range(len(string)):
        print('-', end = '')

    print()

def table_header(*cols) -> None:
    print()
    n = len(cols) - 1

    for i in range(len(cols)):
        n += cols[i][1]

        if i < len(cols) - 1:
            print(cols[i][0].ljust(cols[i][1]), end = ' ')
        else:
            print(cols[i][0])

    for i in range(n):
        print('-', end = '')

    print()

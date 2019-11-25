import string

def print_rangoli(size):
    st = string.ascii_lowercase[:size]
    height = size * 2 - 1
    width = size * 4 - 3
    lines = [None] * height

    for i in range(size):
      rev = st[(-i - 1):]
      letters = ''.join(reversed(rev)) + rev[1:]
      lines[i] = lines[-i -1] = '-'.join(letters).center(width, '-')

    print(*lines, sep='\n')
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
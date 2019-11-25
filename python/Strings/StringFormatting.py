def print_formatted(number):
    output = ""
    fmt = len(format(number, 'b'))

    for i in range(number):
      num = i + 1
      dec = str(num)
      octa = format(num, 'o')
      hexa = format(num, 'x').upper()
      bina = format(num, 'b')

      output = output + dec.rjust(fmt) + " " + octa.rjust(fmt) + " " + hexa.rjust(fmt) + " " + bina.rjust(fmt) + "\n"
    print(output)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
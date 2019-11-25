def containsAlNum(string):
  for i in range(len(string)):
    if (string[i].isalnum()):
      return True
      break
  return False


def containsAlpha(string):
  for i in range(len(string)):
    if (string[i].isalpha()):
      return True
      break
  return False


def containsDigit(string):
  for i in range(len(string)):
    if (string[i].isdigit()):
      return True
      break
  return False


def containsLower(string):
  for i in range(len(string)):
    if (string[i].islower()):
      return True
      break
  return False


def containsUpper(string):
  for i in range(len(string)):
    if (string[i].isupper()):
      return True
      break
  return False


if __name__ == '__main__':
    s = input()
    print(containsAlNum(s))
    print(containsAlpha(s))
    print(containsDigit(s))
    print(containsLower(s))
    print(containsUpper(s))

from collections import OrderedDict


def merge_the_tools(string, k):
      ret = ""
      lenstr = len(string)
      lenword = lenstr // k

      for i in range(lenword):
            word = string[i * k:(i+1)*k]
            print(''.join(OrderedDict.fromkeys(word)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

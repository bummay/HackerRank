import textwrap

def wrap(string, max_width):
    ret = ""
    s_wrap_list = textwrap.wrap(string, max_width)

    for item in s_wrap_list:
      ret = ret + item + "\n"

    return ret

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
import re

def count_substring(string, sub_string):
    cnt = 0
    pos = 0
    st = string[pos:]
    while len(sub_string) <= len(st):
      pos = st.find(sub_string)
      if(pos < 0):
        break
      else:
        cnt = cnt + 1
        st = st[pos+1:]
    return str(cnt)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

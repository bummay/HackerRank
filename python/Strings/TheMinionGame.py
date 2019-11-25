def minion_game(string):
      vowels = ["A", "I", "U", "E", "O"]
      n = len(string)
      # found = []
      stuart = 0
      kevin = 0
      # target = ""

      for i in range(n):
            if string[i] in vowels:
                  kevin += n - i
            else:
                  stuart += n - i

      if kevin < stuart:
            print("Stuart " + str(stuart))
      elif kevin > stuart:
            print("Kevin " + str(kevin))
      else:
            print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
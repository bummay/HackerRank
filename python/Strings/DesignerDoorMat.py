lines, width = (int(x) for x in input().split())
blank = '-'
base = ".|."
times = lines // 2
ret = ""

for i in range(times):
  pattern = base * (i * 2 + 1)
  ret = ret + pattern.center(width, blank) + "\n"

ret = ret + "WELCOME".center(width, blank) + "\n"

for i in range(times):
  pattern = base * (lines - (2 * (i + 1)))
  ret = ret + pattern.center(width, blank) + "\n"

print(ret)

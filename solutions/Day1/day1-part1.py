def findDigitInLine(line):
  leftNum = None
  rightNum = None

  lenLine = len(line)

  for i in range(lenLine):
    if line[i].isdigit():
      leftNum = line[i]
      break

  for i in range(lenLine - 1, -1, -1):
    if line[i].isdigit():
      rightNum = line[i]
      break

  return str(leftNum) + str(rightNum)

file = open('inputs.txt', 'r')
count = 0
for line in file:
  count += int(findDigitInLine(line))

print(count)
file.close()

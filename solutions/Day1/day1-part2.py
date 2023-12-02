alphaNums = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def isDigitNotZero(char):
  if char.isdigit():
    if int(char) == 0:
      return False
    else:
      return True
  else:
    return False


def reversedAlphaNums():
  reversedAlNums = {}
  for alphaNum in alphaNums:
    reversedAlNums[alphaNum[::-1]] = alphaNums[alphaNum]

  return reversedAlNums


revAlphaNums = reversedAlphaNums()


def alphaNumSplit():
  numArray = []
  for alphaNum in alphaNums:
    charString = ""
    for char in alphaNum:
      charString += char
      numArray.append(charString)

    charString = ""
    for char in alphaNum[::-1]:
      charString += char
      numArray.append(charString)

  return list(set(numArray))


chunksAlphaNums = alphaNumSplit()


def scanLine(line, reverse=False):
  leftPointer = 0
  rightPointer = leftPointer + 1
  lenLine = len(line)

  while leftPointer < lenLine and rightPointer < lenLine:
    if isDigitNotZero(line[leftPointer]):
      return line[leftPointer]

    if isDigitNotZero(line[rightPointer]):
      return line[rightPointer]

    subString = line[leftPointer:rightPointer + 1]
    print(subString)
    if (reverse is False) and (subString in alphaNums):
      return alphaNums[subString]
    elif (reverse is True) and (subString in revAlphaNums):
      return revAlphaNums[subString]
    elif subString in chunksAlphaNums:
      rightPointer += 1
    else:
      leftPointer += 1
      rightPointer = leftPointer + 1


def findDigitInLine(line):
  leftNum = str(scanLine(line))
  rightNum = str(scanLine(line[::-1], True))

  return int(leftNum + rightNum)

file = open('inputs.txt', 'r')
count = 0
for line in file:
  val = findDigitInLine(line)
  print(line, val)
  count += int(val)

print(count)
file.close()


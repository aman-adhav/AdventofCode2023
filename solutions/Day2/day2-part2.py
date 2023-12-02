def getColoursAsHash(config):
  colours = {"red": 0, "green": 0, "blue": 0}
  configSplit = config.split(', ')

  for stringColour in configSplit:
    if 'red' in stringColour:
      colours['red'] = int(stringColour.split(' red')[0])
    elif 'blue' in stringColour:
      colours['blue'] = int(stringColour.split(' blue')[0])
    elif 'green' in stringColour:
      colours['green'] = int(stringColour.split(' green')[0])

  return colours


def compareToMaxColourConfig(newHash, oldHash):

  if newHash['red'] > oldHash['red']:
    oldHash['red'] = newHash['red']

  if newHash['green'] > oldHash['green']:
    oldHash['green'] = newHash['green']

  if newHash['blue'] > oldHash['blue']:
    oldHash['blue'] = newHash['blue']


def multiplyMaxGameConfigValues(hash):
  return hash['red'] * hash['green'] * hash['blue']


def findMaxGameConfig(configs):
  maxColourConfig = {'red': 0, 'green': 0, 'blue': 0}

  for config in configs:
    colourHash = getColoursAsHash(config)
    compareToMaxColourConfig(colourHash, maxColourConfig)

  return maxColourConfig


file = open('inputs.txt', 'r')

colour = 0

for line in file:
  lineSplit = line.split(': ')
  game = int(lineSplit[0].split('Game ')[1])
  configs = lineSplit[1].split("; ")
  colour += multiplyMaxGameConfigValues(findMaxGameConfig(configs))

print(colour)
file.close()



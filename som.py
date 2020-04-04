import random

MIN_SOM = 1
PLUS_SOM = 0

def somSoort(somKeus):
    return random.randint(PLUS_SOM, MIN_SOM) if somKeus is None else somKeus

def getAB(somType):
    if (somType == MIN_SOM):
        return [random.randint(11, 19), random.randint(1, 9)]
    else:
        return [random.randint(1, 9), random.randint(1, 9)]

def strSom(som):
    if (som[2] == MIN_SOM):
        return str(som[0]) + " - " + str(som[1]) + " = "
    else:
        return str(som[0]) + " + " + str(som[1]) + " = "

def doSom(som):
    if (som[2] == MIN_SOM):
        return som[0] - som[1]
    else:
        return som[1] + som[0]

def checkSom(som, ans):
    return doSom(som) == ans

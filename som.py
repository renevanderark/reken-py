import random

MIN_SOM = 1
PLUS_SOM = 0

def somSoort(somKeus):
    return random.randint(PLUS_SOM, MIN_SOM) if somKeus is None else somKeus

def getAB(aRngMin, aRngMax, bRngMin, bRngMax):
    return [random.randint(aRngMin, aRngMax), random.randint(bRngMin, bRngMax)]

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

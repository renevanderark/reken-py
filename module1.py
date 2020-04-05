import time
import sys
from som import MIN_SOM, PLUS_SOM, strSom, checkSom, getAB, somSoort
from termi import animateLines, clear, countDown, setColor, DEFAULT_COLOR, GREEN, RED

def getSom(somKeus = None):
    somType = somSoort(somKeus)

    if somType == MIN_SOM:
        [a, b] = getAB(11, 19, 1, 9)
        while (a - b > 9):
            [a, b] = getAB(11, 19, 1, 9)
        return [a, b, somType]
    else:
        [a, b] = getAB(1, 9, 1, 9)
        while (a + b < 11 or a == b):
            [a, b] = getAB(1, 9, 1, 9)
        return [a, b, somType]

def printSplits(som, metExtras = False):
    if (som[2] == MIN_SOM):
        rest = som[0] % 10
    else:
        rest = 10 - som[0]

    print("                " + str(som[1]))
    setColor(GREEN)
    print("              ╭─┴─╮")
    print("              │   │")
    setColor(DEFAULT_COLOR)
    if (metExtras):
        if (som[2] == PLUS_SOM):
            print("          " + str(som[0]) + " + " + str(rest) + " + " + str(som[1] - rest) + " = ?")
        else:
            print("         " + str(som[0]) + " - " + str(rest) + " - " + str(som[1] - rest) + " = ?")
    else:
        print("              " + str(rest) + "   " + str(som[1] - rest))

def printHint(som, foutCount):
    printSplits(som)
    animateLines(8)
    y = 10 if foutCount < 2 else 9
    for x in range(y):
        clear()
        printSplits(som, x % 2 == 0)
        animateLines(8, 0)
        time.sleep(1 if x == 8 else 0.1)

def animateSom(som, ans):
    wasGoed = checkSom(som, ans)
    for n in range(10):
        clear()
        for x in range(n):
            print(' ', end = '')
        print(strSom(som), end = '')
        setColor(GREEN if wasGoed else RED)
        print("?" if ans == -1 else str(ans), end = '')
        setColor(DEFAULT_COLOR)
        sys.stdout.flush()
        time.sleep(0.05)
    return wasGoed

def printSomFeedback(wasGoed):
    if wasGoed:
        print(" --> IS GOED!! *")
    else:
        print(" --> is fout...")
    animateLines(8)
    countDown(3)

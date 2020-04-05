import time
import sys
from som import MIN_SOM, PLUS_SOM, strSom, checkSom, getAB, somSoort, getTypeChar
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

def printSplits(som, metExtras = False, lpad = 10, printTeSplitsen = True):
    if (som[2] == MIN_SOM):
        rest = som[0] % 10
    else:
        rest = 10 - som[0]

    if printTeSplitsen:
        print((" " * lpad) + "      " + str(som[1]))
    setColor(GREEN)
    print((" " * lpad) + "    ╭─┴─╮")
    print((" " * lpad) + "    │   │")
    setColor(DEFAULT_COLOR)
    if (metExtras):
        if (som[2] == PLUS_SOM):
            print((" " * lpad) + str(som[0]) + " + " + str(rest) + " + " + str(som[1] - rest) + " = ?")
        else:
            print((" " * (lpad-1)) + str(som[0]) + " - " + str(rest) + " - " + str(som[1] - rest) + " = ?")
    else:
        print((" " * lpad) + "    " + str(rest) + "   " + str(som[1] - rest))

def printHint(som, foutCount):
    print(strSom(som))
    animateLines(8)
    for x in range(9):
        clear()
        print(str(som[0]) + " " + getTypeChar(som[2]) + " ", end = "")
        if x % 2 == 0:
            print(str(som[1]) + " = ")
        else:
            print("  = ")
        animateLines(8, 0)
        time.sleep(0.2)

    for x in range(9):
        clear()
        if x % 2 == 0:
            print("       " + str(som[1]))
        else:
            print()
        animateLines(2, 0)
        print(strSom(som))
        animateLines(8, 0)
        time.sleep(0.2)
    clear()
    printSplits(som, True, 1)
    animateLines(7, 0)

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

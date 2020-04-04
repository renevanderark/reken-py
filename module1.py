import time
import sys
from som import MIN_SOM, PLUS_SOM, strSom, checkSom
from termi import animateLines, clear, countDown

def printSplits(som, metExtras = False):
    if (som[2] == MIN_SOM):
        rest = som[0] % 10
    else:
        rest = 10 - som[0]
    print("                " + str(som[1]))
    print("              ╭─┴─╮")
    print("              │   │")
    if (metExtras):
        if (som[2] == PLUS_SOM):
            print("          " + str(som[0]) + " + " + str(rest) + " + " + str(som[1] - rest))
        else:
            print("         " + str(som[0]) + " - " + str(rest) + " - " + str(som[1] - rest))
    else:
        print("              " + str(rest) + "   " + str(som[1] - rest))

def printHint(som):
    printSplits(som)
    animateLines(8)
    time.sleep(1.5)
    for x in range(10):
        clear()
        printSplits(som, x % 2 == 0)
        animateLines(8, 0)
        time.sleep(3 if x == 8 else 0.1)

def animateSom(som, ans):
    for n in range(10):
        clear()
        for x in range(n):
            print(' ', end = '')
        print(strSom(som), end = '')
        print("?" if ans == -1 else str(ans), end = '')
        sys.stdout.flush()
        time.sleep(0.05)
    return checkSom(som, ans)

def printSomFeedback(wasGoed):
    if wasGoed:
        print(" --> IS GOED!! *")
    else:
        print(" --> is fout...")
    animateLines(8)
    countDown(3)

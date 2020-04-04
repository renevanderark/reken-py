#!/usr/bin/python3

import sys
import random
import time

MIN_SOM = 1
PLUS_SOM = 0


def getAB(somType):
    if (somType == MIN_SOM):
        return [random.randint(11, 19), random.randint(1, 9)]
    else:
        return [random.randint(1, 9), random.randint(1, 9)]

def getSom():
    somType = random.randint(PLUS_SOM, MIN_SOM)
    [a, b] = getAB(somType)
    if somType == MIN_SOM:
        while (a - b > 9):
            [a, b] = getAB(somType)
        return [a, b, somType]
    else:
        while (a + b < 11 or a == b):
            [a, b] = getAB(somType)
        return [a, b, somType]

def animateLines(x, delay = 0.07):
    for n in range(x):
        print("")
        time.sleep(delay)


def strSom(som):
    if (som[2] == 1):
        return str(som[0]) + " - " + str(som[1]) + " = "
    else:
        return str(som[0]) + " + " + str(som[1]) + " = "

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


def doSom(som):
    if (som[2] == 1):
        return som[0] - som[1]
    else:
        return som[1] + som[0]

def checkSom(som, ans):
    return doSom(som) == ans

def clear():
    print(chr(27) + "[2J")

def printBalk(curSom, amtSom):
    print("|", end = '')
    for x in range(curSom - 1):
        print("=", end = '')
    for x in range(amtSom - curSom + 1):
        print(".", end = '')
    print("| " + str(int((curSom - 1) / amtSom * 100)) + "%")

som = getSom()
clear()
amtSom = 20 if len(sys.argv) < 2 else int(sys.argv[1])
curSom = 1
printBalk(curSom, amtSom)

while True:
    try:
        ans = int(input(strSom(som)))
    except:
        ans = -1
        print("kan ik niet parsen")
        pass


    for n in range(10):
        clear()
        for x in range(n):
            print(' ', end = '')
        print(strSom(som), end = '')
        print("?" if ans == -1 else str(ans), end = '')
        sys.stdout.flush()
        time.sleep(0.05)

    wasGoed = checkSom(som, ans)
    if wasGoed:
        print(" --> IS GOED!! *")
    else:
        print(" --> is fout...")

    animateLines(8)

    print("3 ", end = '')
    sys.stdout.flush()
    time.sleep(0.7)
    print("2 ", end = '')
    sys.stdout.flush()
    time.sleep(0.7)
    print("1 ", end = '')
    sys.stdout.flush()
    time.sleep(0.7)

    clear()
    if wasGoed:
        if (curSom == amtSom):
            printBalk(curSom + 1, amtSom)
            animateLines(11, 0.08)
            print(":)")
            break
        som = getSom()
        curSom += 1
    else:
        printSplits(som)
        animateLines(8)
        time.sleep(1.5)
        for x in range(10):
            clear()
            printSplits(som, x % 2 == 0)
            animateLines(8, 0)
            time.sleep(3 if x == 8 else 0.1)
    printBalk(curSom, amtSom)

import time
import sys

def animateLines(x, delay = 0.07):
    for n in range(x):
        print("")
        time.sleep(delay)

def clear():
    print(chr(27) + "[2J")

def printBalk(curSom, amtSom):
    print("|", end = '')
    for x in range(curSom - 1):
        print("=", end = '')
    for x in range(amtSom - curSom + 1):
        print(".", end = '')
    print("| " + str(int((curSom - 1) / amtSom * 100)) + "%")

def countDown(amt):
    for x in range(amt, 0, -1):
        print(str(x) + " ", end = '')
        sys.stdout.flush()
        time.sleep(0.7)

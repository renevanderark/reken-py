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
    setColor(GREEN)
    for x in range(curSom - 1):
        print("=", end = '')
    setColor(RED)
    for x in range(amtSom - curSom + 1):
        print(".", end = '')
    setColor(DEFAULT_COLOR)
    print("| " + str(int((curSom - 1) / amtSom * 100)) + "%")

def countDown(amt):
    for x in range(amt, 0, -1):
        print(str(x) + " ", end = '')
        sys.stdout.flush()
        time.sleep(0.7)

DEFAULT_COLOR = "255"
GREEN = "154"
RED = "202"
def setColor(code):
    print(chr(27) + "[38;5;" + code + "m", end = "")

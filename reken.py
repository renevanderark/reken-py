#!/usr/bin/python3

import sys
import time
from som import strSom, PLUS_SOM, MIN_SOM, getSom
from termi import animateLines, clear, printBalk
from module1 import printHint, animateSom, printSomFeedback


clear()

try:
    amtSom = int(input("Hoe veel sommen wil je maken? "))
except:
    amtSom = 20

somKeusStr = input("Wat voor sommen wil je maken? + of - of ? ")
somKeus = None
if somKeusStr == '+':
    somKeus = PLUS_SOM
elif somKeusStr == '-':
    somKeus = MIN_SOM

som = getSom(somKeus)
curSom = 1
printBalk(curSom, amtSom)

while True:
    try:
        inp = input(strSom(som))
        if inp == "q":
            break
        ans = int(inp)
    except:
        ans = -1

    wasGoed = animateSom(som, ans)

    printSomFeedback(wasGoed)


    clear()

    if wasGoed:
        if (curSom == amtSom):
            printBalk(curSom + 1, amtSom)
            animateLines(11, 0.08)
            print(":)")
            break
        som = getSom(somKeus)
        curSom += 1
    else:
        printHint(som)

    printBalk(curSom, amtSom)

#!/usr/bin/python3

import sys
import time
from som import strSom, PLUS_SOM, MIN_SOM
from termi import animateLines, clear, printBalk
import module1

modules = [module1]

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

mijnModule = modules[0]

som = mijnModule.getSom(somKeus)
curSom = 1
foutCount = 0
printBalk(curSom, amtSom)
while True:
    try:
        inp = input(strSom(som))
        if inp == "q":
            break
        ans = int(inp)
    except:
        ans = -1

    wasGoed = mijnModule.animateSom(som, ans)

    mijnModule.printSomFeedback(wasGoed)


    clear()

    if wasGoed:
        if (curSom == amtSom):
            printBalk(curSom + 1, amtSom)
            animateLines(11, 0.08)
            print(":)")
            break
        som = mijnModule.getSom(somKeus)
        curSom += 1
        foutCount = 0
    else:
        foutCount += 1
        mijnModule.printHint(som, foutCount)

    printBalk(curSom, amtSom)

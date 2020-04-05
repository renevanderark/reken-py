#!/usr/bin/python3

import sys
import time
from som import strSom, PLUS_SOM, MIN_SOM
from termi import animateLines, clear, printBalk, DEFAULT_COLOR, setColor
import module1
import module2

modules = [module1, module2]

clear()
setColor(DEFAULT_COLOR)
try:
    moduleKeus = int(input("Moeilijkheid: 1 of 2? ")) - 1
except:
    moduleKeus = 0

if (moduleKeus < 0 or moduleKeus > len(modules) - 1):
    moduleKeus = 0

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

mijnModule = modules[moduleKeus]

som = mijnModule.getSom(somKeus)
curSom = 1
foutCount = 0
clear()
printBalk(curSom, amtSom)
while True:
    try:
        inp = input(strSom(som))
        if inp == "q":
            break
        ans = int(inp)
    except:
        ans = -1

    if ans > -1:
        wasGoed = mijnModule.animateSom(som, ans)
        mijnModule.printSomFeedback(wasGoed)
    else:
        wasGoed = False


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

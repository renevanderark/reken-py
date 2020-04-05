import time
from som import MIN_SOM, PLUS_SOM, strSom, checkSom, getAB, somSoort
from termi import animateLines, clear, countDown, setColor, DEFAULT_COLOR, GREEN, RED
import module1

def getSom(somKeus = None):
    somType = somSoort(somKeus)

    if somType == MIN_SOM:
        [a, b] = getAB(20, 50, 10, 30)
        while (a < b or (a % 10) >= (b % 10) or a % 10 == 0 or b % 10 == 0):
            [a, b] = getAB(20, 50, 10, 30)
        return [a, b, somType]
    else:
        [a, b] = getAB(10, 40, 10, 40)
        while (a == b or (a % 10) + (b % 10) < 11):
            [a, b] = getAB(10, 40, 10, 40)
        return [a, b, somType]

def printPlusHint(som, foutCount):
    print(strSom(som))
    animateLines(8)
    time.sleep(1)
    aTiental = som[0] - som[0] % 10
    bTiental = som[1] - som[1] % 10
    aVerschil = som[0] - aTiental
    bVerschil = som[1] - bTiental
    verschillen = [aVerschil, bVerschil]
    tientalSom = [som[0], som[1], som[2]]
    restSom = [0, 0, som[2]]
    for i in range(len(verschillen)):
        for x in range(verschillen[i]):
            tientalSom[i] -= 1
            restSom[i] += 1
            print(strSom(tientalSom))
            print(" " + str(restSom[0]) + " +  " + str(restSom[1]) + " =")
            animateLines(7, 0)
            time.sleep(0.2)
            clear()

    if (foutCount > 1):
        clear()
        module1.printSplits(restSom)
        print(strSom(tientalSom))
        print(" " + str(restSom[0]) + " +  " + str(restSom[1]) + " =")
        animateLines(6,0)

def printHint(som, foutCount):
    if som[2] == PLUS_SOM:
        printPlusHint(som, foutCount)
    else:
        setColor(RED)
        print("Ik heb nog geen hint :(")
        setColor(DEFAULT_COLOR)
        animateLines(8)

def animateSom(som, ans):
    return module1.animateSom(som, ans)

def printSomFeedback(wasGoed):
    module1.printSomFeedback(wasGoed)

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
            clear()
            tientalSom[i] -= 1
            restSom[i] += 1
            print(strSom(tientalSom) + "...")
            print(" " + str(restSom[0]) + " +  " + str(restSom[1]) + " = ...")
            animateLines(7, 0)
            time.sleep(0.2)

    if (foutCount > 1):
        for x in range(9):
            clear()
            print(strSom(tientalSom))
            print(" " + str(restSom[0]) + " +  " + str(restSom[1]) + " =")
            if x % 2 == 0:
                module1.printSplits(restSom, foutCount > 2, 0, False)
                animateLines(4, 0)
            else:
                animateLines(7, 0)
            time.sleep(0.1)

def printMinHint(som, foutCount):
    print(strSom(som))
    animateLines(8)
    time.sleep(1)
    bTiental = som[1] - som[1] % 10
    bVerschil = som[1] - bTiental
    ba = som[1]
    bb = 0
    for x in range(bVerschil):
        clear()
        ba -= 1
        bb += 1
        print(str(som[0]) + " - " + str(ba) + " - " + str(bb) + " = ")
        animateLines(8, 0)
        time.sleep(0.2)

    if (foutCount > 1):
        for x in range(9):
            clear()
            print(str(som[0]) + " - " + str(ba) + " - " + str(bb) + " = ", end = "")
            if x % 2 == 0:
                print(str(som[0] - ba) + " - " + str(bb) + " = ...")
                if foutCount > 2:
                    module1.printSplits([som[0] - ba, bb, MIN_SOM], False, 13, False)
            else:
                print()

            if foutCount > 2 and x % 2 == 0:
                animateLines(5, 0)
            else:
                animateLines(8, 0)
            time.sleep(0.1)


def printHint(som, foutCount):
    if som[2] == PLUS_SOM:
        printPlusHint(som, foutCount)
    else:
        printMinHint(som, foutCount)

def animateSom(som, ans):
    return module1.animateSom(som, ans)

def printSomFeedback(wasGoed):
    module1.printSomFeedback(wasGoed)

from random import randint

import pygame

WIDTH = 801
HEIGHT = 601

rød = 'rødprikk'
gul = 'gulprikk'
grønn = 'grønnprikk'
hvit = 'hvitprikk'
blå = 'blåprikk'
svart = 'svartprikk'
oransje = 'oransjeprikk'
rosa = 'rosaprikk'
alleFarger = [rød, gul, grønn, hvit, blå, svart, oransje, rosa]


#gjett1 = Actor(alleFarger[randint(0,7)], (75, 100))
#gjett2 = Actor(alleFarger[randint(0,7)], (200, 100))
#gjett3 = Actor(alleFarger[randint(0,7)], (340, 100))
#gjett4 = Actor(alleFarger[randint(0,7)], (460, 100))
gjett1 = Actor(hvit, (75, 100))
gjett2 = Actor(hvit, (225, 100))
gjett3 = Actor(hvit, (375, 100))
gjett4 = Actor(hvit, (525, 100))
alleGjett = [gjett1,gjett2,gjett3,gjett4]

riktigFargePaRiktigPlass = 'riktig farge på riktig plass'
riktigFargePaFeilPlass = 'riktig farge på feil plass'

ferdigKnapp = Actor('alien', (675, 100))

hemmeligKode = [alleFarger[randint(0,7)], alleFarger[randint(0,7)], alleFarger[randint(0,7)], alleFarger[randint(0,7)]]

gjetninger = []

firkant = Rect((20,20),(50,50))

def draw():
    screen.clear()
    gjett1.draw()
    gjett2.draw()
    gjett3.draw()
    gjett4.draw()
    ferdigKnapp.draw()
    screen.draw.filled_rect(firkant, "red")



#
def on_mouse_down(pos):

    for gjett in alleGjett:
        if gjett.collidepoint(pos):
            gjett.image = alleFarger[(alleFarger.index(gjett.image) + 1) % len(alleFarger)]
            # print("bytter farge til " + gjett.image)

    if ferdigKnapp.collidepoint(pos):
        gjetninger.append([gjett1.image, gjett2.image, gjett3.image, gjett4.image])
        print("ferdig med gjetning: " + str(len(gjetninger)))
        print(gjetninger[len(gjetninger) - 1])
        sjekkKodeOgGiTilbakemelding()
        flyttGjetninger()

    if firkant.collidepoint(pos):
        firkant.x += 50

def flyttGjetninger():
    for gjett in alleGjett:
        print("her er posisjon: " + str(gjett.center))
        gjett.y += 100

def sjekkKodeOgGiTilbakemelding():
    gjett = gjetninger[len(gjetninger) - 1]
    kodekopi = hemmeligKode.copy()
    antallRiktigFargePaRiktigPlass = 0
    antallRiktigFargePaFeilPlass = 0
    print ("skal sjekke " + str(gjett) + ", opp mot " + str(hemmeligKode))
    for n in range(len(gjett)):
        if gjett[n] == kodekopi[n]:
            print("riktig farge på riktig plass for " + str(n))
            gjett[n] = riktigFargePaRiktigPlass
            kodekopi[n] = riktigFargePaRiktigPlass

    for n in range(len(gjett)):
        if gjett[n] != riktigFargePaRiktigPlass:
            for m in range(len(kodekopi)):
                if gjett[n] == kodekopi[m]:
                    gjett[n] = riktigFargePaFeilPlass
                    kodekopi[m]  = riktigFargePaFeilPlass

    for n in range(len(kodekopi)):
        if kodekopi[n] == riktigFargePaRiktigPlass:
            antallRiktigFargePaRiktigPlass += 1
        if kodekopi[n] == riktigFargePaFeilPlass:
            antallRiktigFargePaFeilPlass += 1

    print("ferdig med sjekk, gjett er nå: " + str(gjett) + ", kodekopi ser slik ut: " + str(kodekopi))
    print("antallHeltRiktige " + str(antallRiktigFargePaRiktigPlass))
    print("antallLittRiktige " + str(antallRiktigFargePaFeilPlass))
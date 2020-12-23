from random import randint

WIDTH = 800
HEIGHT = 770

farge = 'farge'
rect = 'rect'
navn = 'navn'

rød = { navn: "rød", farge: (255, 0, 0) }
gul = { navn: "gul", farge: (255, 255, 0) }
grønn = { navn: "grønn", farge: (0, 255, 0) }
hvit = { navn: "hvit", farge: (255, 255, 255) }
blå = { navn: "blå", farge: (0, 0, 255) }
grå = { navn: "grå", farge: (100, 100, 100) }
oransje = { navn: "oransje", farge: (255, 165, 0) }
rosa = { navn: "rosa", farge: (255, 110, 199) }

alleFarger = [rød, gul, grønn, hvit, blå, grå, oransje, rosa]

gjett1 = { navn: "gjett1", rect: Rect((50, 700), (50, 50)), farge: hvit }
gjett2 = { navn: "gjett2", rect: Rect((110, 700), (50, 50)), farge: hvit }
gjett3 = { navn: "gjett3", rect: Rect((170, 700), (50, 50)), farge: hvit }
gjett4 = { navn: "gjett3", rect: Rect((230, 700), (50, 50)), farge: hvit }
alleGjett = [gjett1, gjett2, gjett3, gjett4]

riktigFargePaRiktigPlass = 'riktig farge på riktig plass'
riktigFargePaFeilPlass = 'riktig farge på feil plass'

ferdigKnapp = Rect((500, 400), (100, 50))

StartPåNyttKnapp = Rect((500, 100), (200,100))

def tilfeldigFarge():
    return alleFarger[randint(0, 7)]


hemmeligKode = [tilfeldigFarge(), tilfeldigFarge(),
    tilfeldigFarge(), tilfeldigFarge()]

gjetninger = []
gameover = False



def draw():
    global gameover
    screen.draw.filled_rect(gjett1[rect], gjett1[farge][farge])
    screen.draw.filled_rect(gjett2[rect], gjett2[farge][farge])
    screen.draw.filled_rect(gjett3[rect], gjett3[farge][farge])
    screen.draw.filled_rect(gjett4[rect], gjett4[farge][farge])
    screen.draw.textbox("Ferdig",ferdigKnapp,color="orange")


def nesteFarge(farge):
    return alleFarger[(alleFarger.index(farge) + 1) % len(alleFarger)]

def on_mouse_down(pos):
    global gameover
    for gjett in alleGjett:
        if gjett[rect].collidepoint(pos):
            gjett[farge] = nesteFarge(gjett[farge])

    if ferdigKnapp.collidepoint(pos):
        #print(f"ferdig med gjetning: {len(gjetninger)}")
        gjetninger.append([gjett1[farge],gjett2[farge],gjett3[farge],gjett4[farge]])
        #print(gjetninger[len(gjetninger) - 1])
        sjekkKodeOgGiTilbakemelding()
        if gameover:
            visBareStartIgjenKnapp()
        else:
            flyttGjetninger()

    if StartPåNyttKnapp.collidepoint(pos):
        initState()

def visBareStartIgjenKnapp():
    for gjett in alleGjett:
        gjett[rect].x += 1000
    screen.draw.filled_rect(ferdigKnapp, (0,0,0))
    ferdigKnapp.x += 1000


def flyttGjetninger():
    for gjett in alleGjett:
        gjett[rect].y -= 70


def sjekkKodeOgGiTilbakemelding():
    global gameover
    gjett = gjetninger[len(gjetninger) - 1]
    kodekopi = hemmeligKode.copy()
    antallRiktigFargePaRiktigPlass = 0
    antallRiktigFargePaFeilPlass = 0
    # print ("skal sjekke " + str(gjett) + ", opp mot " + str(hemmeligKode))
    for n in range(len(gjett)):
        if gjett[n] == kodekopi[n]:
            #print("riktig farge på riktig plass for " + str(n))
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

    screen.draw.text(f"{antallRiktigFargePaRiktigPlass} RR, {antallRiktigFargePaFeilPlass} RF", (gjett4[rect].x + 100, gjett4[rect].y), color="orange")
    if antallRiktigFargePaRiktigPlass == 4:
        screen.draw.textbox("Du klarte det! Start på nytt her", StartPåNyttKnapp, color="orange")
        gameover = True
    if len(gjetninger) == 10:
        screen.draw.textbox("Du klarte det desverre ikke. Prøv på nytt her", StartPåNyttKnapp, color="orange")
        gameover = True

def initState():
    global gameover
    screen.clear()
    hemmeligKode = tilfeldigFarge(), tilfeldigFarge(), tilfeldigFarge(), tilfeldigFarge()
    gjetninger.clear()
    gameover = False
    gjett1[rect].x = 50
    gjett2[rect].x = 110
    gjett3[rect].x = 170
    gjett4[rect].x = 230
    for gjett in alleGjett:
        gjett[rect].y = 700
        gjett[farge] = hvit
    ferdigKnapp.x = 500
    ferdigKnapp.y = 400
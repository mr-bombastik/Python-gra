import pygame
import random
import math
pygame.init()

# stałe
SZEROKOSC_OKNA = 800
WYSOKOSC_OKNA = 800
ROZMIAR_KWADRATU = 50
CZARNY = (0, 0, 0)

# tworzenie okna
okno = pygame.display.set_mode((SZEROKOSC_OKNA, WYSOKOSC_OKNA))
pygame.display.set_caption("Poruszanie kwadratem")

# początkowe położenie kwadratu
x = SZEROKOSC_OKNA // 2 - ROZMIAR_KWADRATU // 2
y = WYSOKOSC_OKNA // 2 - ROZMIAR_KWADRATU // 2
x_pozycja = random.randint(0, SZEROKOSC_OKNA - ROZMIAR_KWADRATU)
y_pozycja = random.randint(0, WYSOKOSC_OKNA - ROZMIAR_KWADRATU)
# początkowy kolor kwadratu
kolor = CZARNY
wynik = 0


def wyswietl_dystans(dystans):

    # ustalenie czcionki i jej rozmiaru
    czcionka = pygame.font.Font(None, 36)

    # stworzenie powierzchni z tekstem
    tekst = czcionka.render(str(dystans), True, (0, 0, 0))

    # wypisanie tekstu na ekranie w lewym górnym rogu
    okno.blit(tekst, (10, 10))

    # aktualizacja okna
    #pygame.display.flip()

def wyswietl_wynik(wynik):

    # ustalenie czcionki i jej rozmiaru
    czcionka = pygame.font.Font(None, 36)

    # stworzenie powierzchni z tekstem
    tekst = czcionka.render(str(wynik), True, (0, 0, 0))

    # wypisanie tekstu na ekranie w lewym górnym rogu
    okno.blit(tekst, (100, 10))

    # aktualizacja okna
    #pygame.display.flip()

# pętla programu
while True:
    # obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    predkosc = 1
    # poruszanie kwadratem za pomocą strzałek
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= predkosc
    if keys[pygame.K_RIGHT]:
        x += predkosc
    if keys[pygame.K_UP]:
        y -= predkosc
    if keys[pygame.K_DOWN]:
        y += predkosc

    # zmiana koloru kwadratu i odwracanie kierunku poza ekranem
    if keys[pygame.K_SPACE]:
        kolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if x < 0:
        x = SZEROKOSC_OKNA - ROZMIAR_KWADRATU
    elif x > SZEROKOSC_OKNA - ROZMIAR_KWADRATU:
        x = 0
    if y < 0:
        y = WYSOKOSC_OKNA - ROZMIAR_KWADRATU
    elif y > WYSOKOSC_OKNA - ROZMIAR_KWADRATU:
        y = 0
    #funkcja obliczająca dystans
    dystans = math.sqrt((x_pozycja - x) ** 2 + (y_pozycja - y) ** 2)
    dystans = round(dystans)

    # losowanie pozycji punktu
    if dystans < 50 and keys[pygame.K_SPACE]:
        x_pozycja = random.randint(0, SZEROKOSC_OKNA - ROZMIAR_KWADRATU)
        y_pozycja = random.randint(0, SZEROKOSC_OKNA - ROZMIAR_KWADRATU)
        wynik = wynik + 1


    # rysowanie kwadratu
    okno.fill((255, 255, 255))
    pygame.draw.rect(okno, CZARNY, (x_pozycja, y_pozycja, ROZMIAR_KWADRATU, ROZMIAR_KWADRATU))
    pygame.draw.rect(okno, kolor, (x, y, ROZMIAR_KWADRATU, ROZMIAR_KWADRATU))
    wyswietl_wynik(wynik)
    wyswietl_dystans(dystans)



    # aktualizacja okna
    pygame.display.update()




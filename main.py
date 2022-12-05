import pygame
import time
from random import randint
from Label import Label

if __name__ == '__main__':
    pygame.init()
    '''Віконце'''
    back = (200, 255, 255)  # колір фона (background)
    mw = pygame.display.set_mode((600, 600))  # віконце проги (main window)
    mw.fill(back)

    clock = pygame.time.Clock()
    RED = (255, 0, 0)
    GREEN = (0, 255, 51)
    YELLOW = (255, 255, 0)
    DARK_BLUE = (0, 0, 100)
    BLUE = (80, 80, 255)
    LIGHT_GREEN = (200, 255, 200)
    LIGHT_RED = (250, 128, 114)
    cards = []
    num_cards = 4
    x = 70

    start_time = time.time()
    cur_time = start_time

    ''' Інтерфейс  гри'''

    time_text = Label(0, 0, 50, 50, back, mw)
    time_text.set_text('Час:', 40, DARK_BLUE)
    time_text.draw(20, 20)

    timer = Label(50, 75, 50, 40, back, mw)
    timer.set_text('0', 40, DARK_BLUE)
    timer.draw(0, 0)

    score_text = Label(300, 0, 50, 50, back, mw)
    score_text.set_text('Рахунок:', 45, DARK_BLUE)
    score_text.draw(20, 20)

    score = Label(430, 75, 50, 40, back, mw)
    score.set_text('0', 40, DARK_BLUE)
    score.draw(0, 0)

    for i in range(num_cards):
        new_card = Label(x, 170, 70, 100, YELLOW, mw)
        new_card.outline(BLUE, 10)
        new_card.set_text('CLICK', 20)
        cards.append(new_card)
        x = x + 100
    wait = 0
    points = 0


    while True:
        '''Картки та кліки'''
        if wait == 0:
            wait = 30  # кількість тіків коли є текст
            click = randint(1, num_cards)
            for i in range(num_cards):
                cards[i].color(YELLOW)
                if (i + 1) == click:
                    cards[i].draw(10, 40)
                else:
                    cards[i].fill()
        else:
            wait -= 1
        '''Обробка кліків та карток'''
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                for i in range(num_cards):
                    # я потапив у ціль
                    if cards[i].collidepoint(x, y):
                        if i + 1 == click:  #зелений коли у яблочко
                            cards[i].color(GREEN)
                            points += 1
                        else:  # без яблочка фарбуєму у червоний, та  -1 у карму і до рахунку
                            cards[i].color(RED)
                            points -= 1
                        cards[i].fill()
                        score.set_text(str(points), 40, DARK_BLUE)
                        score.draw(0, 0)
        '''Queen - We Are The Champions або ні'''
        new_time = time.time()

        if new_time - start_time >= 11:
            win = Label(0, 0, 500, 500, LIGHT_RED, mw)
            win.set_text("Час вичерпано!!!", 60, DARK_BLUE)
            win.draw(110, 180)
            break

        if int(new_time) - int(cur_time) == 1:  # є різниця в 1 секунду між старим та новим часом
            timer.set_text(str(int(new_time - start_time)), 40, DARK_BLUE)
            timer.draw(0, 0)
            cur_time = new_time

        if points >= 5:
            win = Label(0, 0, 500, 500, LIGHT_GREEN, mw)
            win.set_text("Ти  Champions !!!", 60, DARK_BLUE)
            win.draw(140, 180)
            resul_time = Label(90, 230, 250, 250, LIGHT_GREEN, mw)
            resul_time.set_text("Час проходження: " + str(int(new_time - start_time)) + " сек", 40, DARK_BLUE)

            resul_time.draw(0, 0)

            break

        pygame.display.update()
        clock.tick(40)

    pygame.display.update()

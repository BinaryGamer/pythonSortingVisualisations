import pygame
import random
import time

pygame.init()
disp = pygame.display
HEIGHT=640
WIDTH=640
win = disp.set_mode((WIDTH,HEIGHT))
DELAY = 150
LENGTH = 32
running = True
CWIDTH = 5
GAP = 3
def flip(m, i):
    strt = 0
    while strt < i:
        temp = m[strt]
        m[strt] = m[i]
        m[i] = temp
        strt+=1
        i-=1
    return m

def findMax(m, n):
    maxIndex = 0
    for i in range(n):
        if m[i] > m[maxIndex]:
            maxIndex = i
    return maxIndex

def pancake_sort(m, n):
    size_current = n
    while size_current > 1:
        maxIndex = findMax(m, size_current)
        if maxIndex != size_current-1:
            redraw(m, spec=[i for i in range(maxIndex+1)])
            m = flip(m, maxIndex)
            redraw(m, spec=[i for i in range(maxIndex+1)])
            m = flip(m, size_current-1)
            redraw(m, spec=[size_current-1])
        size_current -= 1
    return m



def redraw(x, spec=None, c=(255,0,0)):
    win.fill((255,255,255))
    for i in range(len(x)):
        across = i*CWIDTH+i*GAP
        if spec != None:
            if i in spec:
                pygame.draw.rect(win, (0,0,255), (across, HEIGHT-x[i], CWIDTH, x[i]))
            else:
                pygame.draw.rect(win, c, (across, HEIGHT-x[i], CWIDTH, x[i]))
        else:
            pygame.draw.rect(win, c, (across, HEIGHT-x[i], CWIDTH, x[i]))
    disp.update()
    pygame.time.delay(DELAY)
x = [i for i in range(10, 410, 5)]
random.shuffle(x)
print(len(x))
sortedCheck = False
while running:
    #win.fill((255,255,255))
    if not sortedCheck:
        x = pancake_sort(x, len(x))
        win.fill((255,255,255))
        redraw(x, c=(0,255,0))
        disp.update()

    #disp.update()
    #pygame.time.delay(DELAY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

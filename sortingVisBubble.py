import pygame
import random
import time

pygame.init()
disp = pygame.display
HEIGHT=640
WIDTH=640
win = disp.set_mode((WIDTH,HEIGHT))
DELAY = 30
LENGTH = 32
running = True
CWIDTH = 5
GAP = 3
def merge_sort(m):
    if len(m) <= 1:
        return m
    left = []
    right = []
    for i in range(len(m)):
        if i < len(m)/2:
            left.append(m[i])
        else:
            right.append(m[i])
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
def merge(left, right):
    result = []
    while len(left)!=0 and len(right)!=0:
        if left[0] <= right[0]:
            result.append(left[0])
            left.remove(left[0])
        else:
            result.append(right[0])
            right.remove(right[0])
    while len(left) != 0:
        result.append(left[0])
        left.remove(left[0])
    while len(right) != 0:
        result.append(right[0])
        right.remove(right[0])
    return result

def swap(m, pos1, pos2):
    val1, val2 = m[pos1], m[pos2]
    m[pos2], m[pos1] = val1, val2
    return m

def bubble_sort(m):
    Operation = True
    while Operation:
        Operation = False
        for i in range(len(m)):
            if i != len(m)-1:
                if m[i] > m[i+1]:
                    m=swap(m, i, i+1)
                    Operation = True
                    win.fill((255,255,255))
                    redraw(m, spec=i+1)
                    disp.update()
                    pygame.time.delay(DELAY)
    redraw(m, c=(0,255,0))
    disp.update()

    return m



def redraw(x, spec=None, c=(255,0,0)):
    for i in range(len(x)):
        across = i*CWIDTH+i*GAP
        if spec:
            if i == spec:
                pygame.draw.rect(win, (0,0,255), (across, HEIGHT-x[i], CWIDTH, x[i]))
            else:
                pygame.draw.rect(win, c, (across, HEIGHT-x[i], CWIDTH, x[i]))
        else:
            pygame.draw.rect(win, c, (across, HEIGHT-x[i], CWIDTH, x[i]))

x = [i for i in range(10, 410, 5)]
random.shuffle(x)
print(len(x))
while running:
    #win.fill((255,255,255))
    bubble_sort(x)
    #disp.update()
    #pygame.time.delay(DELAY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

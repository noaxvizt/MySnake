START_FPS = 8
WIDHT = 600
HEIGHT = 420
CELLS_SIZE = 30

BARRIERS1 = []
for i in range(WIDHT // CELLS_SIZE):
    BARRIERS1.append((i, 0))
    BARRIERS1.append((i, HEIGHT // CELLS_SIZE - 1))
for i in range(1, HEIGHT // CELLS_SIZE - 1):
     BARRIERS1.append((0, i))
     BARRIERS1.append((WIDHT // CELLS_SIZE - 1, i))



BARRIERS2 = []
for i in range(4, WIDHT // CELLS_SIZE - 4):
    BARRIERS2.append((i, 0))
    BARRIERS2.append((i, HEIGHT // CELLS_SIZE - 4))
for i in range(5, HEIGHT // CELLS_SIZE - 5):
    BARRIERS2.append((0, i))
    BARRIERS2.append((WIDHT // CELLS_SIZE - 4, i))



BARRIERS3 = []


BARRIERS4 = []
for i in range(4, 6):
    for j in range(1, 3):
        BARRIERS4.append((i, j))
for i in range(8, 10):
    for j in range(1, 3):
        BARRIERS4.append((i, j))
for i in range(12, 14):
    for j in range(1, 3):
        BARRIERS4.append((i, j))
for i in range(16, 18):
    for j in range(1, 3):
        BARRIERS4.append((i, j))
for i in range(4, 6):
    for j in range(5, 7):
        BARRIERS4.append((i, j))
for i in range(8, 10):
    for j in range(5, 7):
        BARRIERS4.append((i, j))
for i in range(12, 14):
    for j in range(5, 7):
        BARRIERS4.append((i, j))
for i in range(16, 18):
    for j in range(5, 7):
        BARRIERS4.append((i, j))
for i in range(4, 6):
    for j in range(9, 11):
        BARRIERS4.append((i, j))
for i in range(8, 10):
    for j in range(9, 11):
        BARRIERS4.append((i, j))
for i in range(12, 14):
    for j in range(9, 11):
        BARRIERS4.append((i, j))
for i in range(16, 18):
    for j in range(9, 11):
        BARRIERS4.append((i, j))
BARRIERS = [BARRIERS1, BARRIERS2, BARRIERS3, BARRIERS4]
from .sector import *


class Apple(Sector):
    def __init__(self, color):
        super().__init__(color, 120, 120, CELLS_SIZE, CELLS_SIZE)

    def Replace(self, lis):
        may_be_lis = []
        for i in range(WIDHT // CELLS_SIZE):
            for j in range(HEIGHT // CELLS_SIZE):
                if not lis[i][j]:
                    may_be_lis.append((i, j))
        cell = random.randint(0, len(may_be_lis) - 1)
        self.rect.x = may_be_lis[cell][0] * CELLS_SIZE
        self.rect.y = may_be_lis[cell][1] * CELLS_SIZE
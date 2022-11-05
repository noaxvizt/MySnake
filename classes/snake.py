from .sector import *


class Snake(Sector):
    def __init__(self, color, apple):
        super().__init__(color, 0, 0, CELLS_SIZE, CELLS_SIZE, "data/images/snakeshead.png")
        self.head = self.sector
        self.score = 0
        self.tail_queue = deque()
        self.apple = apple
        self.ungle = 0

    def SetXVelocity(self, x_velocity):
        super().SetXVelocity(x_velocity)
        if self.x_velocity > 0:
            self.ungle = 0
        else:
            self.ungle = 180
        self.Rotate()

    def SetYVelocity(self, y_velocity):
        super().SetYVelocity(y_velocity)
        if self.y_velocity > 0:
            self.ungle = 270
        else:
            self.ungle = 90
        self.Rotate()

    def Rotate(self):
        self.sector = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(self.image_path),
                                                                     (self.x_size, self.y_size)), self.ungle)
        self.rect = self.sector.get_rect(topleft=(self.rect.x, self.rect.y))

    def CheckCollutions(self):
        if len(self.tail_queue) != 0:
            for i in self.tail_queue:
                if i.rect.x == self.rect.x and i.rect.y == self.rect.y:
                    return True
        return False

    def Move(self):
        if self.apple.rect.x == self.rect.x and self.apple.rect.y == self.rect.y:
            self.score += 1
            self.AddSector()
            lis = [[0 for __ in range(HEIGHT // CELLS_SIZE)] for _ in range(WIDHT // CELLS_SIZE)]
            for i in self.tail_queue:
                lis[i.rect.x // CELLS_SIZE][i.rect.y // CELLS_SIZE] = 1
            lis[self.rect.x // CELLS_SIZE][self.rect.y // CELLS_SIZE] = 1
            self.apple.Replace(lis)
        if self.CheckCollutions():
            print("SHIT")
        if len(self.tail_queue) == 0:
            pass
        elif len(self.tail_queue) == 1:
            if self.tail_queue[-1].freeze:
                self.tail_queue[-1].freeze = False
            else:
                self.tail_queue[-1] = self.DeepCopy()
        else:
            if self.tail_queue[-1].freeze:
                self.tail_queue[-1].freeze = False
                new_tail = self.tail_queue.pop()
                self.tail_queue[-1] = self.DeepCopy()
                last_changed = self.tail_queue.pop()
                self.tail_queue.insert(len(self.tail_queue) - 1, new_tail)
                self.tail_queue.insert(0, last_changed)
            else:
                self.tail_queue[-1] = self.DeepCopy()
                last_changed = self.tail_queue.pop()
                self.tail_queue.insert(0, last_changed)
        super().Move()

    def AddSector(self):
        if len(self.tail_queue) == 0:
            now_sector = self.DeepCopy()
        else:
            now_sector = self.tail_queue[-1].DeepCopy()
        now_sector.freeze = False
        self.tail_queue.append(now_sector)

    def Draw(self, screen):
        for i in self.tail_queue:
            i.Draw(screen)
        super().Draw(screen)

from classes.sector import *
from data.constants import *


class Barrier(Sector):
    def __init__(self, color, x_position, y_position, image_path="data/images/barrier.png"):
        super().__init__(color, x_position, y_position, CELLS_SIZE, CELLS_SIZE, image_path)


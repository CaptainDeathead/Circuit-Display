import rpi.gpio as pins
import time

pins.setmode(pins.BCM)

"""pin-2: top right
pin-3: bottom right
pin-4: middle right
pin-5: 2nd bottom right
pin-6: 3rd top right
pin-9: bottom left
pin-10: 2nd bottom left
pin-11: 2nd middle right
pin-13: 2nd top left
pin-14: 3rd bottom right
pin-16: 2nd middle left
pin-17: 3rd middle left
pin-19: 2nd top right
pin-20: top left
pin-21: 3rd top left
pin-22: 3rd middle right
pin-26: middle left
pin-27: 3rd bottom left"""

class display:
    def __init__(self):
        self.pins.setup(2, pins.OUT)
        self.pins.setup(3, pins.OUT)
        self.pins.setup(4, pins.OUT)
        self.pins.setup(5, pins.OUT)
        self.pins.setup(6, pins.OUT)
        self.pins.setup(9, pins.OUT)
        self.pins.setup(10, pins.OUT)
        self.pins.setup(11, pins.OUT)
        self.pins.setup(13, pins.OUT)
        self.pins.setup(14, pins.OUT)
        self.pins.setup(16, pins.OUT)
        self.pins.setup(17, pins.OUT)
        self.pins.setup(19, pins.OUT)
        self.pins.setup(20, pins.OUT)
        self.pins.setup(21, pins.OUT)
        self.pins.setup(22, pins.OUT)
        self.pins.setup(26, pins.OUT)
        self.pins.setup(27, pins.OUT)

        self.pins.output(2, pins.LOW)
        self.pins.output(3, pins.LOW)
        self.pins.output(4, pins.LOW)
        self.pins.output(5, pins.LOW)
        self.pins.output(6, pins.LOW)
        self.pins.output(9, pins.LOW)
        self.pins.output(10, pins.LOW)
        self.pins.output(11, pins.LOW)
        self.pins.output(13, pins.LOW)
        self.pins.output(14, pins.LOW)
        self.pins.output(16, pins.LOW)
        self.pins.output(17, pins.LOW)
        self.pins.output(19, pins.LOW)
        self.pins.output(20, pins.LOW)
        self.pins.output(21, pins.LOW)
        self.pins.output(22, pins.LOW)
        self.pins.output(26, pins.LOW)
        self.pins.output(27, pins.LOW)

        self.table = {
            0: [2, 3, 4, 5, 6, 14, 19, 22],
            1: [2, 3, 4],
            2: [2, 3, 5, 6, 11, 14, 19],
            3: [2, 3, 4, 5, 6, 11, 14, 19],
            4: [4, 5, 11, 19, 22],
            5: [2, 3, 5, 6, 19, 22],
            6: [2, 3, 4, 5, 6, 19, 22],
            7: [2, 4, 5, 6, 19],
            8: [2, 3, 6, 11, 14],
            9: [2, 3, 4, 11, 19]
        }

    def display(self, number):
        if number == "clear":
            self.pins.output(2, pins.LOW)
            self.pins.output(3, pins.LOW)
            self.pins.output(4, pins.LOW)
            self.pins.output(5, pins.LOW)
            self.pins.output(6, pins.LOW)
            self.pins.output(9, pins.LOW)
            self.pins.output(10, pins.LOW)
            self.pins.output(11, pins.LOW)
            self.pins.output(13, pins.LOW)
            self.pins.output(14, pins.LOW)
            self.pins.output(16, pins.LOW)
            self.pins.output(17, pins.LOW)
            self.pins.output(19, pins.LOW)
            self.pins.output(20, pins.LOW)
            self.pins.output(21, pins.LOW)
            self.pins.output(22, pins.LOW)
            self.pins.output(26, pins.LOW)
            self.pins.output(27, pins.LOW)
        elif number == 0:
            self.table[0].forEach(self.pins.output(self.table[0], pins.HIGH))
        elif number == 1:
            self.table[1].forEach(self.pins.output(self.table[1], pins.HIGH))
        elif number == 2:
            self.table[2].forEach(self.pins.output(self.table[2], pins.HIGH))
        elif number == 3:
            self.table[3].forEach(self.pins.output(self.table[3], pins.HIGH))
        elif number == 4:
            self.table[4].forEach(self.pins.output(self.table[4], pins.HIGH))
        elif number == 5:
            self.table[5].forEach(self.pins.output(self.table[5], pins.HIGH))
        elif number == 6:
            self.table[6].forEach(self.pins.output(self.table[6], pins.HIGH))
        elif number == 7:
            self.table[7].forEach(self.pins.output(self.table[7], pins.HIGH))
        elif number == 8:
            self.table[8].forEach(self.pins.output(self.table[8], pins.HIGH))
        elif number == 9:
            self.table[9].forEach(self.pins.output(self.table[9], pins.HIGH))
        else:
            print("Invalid number")

    def cycle(self):
        for i in range(0, 10):
            self.display(i)
            time.sleep(1)
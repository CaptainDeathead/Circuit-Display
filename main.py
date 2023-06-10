import RPi.GPIO as pins
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
        pins.setup(2, pins.OUT)
        pins.setup(3, pins.OUT)
        pins.setup(4, pins.OUT)
        pins.setup(5, pins.OUT)
        pins.setup(6, pins.OUT)
        pins.setup(9, pins.OUT)
        pins.setup(10, pins.OUT)
        pins.setup(11, pins.OUT)
        pins.setup(13, pins.OUT)
        pins.setup(14, pins.OUT)
        pins.setup(16, pins.OUT)
        pins.setup(17, pins.OUT)
        pins.setup(19, pins.OUT)
        pins.setup(20, pins.OUT)
        pins.setup(21, pins.OUT)
        pins.setup(22, pins.OUT)
        pins.setup(26, pins.OUT)
        pins.setup(27, pins.OUT)

        pins.output(2, pins.LOW)
        pins.output(3, pins.LOW)
        pins.output(4, pins.LOW)
        pins.output(5, pins.LOW)
        pins.output(6, pins.LOW)
        pins.output(9, pins.LOW)
        pins.output(10, pins.LOW)
        pins.output(11, pins.LOW)
        pins.output(13, pins.LOW)
        pins.output(14, pins.LOW)
        pins.output(16, pins.LOW)
        pins.output(17, pins.LOW)
        pins.output(19, pins.LOW)
        pins.output(20, pins.LOW)
        pins.output(21, pins.LOW)
        pins.output(22, pins.LOW)
        pins.output(26, pins.LOW)
        pins.output(27, pins.LOW)

        self.table = {
            0: [2, 3, 4, 5, 6, 14, 19, 22],
            1: [2, 3, 4],
            2: [2, 3, 5, 6, 11, 14, 19],
            3: [2, 3, 4, 5, 6, 11, 14, 19],
            4: [4, 5, 11, 19, 22],
            5: [2, 3, 5, 6, 19, 22],
            6: [2, 3, 4, 5, 6, 14, 19, 22],
            7: [2, 4, 5, 6, 19],
            8: [2, 3, 6, 11, 14],
            9: [2, 3, 4, 11, 19]
        }

    def display(self, number):
        if number == "clear":
            pins.output(2, pins.LOW)
            pins.output(3, pins.LOW)
            pins.output(4, pins.LOW)
            pins.output(5, pins.LOW)
            pins.output(6, pins.LOW)
            pins.output(9, pins.LOW)
            pins.output(10, pins.LOW)
            pins.output(11, pins.LOW)
            pins.output(13, pins.LOW)
            pins.output(14, pins.LOW)
            pins.output(16, pins.LOW)
            pins.output(17, pins.LOW)
            pins.output(19, pins.LOW)
            pins.output(20, pins.LOW)
            pins.output(21, pins.LOW)
            pins.output(22, pins.LOW)
            pins.output(26, pins.LOW)
            pins.output(27, pins.LOW)
        elif number == 0:
            for pin in self.table[0]:
                pins.output(pin, pins.HIGH)
        elif number == 1:
            for pin in self.table[1]:
                pins.output(pin, pins.HIGH)
        elif number == 2:
            for pin in self.table[2]:
                pins.output(pin, pins.HIGH)
        elif number == 3:
            for pin in self.table[3]:
                pins.output(pin, pins.HIGH)
        elif number == 4:
            for pin in self.table[4]:
                pins.output(pin, pins.HIGH)
        elif number == 5:
            for pin in self.table[5]:
                pins.output(pin, pins.HIGH)
        elif number == 6:
            for pin in self.table[6]:
                pins.output(pin, pins.HIGH)
        elif number == 7:
            for pin in self.table[7]:
                pins.output(pin, pins.HIGH)
        elif number == 8:
            for pin in self.table[8]:
                pins.output(pin, pins.HIGH)
        elif number == 9:
            for pin in self.table[9]:
                pins.output(pin, pins.HIGH)
        else:
            print("Invalid number")

    def cycle(self):
        for i in range(0, 10):
            self.display(i)
            time.sleep(1)
            self.display("clear")

if __name__ == "__main__":
    display = display()
    display.cycle()
    pins.cleanup()
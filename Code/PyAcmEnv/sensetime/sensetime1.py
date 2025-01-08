import random

class MyCoin():
    def __init__(self, p: float):
        self.p = p

    def flip(self):
        x = random.random()
        if x < self.p:
            return True
        else:
            return False

    def equal_flip(self):
        while 1:
            x1 = self.flip()
            x2 = self.flip()
            if x1 and not x2:
                return True
            elif not x1 and x2:
                return False
            

def func():
    pass

if __name__ == '__main__':
    func()
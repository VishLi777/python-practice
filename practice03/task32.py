
class C32:
    def __init__(self):
        self.condition = 'A'
    def step(self):
        if self.condition == 'A':
            self.condition = 'B'
            return 0
        elif self.condition == 'C':
            self.condition = 'D'
            return 3
        elif self.condition == 'D':
            self.condition = 'F'
            return 6
        elif self.condition == 'E':
            self.condition = 'F'
            return 7
        elif self.condition == 'F':
            self.condition = 'G'
            return 8
        else:
            RuntimeError
    def exit(self):
        if self.condition == 'A':
            self.condition = 'E'
            return 1
        elif self.condition == 'B':
            self.condition = 'C'
            return 2
        elif self.condition == 'C':
            self.condition = 'G'
            return 4
        elif self.condition == 'D':
            self.condition = 'E'
            return 5
        elif self.condition == 'F':
            self.condition = 'B'
            return 9
        else:
            RuntimeError
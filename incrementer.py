class Incrementer(object):
    def __init__(self, value=1):
        self.value = value

    def up_one(self):
        self.value += 1
        return self.value

class Lamp(object):

    def __init__(self, on=False, off=True):
        self.on = on
        self.off = off


    def turn_on(self):
        if self.on == False:
            self.on = True
            self.off = False


    def turn_off(self):
        if self.off == False:
            self.off = True
            self.on = False


    def toggle(self):
        if self.on == True:
            self.on = False
            self.off = True
        elif self.on != True:
            self.on = True
            self.off = False

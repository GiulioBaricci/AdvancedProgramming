class Gollum:
    def __init__(self):
        self.hasTheOneRing = True
    def chant(self): print("My precious!!!")
    def swallow(self): print("gollllummmm!")
    def lose_the_ring(self): self.hasTheOneRing = False
    def __str__(self):
        return "type :- "+type(self).__name__+",\t\t\tRing "+('✓' if self.hasTheOneRing else 'x')
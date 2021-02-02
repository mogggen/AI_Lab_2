import turtle

class Approch:
    def __init__(self, name, color):
        self.name = name
        self.tur = turtle.Turtle()
        self.tur.speed(0)
        self.tur.pencolor(color)
        self.tur.fillcolor(color)

    #check needs
    def need(self):
        for s in self.states:
            if s[1] < self.worst[1]:
                self.worst = s
    
    def walk(self, dest):
        self.tur.st()
        self.tur.lt(self.tur.towards(dest[0], dest[1]) - self.tur.heading())
        dist = ((self.tur.xcor() - dest[0])**2 +
                (self.tur.ycor() - dest[1])**2)**0.5
        #print(dist)
        if dist > self.walkspeed:
            self.tur.fd(self.walkspeed) #arrive only if destination is within reach
        else:
            self.tur.ht()
            self.worst[1] += 12 

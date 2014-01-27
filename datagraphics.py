# python datagraphics.py datastats.json data2.json [keyword to search for]

import sys
from nodebox.graphics import *
from nodebox.graphics.physics import System, Flock, Particle, MASS

def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]

class Obstacle(Particle):
    def draw(self):
        ellipse(self.x, self.y, self.radius*2, self.radius*2, fill=(0,0,0,0.99)) # buggy

def keywordCount():
    global stringTest
    while True:
        strLine = stData.readline()
        if strLine:
            strLine = strLine.split( )
            if keyword in strLine[0]:
                stringTest += 1
        else: break

def draw(canvas):
    global stringTest
    background(1)
    fill(0.96,0.5,0.15,0.99)
    flock.update(cohesion=0.1)
    localTest = stringTest
    for boid in flock:
        push()
        translate(boid.x, boid.y)
        scale(0.5 + 1.5 * boid.depth)
        rotate(boid.heading)
        if localTest > 0:
            rect(15, 15, 15, 15, fill=(0,0,0,0.99))
            localTest-=1
            pop()
            continue
        arrow(0, 0, 15)
        pop()
    obstacle.x = canvas.mouse.x
    obstacle.y = canvas.mouse.y

stStats = sys.argv[1] # first file
stData = open(sys.argv[2], 'r+') # second file
keyword = sys.argv[3]
wordCount = 0;
statWords = read_words(stStats)
wordCount = statWords[0]
canvas.fps = 30
flock = Flock(int(float(wordCount)), 150, 100, 500, 500)
flock.sight = 300
obstacle = Obstacle(0, 0, mass=70, radius=70, fixed=True)
flock.obstacles.append(obstacle)
stringTest = 0
keywordCount()
canvas.run(draw)
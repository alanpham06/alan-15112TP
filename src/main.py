from cmu_graphics import *
# Create a line class that will help with connecting all of the points
class Line:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.color = 'black'
        self.lineWidth = 5
    
    def __repr__(self):
        return f'Line from ({self.x0}, {self.y0}) to ({self.x1}, {self.y1})'

def onAppStart(app):
    # App speed
    # app.stepsPerSecond = 10

    # Cursor properties
    app.cursX = 200
    app.cursY = 200
    app.cursNewX = None
    app.cursNewY = None
    app.r = 5

    # List of all the lines drawn
    app.allLines = []
    pass

def redrawAll(app):
    # Draw cursor
    drawCircle(app.cursX, app.cursY, app.r, fill='aqua')
    
    # Draw all of the lines
    for line in app.allLines:
        x0, y0, x1, y1 = line.x0, line.y0, line.x1, line.y1
        drawLine(x0, y0, x1, y1, fill=line.color, lineWidth=line.lineWidth)
    pass

def onMousePress(app, mouseX, mouseY):
    pass

def onMouseDrag(app, mouseX, mouseY):
    app.x1, app.y1 = mouseX, mouseY
    if (abs(app.cursX - app.x1) > 5) and (abs(app.cursY - app.y1) > 5):
        tempLine = Line(app.cursX, app.cursY, app.x1, app.y1)
        app.allLines.append(tempLine)
        app.cursX, app.cursY = mouseX, mouseY
        app.x1, app.y1 = None, None
    pass

def onMouseMove(app, mouseX, mouseY):
    pass
    
def onMouseRelease(app, mouseX, mouseY):
    pass

def main():
    runApp(width=800, height=500)

main()

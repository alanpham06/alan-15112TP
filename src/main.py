from cmu_graphics import *
from urllib.request import urlopen
from PIL import Image, ImageDraw

# Create a line class that will help with connecting all of the points
class Line:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.color = 'black'
        self.lineWidth = 3
    
    def __repr__(self):
        return f'Line from ({self.x0}, {self.y0}) to ({self.x1}, {self.y1})'
    
def makePilImage(imageWidth, imageHeight, bgColor):
    # Manually create a new PIL Image w/ given bg color:
    return Image.new('RGBA', (imageWidth, imageHeight), bgColor)

def makeCursorLines(pilImage):
    draw = ImageDraw.Draw(pilImage)
    imageWidth, imageHeight = pilImage.size
    # Add the cross to cursor
    draw.line((imageWidth//2, 0, imageWidth//2, imageHeight), width=3, fill='black')
    draw.line((0, imageHeight//2, imageWidth, imageHeight//2), width=3, fill='black')

def onAppStart(app):
    # Cursor properties
    app.cursorX, app.cursorY = app.width//2, app.height//2
    app.cursNewX, app.cursNewY = None, None
    app.cursorWidth = 15
    app.cursorHeight = 15
    # Initialize the cursor as PIL Image
    bgColor = (0, 0, 0, 0)
    drawCursor = makePilImage(app.cursorWidth, app.cursorHeight, bgColor)
    makeCursorLines(drawCursor)
    # Convert it into a CMU image
    app.cmuCursor = CMUImage(drawCursor)

    # List of all the lines drawn
    app.allLines = []
    app.allObjects = []

    # Tool bar properties
    app.toolBarX = rounded(app.width * 0.1)
    app.toolBarY = 10
    app.toolBarWidth = rounded(app.width * 0.8)
    app.toolBarHeight = rounded(app.height * 0.1)
    app.toolBarColor = 'slateGray'
    pass

def redrawAll(app):
    # Draw tool bar
    drawRect(app.toolBarX, app.toolBarY, app.toolBarWidth, app.toolBarHeight, fill=app.toolBarColor)

    # Draw cursor
    drawImage(app.cmuCursor, app.cursorX, app.cursorY, align='center')
    
    # Draw all of the lines
    for line in app.allLines:
        x0, y0, x1, y1 = line.x0, line.y0, line.x1, line.y1
        drawLine(x0, y0, x1, y1, fill=line.color, lineWidth=line.lineWidth)
    
    # Maintains all of the things already drawn on paper
    for item in app.allObjects:
        for line in item:
            x0, y0, x1, y1 = line.x0, line.y0, line.x1, line.y1
            drawLine(x0, y0, x1, y1, fill=line.color, lineWidth=line.lineWidth)
    pass

def onMousePress(app, mouseX, mouseY):
    pass

def onMouseDrag(app, mouseX, mouseY):
    # Drawing continuous lines logic
    app.x1, app.y1 = mouseX, mouseY
    if (abs(app.cursorX - app.x1) > 3) or (abs(app.cursorY - app.y1) > 3):
        tempLine = Line(app.cursorX, app.cursorY, app.x1, app.y1)
        app.allLines.append(tempLine)
        app.cursorX, app.cursorY = mouseX, mouseY
        app.x1, app.y1 = None, None
    pass

def onMouseMove(app, mouseX, mouseY):
    app.cursorX, app.cursorY = mouseX, mouseY
    pass
    
def onMouseRelease(app, mouseX, mouseY):
    app.allObjects.append(app.allLines)
    app.allLines = []
    app.curorsX, app.cursorY = mouseX, mouseY
    pass

def main():
    runApp(width=1000, height=800)

main()

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
    
# Create classes for each writing utensil
class Pen:
    def __init__(self, app):
        self.penMode = False
        penPILImage = Image.open(r"C:\Users\ankph\Code\alan-15112TP-main\src\writing-utensil-icons\pen-icon.png")
        penPILImgAdjusted = penPILImage.resize((app.iconWidth, app.iconHeight))
        self.cmuPenImgFinal = CMUImage(penPILImgAdjusted )

def loadPilImage(url):
    # Loads a PIL image from a url
    return Image.open(urlopen(url)) 

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
    # Line spacing logic
    app.absXDiff = 1
    app.absYDiff = 1

    # States of drawing modes
    app.penMode = False
    app.penIcon = 0

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
    app.toolBarY = rounded(app.height * 0.01)
    app.toolBarWidth = rounded(app.width * 0.8)
    app.toolBarHeight = rounded(app.height * 0.1)
    app.toolBarColor = 'lightGray'
    app.toolBarBGColor = 'silver'

    # Writing utensils icons in tool bar
    app.iconUpperLeftCorners = []
    numOfIcons = 9
    for i in range(numOfIcons):
        spacingBtwIcons = rounded(app.toolBarWidth/numOfIcons)
        cornerX = app.toolBarX + rounded(app.toolBarX * 0.1)
        cornerY = app.toolBarY + rounded(app.toolBarY * 0.8)
        app.iconUpperLeftCorners.append((cornerX + (i * spacingBtwIcons), cornerY))
    app.iconWidth = rounded(spacingBtwIcons * 0.8)
    app.iconHeight = rounded(app.toolBarHeight * 0.8)

    app.writingTools = [Pen(app)]
    pass

def getWritingUtensilSelection(app, mouseX, mouseY):
    for i in range(len(app.iconUpperLeftCorners)):
        left, top = app.iconUpperLeftCorners[i]
        right = left + app.iconWidth
        bottom = top + app.iconHeight
        if (mouseX > left) and (mouseX < right) and (mouseY < bottom) and (mouseY > top):
            return i
    return None

def redrawAll(app):
    # Draw tool bar
    drawRect(app.toolBarX, app.toolBarY-5, app.toolBarWidth+5, app.toolBarHeight+5, fill=app.toolBarBGColor)
    drawRect(app.toolBarX, app.toolBarY, app.toolBarWidth, app.toolBarHeight, fill=app.toolBarColor)
    # Draw writing utensil icons in tool bar
    for leftX, topY in app.iconUpperLeftCorners:
        drawImage(app.writingTools[0].cmuPenImgFinal, leftX, topY)
        if app.penMode:
            drawRect(leftX, topY, app.iconWidth, app.iconHeight, fill='yellow', opacity=20)

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
    if getWritingUtensilSelection(app, mouseX, mouseY) == app.penIcon:
        app.penMode = not app.penMode
    pass

def onMouseDrag(app, mouseX, mouseY):
    if app.penMode:
        # Drawing continuous lines logic
        app.x1, app.y1 = mouseX, mouseY
        if (abs(app.cursorX - app.x1) > app.absXDiff) or (abs(app.cursorY - app.y1) > app.absYDiff):
            tempLine = Line(app.cursorX, app.cursorY, app.x1, app.y1)
            app.allLines.append(tempLine)
            app.cursorX, app.cursorY = mouseX, mouseY
            app.x1, app.y1 = None, None
    pass

def onMouseMove(app, mouseX, mouseY):
    app.cursorX, app.cursorY = mouseX, mouseY
    pass
    
def onMouseRelease(app, mouseX, mouseY):
    if app.penMode:
        app.allObjects.append(app.allLines)
        app.allLines = []
        app.curorsX, app.cursorY = mouseX, mouseY
    pass

def main():
    runApp(width=1000, height=800)

main()

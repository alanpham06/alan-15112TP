from cmu_graphics import *
from urllib.request import urlopen
from PIL import Image, ImageDraw, ImageOps

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
class Pencil:
    def __init__(self, app):
         # Eventually used to check if mode is active or not
        self.mode = False
    
    def __eq__(self, other):
        return isinstance(other, Pencil)
    
    def __repr__(self):
        return f'Pencil'
    
    def __hash__(self):
        return hash(str(self))
    

class Pen:
    def __init__(self, app):
        # Eventually used to check if mode is active or not
        self.mode = False

    def __eq__(self, other):
        return isinstance(other, Pen)
    
    def __repr__(self):
        return f'Pen'
    
    def __hash__(self):
        return hash(str(self))

class Highlighter:
    def __init__(self, app):
        # Eventually used to check if mode is active or not
        self.mode = False

    def __eq__(self, other):
        return isinstance(other, Highlighter)
    
    def __repr__(self):
        return f'Highlighter'
    
    def __hash__(self):
        return hash(str(self))

class Eraser:
    def __init__(self, app):
        # Eventually used to check if mode is active or not
        self.mode = False
    
    def __eq__(self, other):
        return isinstance(other, Eraser)
    
    def __repr__(self):
        return f'Eraser'
    
    def __hash__(self):
        return hash(str(self))

class Ruler:
    def __init__(self, app):
        # Eventually used to check if mode is active or not
        self.mode = False

    def __eq__(self, other):
        return isinstance(other, Ruler)
    
    def __repr__(self):
        return f'Ruler'
    
    def __hash__(self):
        return hash(str(self))

class Lasso:
    def __init__(self, app):
        # Eventually used to check if mode is active or not
        self.mode = False

    def __eq__(self, other):
        return isinstance(other, Lasso)
    
    def __repr__(self):
        return f'Lasso'
    
    def __hash__(self):
        return hash(str(self))

class PreloadedShapesTool:
    def __init__(self, app):
        # Eventually used to check if mode is active or not
        self.mode = False
    
    def __eq__(self, other):
        return isinstance(other, PreloadedShapesTool)
    
    def __repr__(self):
        return f'Preloaded Shapes Tool'
    
    def __hash__(self):
        return hash(str(self))

class ShapeAutocorrect:
    def __init__(self, app):
        # Eventually used to check if mode is active or not
        self.mode = False
    
    def __eq__(self, other):
        return isinstance(other, ShapeAutocorrect)
    
    def __repr__(self):
        return f'Shape Autocorrect'
    
    def __hash__(self):
        return hash(str(self))

class PageMode:
    def __init__(self, app):
        # Eventually used to check if mode is active or not
        self.mode = False
    
    def __eq__(self, other):
        return isinstance(other, PageMode)
    
    def __repr__(self):
        return f'Page Mode'
    
    def __hash__(self):
        return hash(str(self))
    
# Load writing tool icon images into dictionary
def allWritingToolIcons(app):
    pencilUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/pencil-icon.jpg?raw=true'
    penUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/pen-icon-1.jpg?raw=true'
    highlighterUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/highlighter-icon-2.jpg?raw=true'
    eraserUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/eraser-icon.jpg?raw=true'
    rulerUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/ruler-icon.jpg?raw=true'
    lassoUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/lasso-icon-2.jpg?raw=true'
    preloadedShapesToolUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/preloaded-shapes-icon.jpg?raw=true'
    shapeAutocorrectUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/shape-autocorrect-icon-3.jpg?raw=true'
    pageModeUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/page-icon-2.jpg?raw=true'

    writingTools = ([Pencil(app), Pen(app), Highlighter(app), Eraser(app), Ruler(app), 
                    Lasso(app), PreloadedShapesTool(app), ShapeAutocorrect(app), PageMode(app)])
    allIconUrls = ([pencilUrl, penUrl, highlighterUrl, eraserUrl, rulerUrl, lassoUrl, 
                    preloadedShapesToolUrl, shapeAutocorrectUrl, pageModeUrl])
    allWritingToolIcons = dict()
    iconWidth = 70
    iconHeight = 65

    # Makes all the images and load them into a dictionary for easy access
    for i in range(len(writingTools)):
        currTool = writingTools[i]
        currUrl = allIconUrls[i]
        PILImage = loadPilImage(currUrl)
        PILImgResize = PILImage.resize((iconWidth, iconHeight))
        PILImgAdjusted = addRoundedCornersWithBG(PILImgResize, 20, (0, 0, 0, 0))
        cmuImgFinal = CMUImage(PILImgAdjusted)
        allWritingToolIcons[currTool] = cmuImgFinal
    
    return allWritingToolIcons

def loadPilImage(url):
    # Loads a PIL image from a url
    return Image.open(urlopen(url)) 

def makePilImage(imageWidth, imageHeight, bgColor):
    # Manually create a new PIL Image w/ given bg color:
    return Image.new('RGBA', (imageWidth, imageHeight), bgColor)

# ---------------------------------------------------------------------------
# ------- Heavily referenced ChatGPT to undertand L mode (grayscale), -------
# ------- ImageOps, .putalpha, and .paste                             -------
# ---------------------------------------------------------------------------                          
def addRoundedCorners(image, radius):
    # Create a mask for the rounded corners
    mask = Image.new("L", image.size, 0)  # L mode = grayscale
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0) + image.size, radius=radius, fill=255)
    
    # Apply the rounded corners mask to the image
    rounded_image = ImageOps.fit(image, image.size)
    rounded_image.putalpha(mask)
    
    return rounded_image

def addRoundedCornersWithBG(image, radius, bgColor):
    roundedImg = addRoundedCorners(image, radius)
    bg = Image.new("RGBA", image.size, bgColor)
    bg.paste(roundedImg, (0, 0), roundedImg)
    return bg
# --------------------------------------------------------------------------- 
# --------------------------------------------------------------------------- 

def makeCursorLines(pilImage):
    draw = ImageDraw.Draw(pilImage)
    imageWidth, imageHeight = pilImage.size
    # Add the cross to cursor
    draw.line((imageWidth//2, 0, imageWidth//2, imageHeight), width=3, fill='black')
    draw.line((0, imageHeight//2, imageWidth, imageHeight//2), width=3, fill='black')

def onAppStart(app):
    # Line spacing logic
    app.absXDiff = 3
    app.absYDiff = 3

    # States of drawing modes
    app.selectedWritingTool = None
    app.previousWritingTool = None

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

    app.writingTools = ([Pencil(app), Pen(app), Highlighter(app), Eraser(app), Ruler(app), 
                         Lasso(app), PreloadedShapesTool(app), ShapeAutocorrect(app), PageMode(app)])
    app.writingToolsIcons = allWritingToolIcons(app)
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
    # Draw tool bar + design
    drawRect(app.toolBarX, app.toolBarY-5, app.toolBarWidth+5, app.toolBarHeight+5, fill=app.toolBarBGColor)
    drawRect(app.toolBarX, app.toolBarY, app.toolBarWidth, app.toolBarHeight, fill=app.toolBarColor)
    # Draw writing utensil icons in tool bar
    for i in range(len(app.iconUpperLeftCorners)):
        leftX, topY = app.iconUpperLeftCorners[i]
        currWritingTool = app.writingTools[i]
        drawImage(app.writingToolsIcons[currWritingTool], leftX, topY)
    # Ensures selected tool is highlighted
    if (app.selectedWritingTool != None) and (app.selectedWritingTool.mode):
        indx = app.writingTools.index(app.selectedWritingTool)
        leftX, topY = app.iconUpperLeftCorners[indx]
        drawRect(leftX, topY, app.iconWidth, app.iconHeight, fill='yellow', opacity=20)

    # Draw cursor
    drawImage(app.cmuCursor, app.cursorX, app.cursorY, align='center')
    
    # Draw all of the lines
    for line in app.allLines:
        x0, y0, x1, y1 = line.x0, line.y0, line.x1, line.y1
        drawLine(x0, y0, x1, y1, fill=line.color, lineWidth=line.lineWidth)
    
    # Maintains all of the things already drawn on paper
    for line in app.allObjects:
        x0, y0, x1, y1 = line.x0, line.y0, line.x1, line.y1
        drawLine(x0, y0, x1, y1, fill=line.color, lineWidth=line.lineWidth)
    pass

def onMousePress(app, mouseX, mouseY):
    if (getWritingUtensilSelection(app, mouseX, mouseY) != None) and (app.selectedWritingTool == None):
        selectedIndx = getWritingUtensilSelection(app, mouseX, mouseY)
        app.selectedWritingTool = app.writingTools[selectedIndx]
        app.selectedWritingTool.mode = not app.selectedWritingTool.mode
    elif (getWritingUtensilSelection(app, mouseX, mouseY) != None) and (app.selectedWritingTool != None):
        selectedIndx = getWritingUtensilSelection(app, mouseX, mouseY)
        currWritingTool = app.writingTools[selectedIndx]
        if currWritingTool == app.selectedWritingTool:
            app.selectedWritingTool.mode = not app.selectedWritingTool.mode
            app.selectedWritingTool = None
        else:
            app.previousWritingTool = app.selectedWritingTool
            app.selectedWritingTool = currWritingTool
            app.previousWritingTool.mode = not app.previousWritingTool.mode
            app.selectedWritingTool.mode = not app.selectedWritingTool.mode
    pass

def onMouseDrag(app, mouseX, mouseY):
    if (app.selectedWritingTool == Pen(app)) and (app.selectedWritingTool.mode):
        # Drawing continuous lines logic
        app.x1, app.y1 = mouseX, mouseY
        if (((abs(app.cursorX - app.x1) > app.absXDiff) or (abs(app.cursorY - app.y1) > app.absYDiff)) and 
            ((app.y1 > app.toolBarY+app.toolBarHeight) or (app.x1 < app.toolBarX) or (app.x1 > app.toolBarX+app.toolBarWidth))):
            tempLine = Line(app.cursorX, app.cursorY, app.x1, app.y1)
            app.allLines.append(tempLine)
            app.cursorX, app.cursorY = mouseX, mouseY
            app.x1, app.y1 = None, None
    pass

def onMouseMove(app, mouseX, mouseY):
    app.cursorX, app.cursorY = mouseX, mouseY
    if (app.selectedWritingTool == Eraser(app)) and (app.selectedWritingTool.mode):
        for line in app.allObjects:
            x0, y0, x1, y1 = line.x0, line.y0, line.x1, line.y1
            if ((distance(x0, y0, mouseX, mouseY) < app.cursorWidth//2) or 
                (distance(x1, y1, mouseX, mouseY) < app.cursorWidth//2)):
                app.allObjects.remove(line)
    pass
    
def onMouseRelease(app, mouseX, mouseY):
    if app.allLines != []:
        firstLine = app.allLines[0]
        x0, y0 = firstLine.x0, firstLine.y0
        if distance(x0, y0, mouseX, mouseY) < 5:
            print('Back to starting point')
        else:
            print('Fail')

    if (app.selectedWritingTool == Pen(app)) and (app.selectedWritingTool.mode):
        # testing logic for shape autocorrect
        app.allObjects.extend(app.allLines)
        app.allLines = []
        app.curorsX, app.cursorY = mouseX, mouseY
    
    pass

def distance(x0, y0, x1, y1):
    return ((x1-x0)**2 + (y1-y0)**2)**0.5

def main():
    runApp(width=1000, height=800)

main()
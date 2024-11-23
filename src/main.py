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

        # Initialize image 
        url = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/pencil-icon.jpg?raw=true'
        pencilPILImage = loadPilImage(url)
        pencilPILImgResize = pencilPILImage.resize((app.iconWidth, app.iconHeight))
        pencilPILImgAdjusted = addRoundedCornersWithBG(pencilPILImgResize, 20, (0, 0, 0, 0))
        self.cmuImgFinal = CMUImage(pencilPILImgAdjusted)
    
    def __eq__(self, other):
        return isinstance(other, Pencil)
    

class Pen:
    def __init__(self, app):
        # Eventually used to check if mode is active or not
        self.mode = False

        # Initialize image 
        url = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/pen-icon-1.jpg?raw=true'
        penPILImage = loadPilImage(url)
        penPILImgResize = penPILImage.resize((app.iconWidth, app.iconHeight))
        penPILImgAdjusted = addRoundedCornersWithBG(penPILImgResize, 20, (0, 0, 0, 0))
        self.cmuImgFinal = CMUImage(penPILImgAdjusted)

    def __eq__(self, other):
        return isinstance(other, Pen)

class Highlighter:
    def __init__(self, app):
        # Eventually used to check if mode is active or not
        self.mode = False

        # Initialize image 
        url = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/highlighter-icon-2.jpg?raw=true'
        highlighterPILImage = loadPilImage(url)
        highlighterPILImgResize = highlighterPILImage.resize((app.iconWidth, app.iconHeight))
        highlighterPILImgAdjusted = addRoundedCornersWithBG(highlighterPILImgResize, 20, (0, 0, 0, 0))
        self.cmuImgFinal = CMUImage(highlighterPILImgAdjusted)

    def __eq__(self, other):
        return isinstance(other, Highlighter)

class Eraser:
    def __init__(self, app):
        # Eventually used to check if mode is active or not
        self.mode = False

        # Initialize image 
        url = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/eraser-icon.jpg?raw=true'
        eraserPILImage = loadPilImage(url)
        eraserPILImgResize = eraserPILImage.resize((app.iconWidth, app.iconHeight))
        eraserPILImgAdjusted = addRoundedCornersWithBG(eraserPILImgResize, 20, (0, 0, 0, 0))
        self.cmuImgFinal = CMUImage(eraserPILImgAdjusted)
    
    def __eq__(self, other):
        return isinstance(other, Eraser)

class Ruler:
    def __init__(self, app):
        # Eventually used to check if mode is active or not
        self.mode = False

        # Initialize image 
        url = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/ruler-icon.jpg?raw=true'
        rulerPILImage = loadPilImage(url)
        rulerPILImgResize = rulerPILImage.resize((app.iconWidth, app.iconHeight))
        rulerPILImgAdjusted = addRoundedCornersWithBG(rulerPILImgResize, 20, (0, 0, 0, 0))
        self.cmuImgFinal = CMUImage(rulerPILImgAdjusted)

    def __eq__(self, other):
        return isinstance(other, Ruler)

class Lasso:
    def __init__(self, app):
        # Eventually used to check if mode is active or not
        self.mode = False

        # Initialize image 
        url = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/lasso-icon-2.jpg?raw=true'
        lassoPILImage = loadPilImage(url)
        lassoPILImgResize = lassoPILImage.resize((app.iconWidth, app.iconHeight))
        lassoPILImgAdjusted = addRoundedCornersWithBG(lassoPILImgResize, 20, (0, 0, 0, 0))
        self.cmuImgFinal = CMUImage(lassoPILImgAdjusted)

    def __eq__(self, other):
        return isinstance(other, Lasso)

class PreloadedShapesTool:
    def __init__(self, app):
        # Eventually used to check if mode is active or not
        self.mode = False

        # Initialize image 
        url = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/preloaded-shapes-icon.jpg?raw=true'
        preloadedShapesToolPILImage = loadPilImage(url)
        preloadedShapesToolPILImgResize = preloadedShapesToolPILImage.resize((app.iconWidth, app.iconHeight))
        preloadedShapesToolPILImgAdjusted = addRoundedCornersWithBG(preloadedShapesToolPILImgResize, 20, (0, 0, 0, 0))
        self.cmuImgFinal = CMUImage(preloadedShapesToolPILImgAdjusted)
    
    def __eq__(self, other):
        return isinstance(other, PreloadedShapesTool)

class ShapeAutocorrect:
    def __init__(self, app):
        # Eventually used to check if mode is active or not
        self.mode = False

        # Initialize image 
        url = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/shape-autocorrect-icon-3.jpg?raw=true'
        shapeAutocorrectPILImage = loadPilImage(url)
        shapeAutocorrectPILImgResize = shapeAutocorrectPILImage.resize((app.iconWidth, app.iconHeight))
        shapeAutocorrectPILImgAdjusted = addRoundedCornersWithBG(shapeAutocorrectPILImgResize, 20, (0, 0, 0, 0))
        self.cmuImgFinal = CMUImage(shapeAutocorrectPILImgAdjusted)
    
    def __eq__(self, other):
        return isinstance(other, ShapeAutocorrect)

class PageMode:
    def __init__(self, app):
        # Eventually used to check if mode is active or not
        self.mode = False

        # Initialize image 
        url = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/page-icon-2.jpg?raw=true'
        pageModePILImage = loadPilImage(url)
        pageModePILImgResize = pageModePILImage.resize((app.iconWidth, app.iconHeight))
        pageModePILImgAdjusted = addRoundedCornersWithBG(pageModePILImgResize, 20, (0, 0, 0, 0))
        self.cmuImgFinal = CMUImage(pageModePILImgAdjusted)
    
    def __eq__(self, other):
        return isinstance(other, PageMode)

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
    app.absXDiff = 1
    app.absYDiff = 1

    # States of drawing modes
    app.selectedWritingTool = None

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
        drawImage(app.writingTools[i].cmuImgFinal, leftX, topY)
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
    for item in app.allObjects:
        for line in item:
            x0, y0, x1, y1 = line.x0, line.y0, line.x1, line.y1
            drawLine(x0, y0, x1, y1, fill=line.color, lineWidth=line.lineWidth)
    pass

def onMousePress(app, mouseX, mouseY):
    if getWritingUtensilSelection(app, mouseX, mouseY) != None:
        selectedIndx = getWritingUtensilSelection(app, mouseX, mouseY)
        app.selectedWritingTool = app.writingTools[selectedIndx]
        app.selectedWritingTool.mode = not app.selectedWritingTool.mode
    pass

def onMouseDrag(app, mouseX, mouseY):
    if (app.selectedWritingTool == Pen(app)) and (app.selectedWritingTool.mode):
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
    if (app.selectedWritingTool != None) and (app.selectedWritingTool.mode):
        app.allObjects.append(app.allLines)
        app.allLines = []
        app.curorsX, app.cursorY = mouseX, mouseY
    pass

def main():
    runApp(width=1000, height=800)

main()

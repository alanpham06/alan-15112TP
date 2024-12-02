from cmu_graphics import *
from urllib.request import urlopen
from PIL import Image, ImageDraw, ImageOps

# Create classes for each kind of object that will be drawn on the board
class Line:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.color = 'black'
        self.lineWidth = 3
        self.selected = False
    
    def __repr__(self):
        return f'Line from ({self.x0}, {self.y0}) to ({self.x1}, {self.y1})'

class Circle:
    def __init__(self, cx, cy, r):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.fill = 'white'
        self.border = 'black'
        self.borderWidth = 5
        self.opacity = 70
        self.dashes = False
        self.selected = False
    
    def __repr__(self):
        return f'Circle center:({self.cx},{self.cy}) radius:{self.r}'

class Polygon:
    def __init__(self, points):
        self.points = points
        self.fill = 'white'
        self.border = 'black'
        self.borderWidth = 5
        self.opacity = 70
        self.selected = False
    
    def __repr__(self):
        return f'Polygon with coordinates: {self.points}'
    
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
    app.absXDiff = 1
    app.absYDiff = 1
    # Shape Autocorrect Spacing Logic
    app.absXDiffAuto = 3
    app.absYDiffAuto = 3

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

    # Shape Autocorrect Trackers
    app.startAutoX = None
    app.startAutoY = None
    app.traceLines = []
    app.focalPoints = []
    app.focalPointRadius = 5

    # Lasso Mode Trackers
    app.startLassoX = None
    app.startLassoY = None
    app.autoCx, app.autoCy, app.autoR = None, None, None
    app.referX, app.referY = None, None
    app.selectLines = []
    app.startPoint = []
    app.autoRadius = 10
    pass

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
    
    if (app.selectedWritingTool == Pen(app)) and (app.selectedWritingTool.mode):
        # Draw all of the lines
        for line in app.allLines:
            x0, y0, x1, y1 = line.x0, line.y0, line.x1, line.y1
            drawLine(x0, y0, x1, y1, fill=line.color, lineWidth=line.lineWidth)

    elif (app.selectedWritingTool == ShapeAutocorrect(app)) and (app.selectedWritingTool.mode):
        for autoLine in app.traceLines:
            x0, y0, x1, y1 = autoLine.x0, autoLine.y0, autoLine.x1, autoLine.y1
            drawLine(x0, y0, x1, y1, fill=autoLine.color, lineWidth=autoLine.lineWidth)

        for point in app.focalPoints:
            cx, cy = point
            drawCircle(cx, cy, app.focalPointRadius, fill='green')

    elif (app.selectedWritingTool == Lasso(app)) and (app.selectedWritingTool.mode):
        for lassoLine in app.selectLines:
            x0, y0, x1, y1 = lassoLine.x0, lassoLine.y0, lassoLine.x1, lassoLine.y1
            drawLine(x0, y0, x1, y1, fill=lassoLine.color, lineWidth=lassoLine.lineWidth)
    
    # Maintains all of the things already drawn on paper
    for item in app.allObjects:
        if isinstance(item, Circle):
            cx, cy, r = item.cx, item.cy, item.r
            drawCircle(cx, cy, r, fill=item.fill, border=item.border, 
                       borderWidth=item.borderWidth, opacity=item.opacity, dashes=item.dashes)
        elif isinstance(item, Line):
            x0, y0, x1, y1 = item.x0, item.y0, item.x1, item.y1
            drawLine(x0, y0, x1, y1, fill=item.color, lineWidth=item.lineWidth)
        elif isinstance(item, Polygon):
            allPoints = item.points
            drawPolygon(*allPoints, fill=item.fill, border=item.border, 
                        borderWidth=item.borderWidth, opacity=item.opacity)
    pass

def onMousePress(app, mouseX, mouseY):
    # Ensures only 1 writing tool is selected at a time
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
    
    if ((app.selectedWritingTool == Lasso(app)) and (app.selectedWritingTool.mode) and (app.autoCx != None)):
        if distance(app.autoCx, app.autoCy, mouseX, mouseY) > app.autoR:
            app.autoCx, app.autoCy, app.autoR = None, None, None
            for item in app.allObjects:
                if isinstance(item, Circle) and item.dashes:
                    item.selected = not item.selected
                    app.allObjects.remove(item)
                elif item.selected:
                    item.selected = not item.selected
            resetLassoVars(app)
    pass

def onMouseDrag(app, mouseX, mouseY):
    app.x1, app.y1 = mouseX, mouseY

    # Drawing continuous lines logic
    if (((abs(app.cursorX - app.x1) > app.absXDiff) or (abs(app.cursorY - app.y1) > app.absYDiff)) and 
        ((app.y1 > app.toolBarY+app.toolBarHeight) or (app.x1 < app.toolBarX) 
        or (app.x1 > app.toolBarX+app.toolBarWidth))):
        if (app.selectedWritingTool == Pen(app)) and (app.selectedWritingTool.mode):
            tempLine = Line(app.cursorX, app.cursorY, app.x1, app.y1)
            app.allLines.append(tempLine)
        elif (app.selectedWritingTool == ShapeAutocorrect(app)) and (app.selectedWritingTool.mode):
            if app.traceLines == []:
                app.startAutoX = app.cursorX
                app.startAutoY = app.cursorY
            tracerLine = Line(app.cursorX, app.cursorY, app.x1, app.y1)
            tracerLine.color = 'lightSlateGray'
            app.traceLines.append(tracerLine)
        elif (app.selectedWritingTool == Lasso(app)) and (app.selectedWritingTool.mode):
            if app.selectLines == []:
                app.startLassoX = app.cursorX
                app.startLassoY = app.cursorY
                app.startPoint.append((app.startLassoX, app.startLassoY))
            selectLine = Line(app.cursorX, app.cursorY, app.x1, app.y1)
            selectLine.color = 'paleTurquoise'
            app.selectLines.append(selectLine)

    app.cursorX, app.cursorY = mouseX, mouseY
    app.x1, app.y1 = None, None
    pass

def onMouseMove(app, mouseX, mouseY):
    app.cursorX, app.cursorY = mouseX, mouseY
    if (app.selectedWritingTool == Eraser(app)) and (app.selectedWritingTool.mode):
        for item in app.allObjects:
            if isinstance(item, Line):
                x0, y0, x1, y1 = item.x0, item.y0, item.x1, item.y1
                if ((distance(x0, y0, mouseX, mouseY) < app.cursorWidth//2) or 
                    (distance(x1, y1, mouseX, mouseY) < app.cursorWidth//2)):
                    app.allObjects.remove(item)
            elif isinstance(item, Circle):
                cx, cy, r = item.cx, item.cy, item.r
                if (distance(cx, cy, mouseX, mouseY) < r):
                    app.allObjects.remove(item)
            elif isinstance(item, Polygon):
                cx, cy = findPolygonCenter(item.points)
                polygonRadius = findPolygonRadius(cx, cy, item.points)
                if distance(mouseX, mouseY, cx, cy) <= polygonRadius:
                    app.allObjects.remove(item)
    pass
    
def onMouseRelease(app, mouseX, mouseY):
    if (app.selectedWritingTool == Pen(app)) and (app.selectedWritingTool.mode):
        app.allObjects.extend(app.allLines)
        app.allLines = []
    elif ((app.selectedWritingTool == ShapeAutocorrect(app)) and (app.selectedWritingTool.mode)
         and (app.traceLines != [])):
        app.focalPoints.append((mouseX, mouseY))
        if distance(app.startAutoX, app.startAutoY, mouseX, mouseY) <= app.focalPointRadius:
            numOfFocalPoints = len(app.focalPoints)
            unpackedPoints = unpackTupleList(app.focalPoints)
            if numOfFocalPoints == 1:
                cx, cy, radius = getCircleFeatures(app.focalPoints, app.traceLines)
                newCircle = Circle(cx, cy, radius)
                app.allObjects.append(newCircle)
            elif numOfFocalPoints == 2:
                x0, y0, x1, y1 = unpackedPoints
                newLine = Line(x0, y0, x1, y1)
                app.allObjects.append(newLine)
            elif numOfFocalPoints > 2:
                newPolygon = Polygon(unpackedPoints)
                app.allObjects.append(newPolygon)
            resetShapeAutocorrectVars(app)
    elif ((app.selectedWritingTool == Lasso(app)) and (app.selectedWritingTool.mode)
         and (app.selectLines != [])):
         if distance(app.startLassoX, app.startLassoY, mouseX, mouseY) <= app.autoRadius:
            app.autoCx, app.autoCy, app.autoR = getCircleFeatures(app.startPoint, app.selectLines)
            newSelectCir = Circle(app.autoCx, app.autoCy, app.autoR)
            newSelectCir.opacity = 40
            newSelectCir.dashes = True
            newSelectCir.selected = True
            app.allObjects.append(newSelectCir)
            # Marks all of the items on screen that was selected
            for item in app.allObjects:
                if isinstance(item, Line):
                    x0, y0, x1, y1 = item.x0, item.y0, item.x1, item.y1
                    if ((distance(x0, y0, app.autoCx, app.autoCy) <= app.autoR) and 
                        (distance(x1, y1, app.autoCx, app.autoCy) <= app.autoR)):
                        item.selected = True
                elif isinstance(item, Circle) and (item.dashes != True):
                    cirCx, cirCy = item.cx, item.cy
                    if distance(cirCx, cirCy, app.autoCx, app.autoCy) < app.autoR:
                        item.selected = True
                elif isinstance(item, Polygon):
                    polyCx, polyCy = findPolygonCenter(item.points)
                    if distance(polyCx, polyCy, app.autoCx, app.autoCy) < app.autoR:
                        item.selected = True
            resetLassoVars(app)


    app.curorsX, app.cursorY = mouseX, mouseY
    pass

def onKeyHold(app, keys):
    if (app.selectedWritingTool == Lasso(app)) and (app.selectedWritingTool.mode) and (app.autoCx != None):
        if (('right' in keys) and ('up' in keys)) or (('d' in keys) and ('w' in keys)):
            xShift = +3
            yShift = -3
        elif (('right' in keys) and ('down' in keys)) or (('d' in keys) and ('s' in keys)):
            xShift = +3
            yShift = +3
        elif (('left' in keys) and ('up' in keys)) or (('a' in keys) and ('w' in keys)):
            xShift = -3
            yShift = -3
        elif (('left' in keys) and ('down' in keys)) or (('a' in keys) and ('s' in keys)):
            xShift = -3
            yShift = +3
        elif ('right' in keys) or ('d' in keys):
            xShift = +3
            yShift = 0
        elif ('left' in keys) or ('a' in keys):
            xShift = -3
            yShift = 0
        elif ('up' in keys) or ('w' in keys):
            xShift = 0
            yShift = -3
        elif ('down' in keys) or ('s' in keys):
            xShift = 0
            yShift = +3

        for lassoItem in app.allObjects:
            if lassoItem.selected:
                if isinstance(lassoItem, Line):
                    lassoItem.x0 += xShift
                    lassoItem.x1 += xShift
                    lassoItem.y0 += yShift
                    lassoItem.y1 += yShift
                elif isinstance(lassoItem, Circle):
                    lassoItem.cx += xShift
                    lassoItem.cy += yShift
                elif isinstance(lassoItem, Polygon):
                    for i in range(0, len(lassoItem.points), 2):
                        lassoItem.points[i] += xShift
                    for i in range(1, len(lassoItem.points), 2):
                        lassoItem.points[i] += yShift
    pass

def onKeyPress(app, key):
    if ((key == 'r') and (app.selectedWritingTool == ShapeAutocorrect(app)) and 
        (app.selectedWritingTool.mode) and (app.traceLines != [])):
        resetShapeAutocorrectVars(app)
    elif ((key == 'r') and (app.selectedWritingTool == Lasso(app)) and 
        (app.selectedWritingTool.mode) and (app.selectLines != [])):
        resetLassoVars(app)

    pass

# Helper functions used throughout the program
def getWritingUtensilSelection(app, mouseX, mouseY):
    for i in range(len(app.iconUpperLeftCorners)):
        left, top = app.iconUpperLeftCorners[i]
        right = left + app.iconWidth
        bottom = top + app.iconHeight
        if (mouseX > left) and (mouseX < right) and (mouseY < bottom) and (mouseY > top):
            return i
    return None

def resetLassoVars(app):
    app.startPoint = []
    app.selectLines = []
    app.startLassoX, app.startLassoY = None, None

def resetShapeAutocorrectVars(app):
    app.focalPoints = []
    app.traceLines = []
    app.startAutoX, app.startAutoY = None, None

def findPolygonCenter(points):
    totalX, numOfX = 0, 0
    totalY, numOfY = 0, 0
    for i in range(0, len(points), 2):
        currX = points[i]
        currY = points[i+1]
        totalX += currX
        numOfX += 1
        totalY += currY
        numOfY += 1
    return rounded(totalX/numOfX), rounded(totalY/numOfY)

def findPolygonRadius(cx, cy, points):
    minDist = None
    for i in range(0, len(points), 2):
        currX = points[i]
        currY = points[i+1]
        currDist = distance(cx, cy, currX, currY)
        if (minDist == None) or (currDist <= minDist):
            minDist = currDist
    return minDist

def getCircleFeatures(L, M):
    farDist = None
    farPtX, farPtY = None, None
    focalX, focalY = L[0]
    for line in M:
        currX, currY = line.x1, line.y1
        currDist = distance(currX, currY, focalX, focalY)
        if (farDist == None) or (currDist > farDist):
            farDist = currDist
            farPtX, farPtY = currX, currY
    radius = farDist//2
    cx, cy = midpoint(focalX, focalY, farPtX, farPtY)
    return cx, cy, radius

def unpackTupleList(L):
    result = []
    for tuple in L:
        val0, val1 = tuple
        result.append(val0)
        result.append(val1)
    return result
    
def midpoint(x0, y0, x1, y1):
    midptX = rounded((x0 + x1) / 2)
    midptY = rounded((y0 + y1) / 2)
    return midptX, midptY

def distance(x0, y0, x1, y1):
    return ((x1-x0)**2 + (y1-y0)**2)**0.5

def main():
    runApp(width=1000, height=800)

main()
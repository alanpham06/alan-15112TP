from cmu_graphics import *
from urllib.request import urlopen
from PIL import Image, ImageDraw, ImageOps
# Fix eraser, write instruction screens, fix movement 
# Create classes for each kind of object that will be drawn on the board
class Line:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.color = 'black'
        self.lineWidth = 3
        self.opacity = 100
        self.selected = False
    
    def __repr__(self):
        return f'Line from ({self.x0}, {self.y0}) to ({self.x1}, {self.y1})'

class Circle:
    def __init__(self, cx, cy, r):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.fill = None
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
        self.fill = None
        self.border = 'black'
        self.borderWidth = 5
        self.opacity = 70
        self.selected = False
    
    def __repr__(self):
        return f'Polygon with coordinates: {self.points}'
    
class RegPolygon:
    def __init__(self, cx, cy, r, points):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.points = points
        self.fill = None
        self.border = 'black'
        self.borderWidth = 3
        self.opacity = 70
        self.selected = False
    
    def __repr__(self):
        return f'Regular Polygon center: ({self.cx},{self.cy}), radius:{self.r}, points:{self.points}'
    
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
    
class Undo:
    def __init__(self, app):
        # Eventually used to check if mode is active or not
        self.mode = False
        
    def __eq__(self, other):
        return isinstance(other, Undo)
    
    def __repr__(self):
        return f'Undo'
    
    def __hash__(self):
        return hash(str(self))
    
class Reset:
    def __init__(self, app):
        # Eventually used to check if mode is active or not
        self.mode = False

    def __eq__(self, other):
        return isinstance(other, Reset)
    
    def __repr__(self):
        return f'Reset'
    
    def __hash__(self):
        return hash(str(self))
    
# Load writing tool icon images into dictionary
# Visit an-image-citation.md file in the src folder to see the citation for these writing tool icons
# Link: https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/an-image-citation.md 
def allWritingToolIcons(app):
    pencilUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/pencil-icon.jpg?raw=true'
    penUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/pen-icon-1.jpg?raw=true'
    highlighterUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/highlighter-icon-2.jpg?raw=true'
    eraserUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/eraser-icon.jpg?raw=true'
    lassoUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/lasso-icon-2.jpg?raw=true'
    preloadedShapesToolUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/preloaded-shapes-icon.jpg?raw=true'
    shapeAutocorrectUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/shape-autocorrect-icon-3.jpg?raw=true'
    pageModeUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/page-icon-2.jpg?raw=true'
    undoUrl = 'https://raw.githubusercontent.com/alanpham06/alan-15112TP/refs/heads/main/src/writing-tool-icons/undo-icon.jpg'
    resetUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/reset-icon.jpg?raw=true'
    writingTools = ([Pencil(app), Pen(app), Highlighter(app), Eraser(app), Lasso(app), 
                     PreloadedShapesTool(app), ShapeAutocorrect(app), PageMode(app),
                     Undo(app), Reset(app)])
    allIconUrls = ([pencilUrl, penUrl, highlighterUrl, eraserUrl, lassoUrl, 
                    preloadedShapesToolUrl, shapeAutocorrectUrl, pageModeUrl,
                    undoUrl, resetUrl])
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
# --Heavily referenced/copied code from ChatGPT to undertand               -- 
# --L mode (grayscale), ImageOps, .putalpha, and .paste                    --                                               --
# --ChatGPT Prompt: "How to make a mask over images in CMU Graphics to make--
# --pictures have rounded corners?"                                        --
# --Link: https://chatgpt.com/                                             --
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

# (1) Referenced "demo-pil-image-draw" from CMU 112 Website
# Link: https://www.cs.cmu.edu/~112/notes/tp-related-demos/tp-related-demos.html

def makeCursorLines(pilImage):
    draw = ImageDraw.Draw(pilImage)
    imageWidth, imageHeight = pilImage.size
    # Add the cross to cursor
    draw.line((imageWidth//2, 0, imageWidth//2, imageHeight), width=3, fill='black')
    draw.line((0, imageHeight//2, imageWidth, imageHeight//2), width=3, fill='black')

def onAppStart(app): 
    app.keys = []
    app.background = 'floralWhite'

    # Line spacing logic
    app.absXDiff = 0.1
    app.absYDiff = 0.1
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
    # (1) Initialize the cursor as PIL Image
    cursorBgColor = (0, 0, 0, 0)
    drawCursor = makePilImage(app.cursorWidth, app.cursorHeight, cursorBgColor)
    makeCursorLines(drawCursor)
    # (1) Convert it into a CMU image
    app.cmuCursor = CMUImage(drawCursor)

    # List of all the lines drawn
    app.allLines = []
    app.allObjects = []

    # Tool bar properties
    app.toolBarX = rounded(app.width * 0.1)
    app.toolBarY = rounded(app.height * 0.01)
    app.toolBarWidth = rounded(app.width * 0.85)
    app.toolBarHeight = rounded(app.height * 0.1)
    app.toolBarColor = 'lightGray'
    app.toolBarBGColor = 'silver'

    # Writing utensils icons in tool bar
    app.iconUpperLeftCorners = []
    numOfIcons = 10
    for i in range(numOfIcons):
        spacingBtwIcons = rounded(app.toolBarWidth/numOfIcons)
        cornerX = app.toolBarX + rounded(app.toolBarX * 0.1)
        cornerY = app.toolBarY + rounded(app.toolBarY * 0.8)
        app.iconUpperLeftCorners.append((cornerX + (i * spacingBtwIcons), cornerY))
    app.iconWidth = rounded(spacingBtwIcons * 0.8)
    app.iconHeight = rounded(app.toolBarHeight * 0.8)

    app.writingTools = ([Pencil(app), Pen(app), Highlighter(app), Eraser(app), Lasso(app), 
                         PreloadedShapesTool(app), ShapeAutocorrect(app), PageMode(app), 
                         Undo(app), Reset(app)])
    app.writingToolsIcons = allWritingToolIcons(app)

    # Writing Tool Properties
    app.pencilLineWidth = 3
    app.eraserRadius = 15
    app.penLineWidth = 3
    app.highlighterLineWidth = 15
    app.penColor = 'black'
    app.highlighterColor = 'yellow'

    # Pencil/Pen/Highlighter/Eraser Size Dropdown Menu
    app.sizeMenuX = app.toolBarX 
    app.sizeMenuY = app.toolBarY + app.toolBarHeight
    app.sizeMenuWidth = rounded(app.toolBarWidth*0.2)
    app.sizeMenuHeight = rounded(app.toolBarHeight*0.75)
    app.sizeMenuUpperLeftCorners = []
    sizeOffset = 10
    app.buttonWidth = 50
    app.buttonHeight = app.sizeMenuHeight - (sizeOffset*2)
    for i in range(3):
        left, top = app.sizeMenuX+sizeOffset + app.buttonWidth*i, app.sizeMenuY+sizeOffset
        app.sizeMenuUpperLeftCorners.append((left, top))
    app.sizeMenuColor = 'gainsboro'
    app.sizeButtonColors = ['aliceBlue', 'azure', 'aliceBlue']
    app.sizeButtonLabels = ['-', '', '+']
    app.currSize = None

    # Color Selection Dropdown Menu
    app.colorMenuX = app.sizeMenuX + app.sizeMenuWidth
    app.colorMenuY = app.toolBarY + app.toolBarHeight
    app.colorMenuWidth = rounded(app.toolBarWidth-app.sizeMenuWidth)
    app.colorMenuHeight = rounded(app.toolBarHeight*0.75)
    numOfColors = 10
    colorOffset = app.colorMenuWidth//numOfColors
    app.colorMenuCenters = []
    app.colorPaletteR = (app.colorMenuHeight*0.7)//2
    for i in range(numOfColors):
        colorCx = app.colorMenuX + app.colorPaletteR+5 + (colorOffset*i)
        colorCy = app.colorMenuY + app.colorPaletteR+10
        app.colorMenuCenters.append((colorCx, colorCy))
    app.colorMenuColor = 'gainsboro'
    app.colorMenuOptions = (['crimson', 'darkOrange', 'gold', 'forestGreen', 'royalBlue', 
                             'midnightBlue','violet', 'lightPink', 'saddleBrown', 'black'])
    app.selectedColor = None

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

    # Preloaded Shapes Tool Trackers
    app.regPolyCx, app.regPolyCy = None, None
    app.regPolyR = None
    app.regPolyPoints = None
    pass

# Referenced CMU Graphics Documentation to understand certain functions like Drawing Shapes
# Link: https://academy.cs.cmu.edu/docs 
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
        drawRect(leftX, topY, app.iconWidth+2, app.iconHeight, fill='yellow', opacity=20)
    # Draw proper dropdown menu for each tool
    if ((app.selectedWritingTool == Pencil(app)) and (app.selectedWritingTool.mode) or
        (app.selectedWritingTool == Pen(app)) and (app.selectedWritingTool.mode) or 
        (app.selectedWritingTool == Eraser(app)) and (app.selectedWritingTool.mode) or 
        (app.selectedWritingTool == Highlighter(app)) and (app.selectedWritingTool.mode)):
        drawRect(app.sizeMenuX, app.sizeMenuY, app.sizeMenuWidth, 
                 app.sizeMenuHeight, fill=app.sizeMenuColor)
        for i in range(len(app.sizeMenuUpperLeftCorners)):
            left, top = app.sizeMenuUpperLeftCorners[i]
            drawRect(left, top, app.buttonWidth, app.buttonHeight, fill=app.sizeButtonColors[i], border='black')
            if i%2==0:
                drawLabel(app.sizeButtonLabels[i], (left+app.buttonWidth//2), 
                          top+app.buttonHeight//2, size=30, bold=True)
            else:
                drawLabel(app.currSize, (left+app.buttonWidth//2), 
                          top+app.buttonHeight//2, size=15, bold=True, font='orbitron')
    
    if ((app.selectedWritingTool == Pen(app)) and (app.selectedWritingTool.mode) or 
          (app.selectedWritingTool == Highlighter(app)) and (app.selectedWritingTool.mode)):
        drawRect(app.colorMenuX, app.colorMenuY, app.colorMenuWidth, 
                 app.colorMenuHeight, fill=app.colorMenuColor)
        for i in range(len(app.colorMenuCenters)):
            cx, cy = app.colorMenuCenters[i]
            color = app.colorMenuOptions[i]
            drawCircle(cx, cy, app.colorPaletteR, fill=color, 
                       border=('yellow' if app.selectedColor==i else None))

    # Draw cursor
    if ((app.selectedWritingTool == Eraser(app)) and (app.selectedWritingTool.mode)):
        drawCircle(app.cursorX, app.cursorY, app.eraserRadius, fill=None, border='dimGray', dashes=True)
    drawImage(app.cmuCursor, app.cursorX, app.cursorY, align='center')
    
    if (((app.selectedWritingTool == Pencil(app)) and (app.selectedWritingTool.mode)) or
        ((app.selectedWritingTool == Pen(app)) and (app.selectedWritingTool.mode)) or 
        ((app.selectedWritingTool == Highlighter(app)) and (app.selectedWritingTool.mode))):
        # Draw all of the lines
        for line in app.allLines:
            x0, y0, x1, y1 = line.x0, line.y0, line.x1, line.y1
            drawLine(x0, y0, x1, y1, fill=line.color, lineWidth=line.lineWidth, opacity=line.opacity)

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
            drawLine(x0, y0, x1, y1, fill=item.color, lineWidth=item.lineWidth, opacity=item.opacity)
        elif isinstance(item, Polygon):
            allPoints = item.points
            drawPolygon(*allPoints, fill=item.fill, border=item.border, 
                        borderWidth=item.borderWidth, opacity=item.opacity)
        elif isinstance(item, RegPolygon):
            regCx, regCy, regR, regPts = item.cx, item.cy, item.r, item.points
            drawRegularPolygon(regCx, regCy, regR, regPts, fill=item.fill, border=item.border, 
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
    
    # Allows for button presses to alter size of writing tools
    sizeSelection = getSizeCounter(app, mouseX, mouseY)
    if ((app.selectedWritingTool == Pencil(app)) and (app.selectedWritingTool.mode)):
        if (sizeSelection == '-') and (app.pencilLineWidth > 1):
            app.pencilLineWidth -= 0.25
        elif (sizeSelection == '+'):
            app.pencilLineWidth += 0.25
        app.currSize = app.pencilLineWidth
    elif ((app.selectedWritingTool == Pen(app)) and (app.selectedWritingTool.mode)):
        if (sizeSelection == '-') and (app.pencilLineWidth > 1):
            app.penLineWidth -= 0.25
        elif (sizeSelection == '+'):
            app.penLineWidth += 0.25
        app.currSize = app.penLineWidth
    elif ((app.selectedWritingTool == Highlighter(app)) and (app.selectedWritingTool.mode)):
        if (sizeSelection == '-') and (app.pencilLineWidth > 1):
            app.highlighterLineWidth -= 0.25
        elif (sizeSelection == '+'):
            app.highlighterLineWidth += 0.25
        app.currSize = app.highlighterLineWidth
    elif ((app.selectedWritingTool == Eraser(app)) and (app.selectedWritingTool.mode)):
        if (sizeSelection == '-') and (app.eraserRadius > 1):
            app.eraserRadius -= 1
        elif (sizeSelection == '+'):
            app.eraserRadius += 1
        app.currSize = app.eraserRadius
    
    # Allows for users to choose their colors
    colorIndx = getColorSelection(app, mouseX, mouseY)
   
    if (colorIndx != None):
        colorSelection = app.colorMenuOptions[colorIndx]
        app.selectedColor = colorIndx
        if ((app.selectedWritingTool == Pen(app)) and (app.selectedWritingTool.mode)):
            app.penColor = colorSelection
        elif ((app.selectedWritingTool == Highlighter(app)) and (app.selectedWritingTool.mode)):
            app.highlighterColor = colorSelection
            
    if ((app.selectedWritingTool == PreloadedShapesTool(app)) and (app.selectedWritingTool.mode)):
        if ((app.regPolyCx != None) and (app.regPolyCy != None) and 
            (app.regPolyR != None) and (app.regPolyPoints != None)):
            regPoly = RegPolygon(app.regPolyCx, app.regPolyCy, app.regPolyR, app.regPolyPoints)
            app.allObjects.append(regPoly)
            resetRegPolygon(app)
        elif ((app.regPolyR != None) and (app.regPolyPoints != None) and 
            (mouseY > app.toolBarY+app.toolBarHeight+app.regPolyR) or (mouseX < app.toolBarX) 
            or (mouseX > app.toolBarX+app.toolBarWidth)):
            app.regPolyCx, app.regPolyCy = mouseX, mouseY
        else:
            response = app.getTextInput('''What is the radius and number of points for this regular polygon?
                                    \nPlease response in the following format with numerical values: 
                                    (radius),(number of points)''')
            app.regPolyR, app.regPolyPoints = getRegPolyFeatures(response)
        
    
    if (app.autoCx != None) and (distance(app.autoCx, app.autoCy, mouseX, mouseY) > app.autoR):
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
        if (app.selectedWritingTool == Pencil(app)) and (app.selectedWritingTool.mode):
            pencilLine = Line(app.cursorX, app.cursorY, app.x1, app.y1)
            # Referenced palettemaker.com to find rgb value of graphite for pencil
            # https://palettemaker.com/colors/graphite 
            graphite = rgb(65, 66, 76)
            pencilLine.color = graphite
            pencilLine.lineWidth = app.pencilLineWidth
            app.allLines.append(pencilLine)
        elif (app.selectedWritingTool == Pen(app)) and (app.selectedWritingTool.mode):
            penLine = Line(app.cursorX, app.cursorY, app.x1, app.y1)
            penLine.color = app.penColor
            penLine.lineWidth = app.penLineWidth
            app.allLines.append(penLine)
        elif (app.selectedWritingTool == Highlighter(app)) and (app.selectedWritingTool.mode):
            highlighterLine = Line(app.cursorX, app.cursorY, app.x1, app.y1)
            highlighterLine.color = app.highlighterColor
            highlighterLine.lineWidth = app.highlighterLineWidth
            highlighterLine.opacity = 40
            app.allLines.append(highlighterLine)
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
                if ((distance(x0, y0, mouseX, mouseY) < app.eraserRadius) or 
                    (distance(x1, y1, mouseX, mouseY) < app.eraserRadius)):
                    app.allObjects.remove(item)
            elif isinstance(item, Circle):
                cx, cy, r = item.cx, item.cy, item.r
                if (distance(cx, cy, mouseX, mouseY) < r+app.eraserRadius):
                    app.allObjects.remove(item)
            elif isinstance(item, Polygon):
                cx, cy = findPolygonCenter(item.points)
                polygonRadius = findPolygonRadius(cx, cy, item.points)
                if distance(mouseX, mouseY, cx, cy) <= polygonRadius+app.eraserRadius:
                    app.allObjects.remove(item)
            elif isinstance(item, RegPolygon):
                regCx, regCy, regR = item.cx, item.cy, item.r
                if (distance(regCx, regCy, mouseX, mouseY) < regR+app.eraserRadius):
                    app.allObjects.remove(item)
    pass
    
def onMouseRelease(app, mouseX, mouseY):
    if (((app.selectedWritingTool == Pencil(app)) and (app.selectedWritingTool.mode)) or
        ((app.selectedWritingTool == Pen(app)) and (app.selectedWritingTool.mode)) or 
        ((app.selectedWritingTool == Highlighter(app)) and (app.selectedWritingTool.mode))):
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
                elif isinstance(item, RegPolygon):
                    regPolyCx, regPolyCy = item.cx, item.cy
                    if distance(regPolyCx, regPolyCy, app.autoCx, app.autoCy) < app.autoR:
                        item.selected = True
            resetLassoVars(app)
        else:
            resetLassoVars(app)

    app.curorsX, app.cursorY = mouseX, mouseY
    pass

def onKeyHold(app, keys):
    if (app.selectedWritingTool == Lasso(app)) and (app.selectedWritingTool.mode) and (app.autoCx != None):
        xShift, yShift = 0, 0
        if (('right' in app.keys) and ('up' in app.keys)) or (('d' in app.keys) and ('w' in app.keys)):
            xShift = +3
            yShift = -3
        elif (('right' in app.keys) and ('down' in app.keys)) or (('d' in app.keys) and ('s' in app.keys)):
            xShift = +3
            yShift = +3
        elif (('left' in app.keys) and ('up' in app.keys)) or (('a' in app.keys) and ('w' in app.keys)):
            xShift = -3
            yShift = -3
        elif (('left' in app.keys) and ('down' in app.keys)) or (('a' in app.keys) and ('s' in app.keys)):
            xShift = -3
            yShift = +3
        elif ('right' in app.keys) or ('d' in app.keys):
            xShift = +3
            yShift = 0
        elif ('left' in app.keys) or ('a' in app.keys):
            xShift = -3
            yShift = 0
        elif ('up' in app.keys) or ('w' in app.keys):
            xShift = 0
            yShift = -3
        elif ('down' in app.keys) or ('s' in app.keys):
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
                elif isinstance(lassoItem, RegPolygon):
                    lassoItem.cx += xShift
                    lassoItem.cy += yShift
    pass

def onKeyRelease(app, key):
    if (app.selectedWritingTool == Lasso(app)) and (app.selectedWritingTool.mode):
        app.keys.remove(key)
    pass

def onKeyPress(app, key):
    if ((key == 'r') and (app.selectedWritingTool == ShapeAutocorrect(app)) and 
        (app.selectedWritingTool.mode) and (app.traceLines != [])):
        resetShapeAutocorrectVars(app)
    elif ((key == 'r') and (app.selectedWritingTool == Lasso(app)) and 
        (app.selectedWritingTool.mode) and (app.selectLines != [])):
        resetLassoVars(app)
    else:
        app.keys.append(key)
    pass

# Helper functions used throughout the program
def getColorSelection(app, mouseX, mouseY):
    for i in range(len(app.colorMenuCenters)):
        cx, cy = app.colorMenuCenters[i]
        if distance(cx, cy, mouseX, mouseY) < app.colorPaletteR:
            return i
    return None

def getSizeCounter(app, mouseX, mouseY):
    for i in range(len(app.sizeMenuUpperLeftCorners)):
        left, top = app.sizeMenuUpperLeftCorners[i]
        right = left + app.buttonWidth
        bottom = top + app.buttonHeight
        if (mouseX > left) and (mouseX < right) and (mouseY < bottom) and (mouseY > top):
            return app.sizeButtonLabels[i]
    return None
    
def resetRegPolygon(app):
    app.regPolyCx, app.regPolyCy = None, None
    app.regPolyR = None
    app.regPolyPoints = None

def getRegPolyFeatures(s):
    if ',' in s:
        commaIndx = s.find(',')
        regPolyR = s[:commaIndx]
        regPolyPts = s[commaIndx+1:]
        if regPolyR.isdigit() and regPolyPts.isdigit():
            return int(regPolyR), int(regPolyPts)
    return None, None

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
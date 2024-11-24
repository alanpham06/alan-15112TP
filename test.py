from cmu_graphics import *
from urllib.request import urlopen
from PIL import Image, ImageDraw, ImageOps

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
    
def allWritingToolIcons():
    pencilUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/pencil-icon.jpg?raw=true'
    penUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/pen-icon-1.jpg?raw=true'
    highlighterUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/highlighter-icon-2.jpg?raw=true'
    eraserUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/eraser-icon.jpg?raw=true'
    rulerUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/ruler-icon.jpg?raw=true'
    lassoUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/lasso-icon-2.jpg?raw=true'
    preloadedShapesToolUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/preloaded-shapes-icon.jpg?raw=true'
    shapeAutocorrectUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/shape-autocorrect-icon-3.jpg?raw=true'
    pageModeUrl = 'https://github.com/alanpham06/alan-15112TP/blob/main/src/writing-tool-icons/page-icon-2.jpg?raw=true'

    writingTools = ([Pencil, Pen, Highlighter, Eraser, Ruler, Lasso, 
                     PreloadedShapesTool, ShapeAutocorrect, PageMode])
    allIconUrls = ([pencilUrl, penUrl, highlighterUrl, eraserUrl, rulerUrl, lassoUrl, 
                    preloadedShapesToolUrl, shapeAutocorrectUrl, pageModeUrl])
    allWritingToolIcons = dict()
    iconWidth = 10
    iconHeight = 10

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

print(allWritingToolIcons())
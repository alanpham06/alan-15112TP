from cmu_graphics import *

def onAppStart(app):
    # Cursor properties
    app.cx = 200
    app.cy = 200
    app.r = 20

    # Current line endpoints
    app.x0 = None
    app.y0 = None
    app.x1 = None
    app.y1 = None

    # List of all the lines/temp circles
    app.lines = []
    app.circs = []
    pass

def redrawAll(app):
    # Draw cursor
    drawCircle(app.cx, app.cy, app.r, fill='aqua')

    # Draw temp circles
    for cx, cy in app.circs:
        drawCircle(cx, cy, 5, fill='black')

    if (app.x0 != None) and (app.y0 != None) and (app.x1 != None) and (app.y1 != None):
        drawLine(app.x0, app.y0, app.x1, app.y1, fill='black', lineWidth=10)
    pass

def onMousePress(app, mouseX, mouseY):
    app.x0, app.y0 = mouseX, mouseY
    app.circs.append((app.x0, app.y0))
    app.lines.append(app.x0)
    app.lines.append(app.y0)
    pass

def onMouseHold(app, mouseX, mouseY):
    app.x1, app.y1 = mouseX, mouseY
    app.circs.append((app.x1, app.y1))
    app.lines.append(app.x1)
    app.lines.append(app.y1)

def onMouseMove(app, mouseX, mouseY):
    app.cx, app.cy = mouseX, mouseY
    app.x1, app.y1 = mouseX, mouseY
    pass
    

def onMouseRelease(app, mouseX, mouseY):
    app.x1, app.y1 = mouseX, mouseY
    pass

def onStep(app):
    pass

def main():
    runApp()

main()

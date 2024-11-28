points = [100, 100, 100, 200, 200, 200, 200, 100]
x, y = 150, 150

numOfIntersections = 0
prevPtX, prevPtY = None, None
for i in range(0, len(points), 2):
    currPtX = points[i]
    currPtY = points[i+1]
    if (prevPtX == None) and (prevPtY == None):
        prevPtX, prevPtY = currPtX, currPtY
        continue
    minY = min(prevPtY, currPtY)
    maxY = max(prevPtY, currPtY)
    print(minY, maxY, currPtX, currPtY)
    if (x <= prevPtX) and (x <= currPtX) and (y >= minY) and (y <= maxY):
        numOfIntersections += 1
    prevPtX, prevPtY = currPtX, currPtY
    
print(numOfIntersections)
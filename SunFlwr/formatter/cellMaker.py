'''
CellMaker module.
This module is the low-level formatter of the excel evaluation generator.
this class is the basic contruction for  doing cells  which will include:
    - cells that only contain values and a location.
    - cells that need ot be merged with more adjecent tables.
'''
from openpyxl import Workbook

def addCell(ws, x, y, text, dx =0, dy=0):
    '''
    create cells with predifinied coodenates(cartesan) and size(merged cells).
    ws = worksheet
    x = horizontal axis (letters)
    y = vertical axis (numbers)
    length = lenght of the cell if happens to merge.
    '''
    if dx or dy > 0:
        ws.merge_cells(mergeCoordRange(x,y,dx,dy))
    ws[genCoord(x,y)] = text

def genCoord(x,y):
    """
    coverts number to cordenates to excel format coordinates.
    """
    return '{0}{1}'.format(chr(x+64),y)

def mergeCoordRange(x,y,dx=0,dy=0):
    '''
        Genrates a range of two excel coordinate points.
    '''
    return '{0}:{1}'.format(genCoord(x,y),genCoord(x+dx,y+dy))

if __name__ == '__main__':
    print(genCoord(1,2))
    print(mergeCoordRange(1,2,3))
    print(mergeCoordRange(1,2,3,4))

    wb = Workbook()
    ws = wb.active
    for i in range(1,10):
        addCell(ws,1,i,i, dx = i)

    wb.save('sheets/loop.xlsx')

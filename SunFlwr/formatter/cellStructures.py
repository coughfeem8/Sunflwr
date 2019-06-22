'''
module cell structures this modules is made for  creating more complex
cells strucures in an excel sheet.
the following strucures can be created:
    - label with value.
    - label columns
    - picture frames
    - section titles
'''
from cellMaker import addCell
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.drawing.image import Image



def makeLabeledField(ws,label, value):
    for cell in (label,value):
        print(cell['text'])
        addCell(ws,
                cell['posx'],cell['posy'],
                cell['text'],
                cell['dimx'],cell['dimy'])

def makeTable(ws,columns,data,x ,y ,padding=0):
    '''
    # TODO: still need to check if making tables does work.
    '''
    for i, col in enumerate(columns):
        # add the column wiht optional padding.
        cell = createCell(x+(i*padding), y, col, dx=padding)
        print(cell)
        addCell(ws,
                cell['posx'], cell['posy'],
                cell['text'],
                cell['dimx'], cell['dimy'])


    for row in data:
        for i, item in enumerate(row):
            # add items for the table.
            cell = createCell(x+(i*padding), y, item, dx=padding)
            print(cell)
            addCell(ws,
                    cell['posx'], cell['posy'],
                    cell['text'],
                    cell['dimx'], cell['dimy'])



def maketitle(ws, title, y):
    '''
    create a cell that will merge a whole row to do a title.
    (i.e)|                                          Title|
    '''
    cell = createCell(1, y, title, dx=17) #ord('R')- ord('A') =17
    addCell(ws,
            cell['posx'],cell['posy'],
            cell['text'],
            cell['dimx'],cell['dimy'])

def makeLabeledField(ws,label, value):
    '''
    create two cells that following the Label and the value for the Label
    (i.e.) |LABEL: | value|
    '''
    for cell in (label,value):
        addCell(ws,
                cell['posx'],cell['posy'],
                cell['text'],
                cell['dimx'],cell['dimy'])

def createCell(x, y, text, dx =0, dy=0):
    return {'text': text,
            'posx' : x,'posy' : y,
            'dimx' : dx,'dimy' : dy}

if __name__ == '__main__':
    from openpyxl import Workbook
    wb= Workbook()
    ws = wb.active
    label = createCell(1,1,"label",dx=4)
    value = createCell(2,2,"value", dy=0)


    makeLabeledField(ws,label,value)
    #testing titles
    maketitle(ws,"TITULO",6)

    #testing tables
    data = [
        ['Apples', 10000, 5000, 8000, 6000],
        ['Pears',   2000, 3000, 4000, 5000],
        ['Bananas', 6000, 6000, 6500, 6000],
        ['Oranges',  500,  300,  200,  700],
    ]

    cols = ["Fruit", "2011", "2012", "2013", "2014"]

    makeTable(ws,cols,data,2 ,7)
    makeTable(ws,cols,data,14 ,15,padding = 3)
    wb.save('sheets/structuresTest.xlsx')

'''
module cell structures this modules is made for  creating more complex
cells strucures in an excel sheet.
the following strucures can be created:
    - label with value.
    - picture with and without frames
    - section titles
    - tables
'''
from cellMaker import add_cell, add_image
# from openpyxl.worksheet.table import Table, TableStyleInfo
# from openpyxl.drawing.image import Image


def make_table(ws, columns, data, x, y, padding=0):
    make_row(ws, columns, x, y, padding)      # table titles
    for i, row in enumerate(data):            # table contents
        make_row(ws, row, x, y+i, padding)  # incremeted for the title row.


def make_row(ws, items, x, y, padding=0):
    '''Creates a row of evenly spaced items in a excel spreadsheet.'''
    for i, item in enumerate(items):
        cell = create_cell(x+(i+i*padding), y, item, dx=padding)
        print("{0}: {1},{2}".format(cell['text'], cell['posx'], cell['posy']))
        add_cell(ws,
                 cell['posx'], cell['posy'],
                 cell['text'],
                 cell['dimx'], cell['dimy'])


def make_title(ws, title, y):
    '''
    create a cell that will merge a whole row to do a title.
    (i.e)|                                          Title|
    '''
    cell = create_cell(1, y, title, dx=17)  # ord('R')- ord('A') =17
    add_cell(ws,
             cell['posx'], cell['posy'],
             cell['text'],
             cell['dimx'], cell['dimy'])


def make_labeled_field(ws, label, value):
    '''
    create two cells that following the Label and the value for the Label
    (i.e.) |LABEL: | value|
    '''
    for cell in (label, value):
        add_cell(ws,
                 cell['posx'], cell['posy'],
                 cell['text'],
                 cell['dimx'], cell['dimy'])


def create_cell(x, y, text, dx=0, dy=0):
    '''formats cell data into a dictionary.'''
    return {'text': text,
            'posx': x, 'posy': y,
            'dimx': dx, 'dimy': dy}


if __name__ == '__main__':
    from openpyxl import Workbook
    wb = Workbook()
    ws = wb.active
    label = create_cell(1, 1, "label", dx=4)
    value = create_cell(2, 2, "value", dy=0)

    make_labeled_field(ws, label, value)
    # testing titles
    make_title(ws, "TITULO", 6)

    # testing tables
    data = [
        ['Apples', 10000, 5000, 8000, 6000],
        ['Pears',   2000, 3000, 4000, 5000],
        ['Bananas', 6000, 6000, 6500, 6000],
        ['Oranges',  500,  300,  200,  700],
    ]

    cols = ["Fruit", "2011", "2012", "2013", "2014"]

    make_table(ws, cols, data, 2, 7)
    make_table(ws, cols, data, 14, 15, padding=2)
    # for i, row in enumerate(data):
    #    make_row(ws, row, 2, 15+i, padding=1)
    # wb.save('tests/sheets/structuresTest.xlsx')
    print('document test written')

from nose.tools import *
from Conor.main import *

def test_file_read():
    file_url="http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    eq_(read_file(file_url)[:20],'1000\nturn off 660,55',"Error: First 20 characters do not match")

def test_return_coordinates():
    eq_(return_coordinates("200,500"), [200,500], "Conversion error")

def test_turn_on():
    test_board=LED_board(5)
    test_board.turn_on([0,0], [4,3])
    on_count=0
    for i in range(0,5):
        for j in range(0,5):
            if test_board.array[i][j]==1:
                on_count+=1
    eq_(on_count, 20, "Incorrect number of lights on")

def test_turn_off():
    test_board=LED_board(5)
    test_board.turn_on([0,0], [3,3])
    test_board.turn_off([0,0], [0,3])
    on_count=0
    for i in range(0,5):
        for j in range(0,5):
            if test_board.array[i][j]==1:
                on_count+=1
    eq_(on_count, 12, "Incorrect number of lights on")
    
def test_toggle():
    test_board=LED_board(5)
    test_board.toggle([0,0], [2,2])
    on_count=0
    for i in range(0,5):
        for j in range(0,5):
            if test_board.array[i][j]==1:
                on_count+=1
    eq_(on_count, 9, "Incorrect number of lights")
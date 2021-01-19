#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 11
day = 19

def test_code():
    assert sumBetween(1,2) == 0, "x = 1 y = 2 failed"
    assert sumBetween(3,7) == 15, "x = 3 y = 7 failed"
    assert sumBetween(0,2) == 1, "x = 0 y = 1 failed"

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"

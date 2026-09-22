import time

import pytest

from assignment import find_closest, integer_sqrt, find_missing


class CountingList(list):

    def __init__(self, *args):
        super().__init__(*args)
        self.accesses = 0

    def __getitem__(self, index):
        self.accesses += 1
        return super().__getitem__(index)

    def __iter__(self):
        self.accesses += len(self)
        return super().__iter__()

    def __contains__(self, value):
        self.accesses += len(self)
        return super().__contains__(value)

    def index(self, *args):
        self.accesses += len(self)
        return super().index(*args)

    def count(self, value):
        self.accesses += len(self)
        return super().count(value)


DATA = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]



@pytest.mark.parametrize(
    "data, target, expected",
    [
        [DATA, 13, 12],    
        [DATA, 14, 12],    
        [DATA, 30, 23], 
        [DATA, 31, 38],     
        [DATA, 23, 23],    
        [DATA, 1, 2],     
        [DATA, 100, 91], 
        [DATA, 2, 2],     
        [DATA, 91, 91],   
        [[7], 100, 7],      
        [[10, 20], 15, 10],
    ]
)
def test1(data, target, expected):
    assert find_closest(data, target) == expected


def test1_efficiency():
    data = CountingList(range(0, 400000, 4))  
    assert find_closest(data, 123457) == 123456
    checked = data.accesses
    assert checked < 200, (
        "Too many elements checked (%d). Exercise 1 must use binary search."
        % checked
    )


# --- Exercise 2: Integer square root ---
@pytest.mark.parametrize(
    "n, expected",
    [
        [0, 0],
        [1, 1],
        [2, 1],
        [3, 1],
        [4, 2],
        [8, 2],
        [9, 3],
        [15, 3],
        [16, 4],
        [24, 4],
        [25, 5],
        [100, 10],
        [999, 31],
        [1000000, 1000],
    ]
)
def test2(n, expected):
    assert integer_sqrt(n) == expected


def test2_efficiency():
    start = time.time()
    assert integer_sqrt(10000000000000000) == 100000000
    elapsed = time.time() - start
    assert elapsed < 1.0, (
        "Took %.1f seconds. Exercise 2 must use binary search, not a loop "
        "that counts upwards." % elapsed
    )

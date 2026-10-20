import airtime

def test_airtime_function_1():
    assert(airtime.airtime([0,5,0])== 1)

def test_airtime_function_2():
    assert(airtime.airtime([1,2,3,4,5])== 0)


def test_airtime_function_3():
    assert(airtime.airtime([1,2,3,3,4,5,6,5,4,4,4,3,2])== 3)
import quickbrownfox

def test_quickfox_1():
    assert(quickbrownfox.letter_checker("The quick brown fox jumps over the lazy dog.")== "")

def test_quickfox_2():
    assert(quickbrownfox.letter_checker("abcdefghijklmnopqrstuvwxy")== "z")

def test_quickfox_3():
    assert(quickbrownfox.letter_checker("defghijklmnopqrstuvw")== "abcxyz")



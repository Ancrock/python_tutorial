from nose.tools import *
from ex47.game import Room

def test_room():
    gold = Room("Gold Room", "This room has gold in it.")
    assert_equal(gold.name, "Gold Room")
    assert_equal(gold.paths, {})
    
def test_get():
    gold = Room("Gold Room", "This room has gold in it.")
    gold.add_paths({"west": "Please go west"})
    f = gold.go("west")
    assert_equal(f, "Please go west")
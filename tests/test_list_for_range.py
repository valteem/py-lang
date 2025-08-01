import pytest

def test_list_of_class_objects_for_range():

    class Food:
        def __init__(self, name, expired):
            self.name = name
            self.expired = expired

    food_items = [
        Food("apples", False),
        Food("cherries", False),
        Food("onions", False)
    ]

    for f in food_items:
        f.expired = True

    for f in food_items:
        assert f.expired == True
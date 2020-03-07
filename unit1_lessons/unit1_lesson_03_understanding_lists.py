__author__ = 'Kalyan'

from placeholders import *

notes = '''
python list is a ordered mutable sequence of objects. You will see that some
of the ideas/concepts that are introduced in strings also apply to lists 
(slicing, indexing etc).

experiment in console to learn and make these tests pass.
'''

def test_list_type():
    fruits = ["banana", "orange", "grape"]
    assert __ == type(fruits).__name__

def test_list_len():
    fruits = ["banana", "orange", "grape"]
    assert __ == len(fruits)

def test_list_can_be_indexed():
    fruits = ["banana", "orange", "grape"]
    assert __ == fruits[0]
    assert __ == fruits[1]
    assert __ == fruits[2]
    assert __ == fruits[-1]
    assert __ == fruits[-2]
    assert __ == fruits[-3]

def test_list_is_mutable():
    fruits = ["banana", "orange", "grape"]
    fruits[0] = "mango"
    assert [__] == fruits  #replace __ with expected contents of list

def test_list_can_be_sliced():
    """
     Slicing works the same as on strings
    """
    fruits = ["banana", "orange", "grape"]
    assert [__] == fruits[0:0]

    #begin : end
    assert [__] == fruits[0:2]
    assert [__] == fruits[0:5]
    assert [__] == fruits[1:-1]

    # begin :
    assert [__] == fruits[0:]
    assert [__] == fruits[2:]
    assert [__] == fruits[0:]

    #: end
    assert [__] == fruits[:0]
    assert [__] == fruits[:2]
    assert [__] == fruits[:5]

    # note the invariant
    assert [__] == fruits[:1] + fruits[1:]


def test_slice_creates_a_new_list():
    fruits = ["banana", "orange", "grape"]
    slice = fruits[0:2]
    slice.append("guava")

    assert [__] == fruits # did this change?
    assert [__] == slice


def test_list_merge():
    fruits = ["banana", "orange", "grape"]
    veggies = ["beetroot", "tomato"]
    all = fruits + veggies

    assert [__] == all
    assert [__] == fruits
    assert [__] == veggies
    assert [__] == fruits[1:] + veggies[:1]

def test_list_slice_replacement_is_inplace():
    fruits = ["banana", "orange", "grape"]

    fruits[1:2] = ["litchi", "guava"]
    assert [__] == fruits

    fruits[3:] = []
    assert [__] == fruits

    fruits[:2] = []
    assert [__] == fruits

def test_list_common_methods():
    """
     You can find methods supported by lists by entering []. (note the dot)
     in the python console. the autocomplete will pop up all the available methods
     on the list.

     For help on a specific function like pop enter help([].pop) in console
    """
    fruits = []
    fruits.append("orange")

    assert __ == fruits

    fruits.insert(0, "banana")
    assert __ == fruits

    fruits.extend(["litchi", "guava"])
    assert __ == fruits

    fruits.reverse()
    assert __ == fruits

    fruits.pop()
    assert __ == fruits

    fruits.pop(0)
    assert __ == fruits

def test_list_can_contain_lists():
    fruits = ["orange", "banana"]
    veggies = ["beetroot", "tomato"]
    all = [fruits, veggies]

    assert __ == len(all)
    assert [__] == all[0]
    assert [__] == all[1]

def test_list_can_contain_objects_of_different_types():
    # note that this is rarely done in practice!
    mixed = ["string", 10]
    assert __ == mixed[0]
    assert __ == mixed[1]

def test_list_sort():
    numbers = [ 5, 4, 3, 8 ]
    numbers.sort()
    assert [__] == numbers
    numbers.sort(reverse=True)
    assert [__] == numbers

# if something unexpected happens see,
# https://docs.python.org/3/reference/expressions.html#comparisons
# and fix accordingly.
def test_list_membership():
    numbers = [ 5, 4, 3]
    assert __ == 5 in numbers
    assert __ == 10 in numbers


# you will understand how this works in later lessons (the next 2 tests).
# for now understand the behavior.
def test_list_range():
    # range objects can be used to generate lists of numbers of all kinds
    # note that you need to pass a range object to list constructor to create the
    # the list.
    # print (range.__doc__)
    numbers = list(range(1,5))
    assert [__] == numbers

    numbers = list(range(1, 5, 2))
    assert [__] == numbers


def test_list_from_string():
    # you can create lists from other sequences like objects like strings.
    result = list("hello")
    assert [__] == result


#Now apply what you have learnt. Type  help(range) in console or read online docs
def odd_desc(count):
    """
    Replace ___ with a single call to range to return a list of descending odd numbers ending with 1
    For e.g if count = 2, return a list of 2 odds [3,1]. See the test below if it is not clear
    """
    return ___

def test_odd_desc():
    assert [] == odd_desc(0)
    assert [1] == odd_desc(1)
    assert [7,5,3,1] == odd_desc(4)
    assert [11,9,7,5,3,1] == odd_desc(6)


three_things_i_learnt = """
-
-
-
"""
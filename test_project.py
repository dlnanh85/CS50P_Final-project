from project import *


def test_visualizer__str__():
    input = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    expected = \
'''1\t #
2\t ##
3\t ###
4\t ####
5\t #####'''
    assert visualizer__str__(input) == expected

    input = [(0, 0), (1, 1), (2, 2)]
    expected = \
'''0\t 
1\t #
2\t ##'''
    assert visualizer__str__(input) == expected

    input = []
    expected = \
''''''
    assert visualizer__str__(input) == expected

    input = [(22222222, 2), (11111111, 1)]
    expected = \
'''22222222\t\t ##
11111111\t\t #'''
    assert visualizer__str__(input) == expected

    input = [(4, 1), (16, 4), (32, 8)]
    expected = \
'''4\t #
16\t ####
32\t ########'''
    assert visualizer__str__(input) == expected


def test_scale():
    input = [1, 2, 3] 
    expected = [(1, 1), (2, 2), (3, 3)]
    assert scale(input) == expected


    input = [2, 4, 6, 8]
    expected = [(2, 1), (4, 2), (6, 3), (8, 4)]
    assert scale(input) == expected


    input = [0, 5, 10]
    expected =[(0, 0), (5, 1), (10, 2)]
    assert scale(input) == expected


def test_get_common_div():
    input = [0, 5, 10]
    expected = [1, 5]
    assert get_common_div(input) == expected

    input = [0, 1, 2, 3, 4]
    expected = [1]
    assert get_common_div(input) == expected

    input = [2, 10, 100, 2000]
    expected = [1, 2]
    assert get_common_div(input) == expected

    input = [7, 11, 31]
    expected = [1]
    assert get_common_div(input) == expected
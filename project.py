import argparse
import os
import sys
import random
from sort_visualize import *

if __name__ == '__main__':
    TERMINAL_SIZE = os.get_terminal_size()
else:
    # Sample for testing
    TERMINAL_SIZE = os.terminal_size([1000, 1000])

TAB_SIZE = 8
SEPARATOR = 1
IS_RANDOM = False
MIN_HEIGHT = 5


def main():
    args = handle_args()

    # Get list
    ls = gen_random_list() if IS_RANDOM else get_list()

    sort_obj = SortVisualizer(scale(ls), args.delay)
    
    print(visualizer__str__(sort_obj.ls))
    
    if args.algorithm == 'bubble':
        sort_obj.bubble_sort()
    elif args.algorithm == 'selection':
        sort_obj.selection_sort()
    elif args.algorithm == 'insertion':
        sort_obj.insertion_sort()


def handle_args():
    '''
    Handle the command line arguments

    :return: A dict of arguments
    :rtype: dict
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--algorithm', choices=['bubble', 'selection', 'insertion'], help='select the sorting algorithm', required=True)
    parser.add_argument('-d', '--delay', help='the time interval between steps (in seconds)', type=float, default=0.25)
    parser.add_argument('-r', '--random', help='generate random list', action='store_true')
    result =  parser.parse_args()
    
    global IS_RANDOM
    IS_RANDOM = result.random
    
    return result


# TEST
def visualizer__str__(ls: list):
    '''
    Generate a complete string to represent the first view of visualizer
    
    :param ls: a dict consist of original and scaled list
    :type ls: dict
    :return: a complete string to print out the first view of visualizer
    :rtype: str
    '''

    lines = ''
    
    # Clear screen ('if' to avoid clearing screen while testing)
    if __name__ == '__main__':
        os.system('cls' if os.name == 'nt' else 'clear')
    
    for element in ls:
        
        line = f'{element[0]}'\
            + ((int(len(str(max([ele[0] for ele in ls]))) / TAB_SIZE) + 1) * '\t')\
            + (' ' * SEPARATOR) + ('#' * element[1])\
            + '\n' 
            
        lines += line
        
    return lines.rstrip()


# TEST
def scale(original: list):
    '''
    Scale the list to fit the terminal window
    
    :param orignal: the list need to be scaled
    :type orignal: list[int]
    :return: a list consist of pair of original value and scaled value (tuple)
    :rtype: list
    '''
    scaled = []
    
    # Check height
    # Ignore if list is randomly generated
    check_height(len(original))

    # Check width
    # Ignore if list is randomly generated
    common_divs = get_common_div(original)
    for common_div in reversed(common_divs):
        scaled = list(map(lambda x: int(x / common_div), original))
        if check_width(original, scaled):
            break

    return [(original[i], scaled[i]) for i in range(len(original))]


# TEST
def get_common_div(ls: list):
    '''
    Return all common divisors of a list
    
    :param ls: a list of integer
    :type ls: list[int]
    :return: a list of common divisors
    :rtype: list[int]
    '''
    common_divs = [1]
    try:
        min_ele = min(filter(lambda x: x != 0, ls))
    except ValueError:
        return common_divs

    for i in range(2, min_ele + 1):
        for element in ls:
            if element % i != 0:
                break
        else:
            common_divs.append(i)

    return common_divs


def check_height(length: int):
    '''
    Check if the height of terminal window is fit for the visualizer
    
    :param length: the number of element in user's list
    :type length: int
    '''
    height = TERMINAL_SIZE.lines - 1
    while height < length:
        response = get_response(f'You need to make your terminal window higher! (about {length - height} more lines)')
        if response == 0:
            break
        elif response == 1:
            height = os.get_terminal_size().lines
        elif response == 2:
            if not IS_RANDOM:
                print('The number of element in your list is too many. Please input a new list')
            else:
                print('The generated list cannot be visualized. Generating new list')
            main()
            sys.exit()


def check_width(original: list, scaled: list):
    '''
    Check if the width of terminal window is fit for the visualizer
    
    :param original: the user's original list
    :type original: list[int]
    :param scaled: the user's scaled list (need to be checked)
    :type scaled: list[int]
    :return: whether the width if appropriate
    :rtype: bool
    '''
    width = TERMINAL_SIZE.columns
    max_scaled = max(scaled)
    max_original = max(original)

    # width_needed = tabs needed to cover original_max + width need for the scaled + SERPARATOR
    width_needed =  (int(len(str(max_original)) / TAB_SIZE) + 1) * TAB_SIZE + max_scaled + SEPARATOR
    
    while width < width_needed:
        response = get_response(f'You need to make your terminal window wider! (about {width_needed - width} more columns)')
        if response == 0:
            break
        elif response == 1:
            width = os.get_terminal_size().columns
        elif response == 2:
            if not IS_RANDOM:
                print('Cannot find the appropriate scale for the inputted list. Please input a new list')
            else:
                print('The generated list cannot be visualized. Generating new list')
            main()
            sys.exit()
            
    return True


def get_list():
    '''
    Get a list of integer from user
    
    :return: a list from user's input
    :rtype: list[int]
    '''
    print('Please enter a list of integer. Example: 1,2,3,4')
    
    user = []
    while True:
        try:
            user = [int(s.strip()) for s in input('List: ').split(',')]
            break
        except ValueError:
            print('Invalid input, try again.')
    
    return user


def gen_random_list():
    ls = []
    global TERMINAL_SIZE
    
    while MIN_HEIGHT > (TERMINAL_SIZE.lines - 1):
        response = get_response(f'You need to make your terminal window wider! (about {MIN_HEIGHT - TERMINAL_SIZE.lines} more columns)')
        if response == 0:
            height = MIN_HEIGHT
            break
        elif response == 1:
            TERMINAL_SIZE = os.get_terminal_size()
        elif response == 2:
            sys.exit('This program is not appropriate to run on your device')
    else:
        height = random.choice(range(MIN_HEIGHT, TERMINAL_SIZE.lines - 1))
    
    for _ in range(height):
        ls.append(random.randint(1, 100))
    
    return ls


def get_response(s: str):
    '''
    Get response from user when the terminal size is not appropriate
    '''
    print(s)
    print('Choose one of the response:')
    print('0: Ignore (not recommended)')
    print('1: Resize terminal (resize your terminal then type in 1)')
    print('2: Cannot resize anymore')
    return int(input())


if __name__ == '__main__':
    main()
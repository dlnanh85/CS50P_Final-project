# SORTING ALGORITHMS VISUALIZER (CLI based)
### Description: This project allow the user to see the visualization of sorting algorithms, with the ability to generate random or custom inputs
## Video Demo:  <URL HERE>

## Dependencies
Only `argparse` is required for this project to operate

## Usage
`project.py [-h] -a {bubble,selection,insertion} [-d DELAY] [-r]`

#### Options:

* `-h, --help`: show this help message and exit

* `-a {bubble,selection,insertion}, --algorithm {bubble,selection,insertion}`: select the sorting algorithm

* `-d DELAY, --delay DELAY`: the time interval between steps (in seconds)
                    
* `-r, --random`: generate random list

## File structure
* project.py
* sort_visualize.py
* test_project.py

### project.py
Consist of 9 helping functions

#### `handle_args()`
This function handles command line arguments using `argparse` library. 

#### `visualizer__str__(ls)`
Takes in `ls` as list of tuples of **user's input** (or generated randomly by the program) and the **scaled values**. This function will process each element of the list and generate line by line, then concatenate these lines as a big string for return.

#### `scale(original)`
Returns a list of tuples of **user's input** `original` and its **scaled values**

#### `get_common_div(ls)`
Returns a list of common divisors of the element of `ls`

#### `check_height(length)`
Checks if the `length` of the list would fit the **terminal's height**

#### `check_width(original, scaled)`
Checks if the visualization would fit the **terminal's width**

#### `get_list()`
This function asks and returns the list from user's input

#### `get_random_list()`
Returns a randomly generated list (this list must fit the terminal's size)

#### `get_response()`
When the size of the terminal is too small to show the visualizer, the user is asked what they want:
- *Ignore*
- *Resize the terminal*
- If *cannot resize anymore*, the user is asked to provide a new list. When the list is **randomly generated**, the program will only ask the user to resize the terminal window when its size is too small (smaller than the hard-coded minimum range in the `get_random_list()`)


In my opinion, these helping functions can be part of a class (maybe called ListVisualizer) to handle showing the list and its visualization to the user. However, for the context of CS50P's Final project and for testing purpose. These functions are implemented as standalones.

### sort_visualize.py

#### `class SortVisualizer`
This class consists of 2 properties: The list `ls` consists of tuples of user's input and its visualization, and `delay` is the amount of time each step takes so that the visualization is observable.

**Methods:**
##### `SortVisualizer.bubble_sort(self)`
##### `SortVisulizer.insertion_sort(self)`
##### `SortVisulizer.selection_sort(self)`
These methods are implementation of simple sorting algorithms. These are just simple algorithms that are easy to visualize (it's not that easy, it's just easier than the others). While implementing the normal sort functionality, these methods also use other methods to manipulate the output of terminal (like coloring, swapping), with the support of `class TerminalCursor` to move the terminal's cursor around the window.

##### `SortVisualizer.swap(self, pos1, pos2, color1=TEXT_GREEN, color2=TEXT_GREEN)`
This function swaps the element at `pos1` and `pos2` in `self.ls`, while highlighting the swapping lines.

##### `SortVisualizer.highlight(self, pos, color=TEXT_GREEN, unlight=False)`
This function highlight with `color` the printed line at `pos` index (from top to bottom). `unlight=True` will reset the color of the line.


#### `class TerminalCursor`
This class includes the following methods: `move_up()`, `move_down`, `del_line()`. These methods manipulate the cursor of the terminal window and the outputed text.
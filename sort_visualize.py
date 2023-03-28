from project import *
import time

TEXT_GREEN = '\033[92m'
TEXT_RED = '\u001b[31m'
TEXT_RESET = '\033[0m'


class SortVisualizer:
    def __init__(self, ls: list, delay: float):
        self.ls = ls
        self.delay = delay
        
    def bubble_sort(self):
        size = len(self.ls)
        for i in range(size):
            for j in range(size - 1 - i):
                if self.ls[j][0] > self.ls[j + 1][0]:
                    self.swap(j, j + 1)

    def selection_sort(self):
        size = len(self.ls)
        for i in range(size):

            self.highlight(i, color=TEXT_RED)

            min = self.ls[i][0]
            min_index = i
            for j in range(i + 1, size):
                time.sleep(self.delay)
                self.highlight(j)

                if min > self.ls[j][0]:
                    self.highlight(min_index, unlight=True)

                    min = self.ls[j][0]
                    min_index = j

                    self.highlight(min_index, color=TEXT_RED)
                else:
                    self.highlight(j, unlight=True)
            
            if min_index != i:
                self.swap(min_index, i, color1=TEXT_RED, color2=TEXT_GREEN)
            self.highlight(i, unlight=True)
         
    def insertion_sort(self):
        size = len(self.ls)

        for i in range(size):
            old_j = i
            self.highlight(i, color=TEXT_RED)
            for j in reversed(range(0, i)):
                if self.ls[j][0] > self.ls[j + 1][0]:
                    self.swap(j, j + 1, color2=TEXT_RED)
                    self.highlight(j, color=TEXT_RED)
                    self.highlight(j + 1)
                    old_j = j
            time.sleep(self.delay)
            self.highlight(old_j)

    def swap(self, pos1, pos2, color1=TEXT_GREEN, color2=TEXT_GREEN):
        self.highlight(pos1, color1)
        self.highlight(pos2, color2)
        self.ls[pos1], self.ls[pos2] = self.ls[pos2], self.ls[pos1]
        time.sleep(self.delay)
        self.highlight(pos1, color2)
        self.highlight(pos2, color1)
        time.sleep(self.delay)
        self.highlight(pos1, unlight=True)
        self.highlight(pos2, unlight=True)
        
    def highlight(self, pos, color=TEXT_GREEN, unlight=False):
        size = len(self.ls)
        
        TerminalCursor.move_up(size - pos)
        # print("HELLO")
        TerminalCursor.del_line()
        line = (color if not unlight else TEXT_RESET)\
            + f'{self.ls[pos][0]}'\
            + ((int(len(str(max([ele[0] for ele in self.ls]))) / TAB_SIZE) + 1) * '\t')\
            + (' ' * SEPARATOR) + ('#' * self.ls[pos][1])\
            + TEXT_RESET
        print(line)
        TerminalCursor.move_down(size - pos - 1)
    
    
class TerminalCursor:
    @staticmethod
    def move_up(n: int):
        if n > 0: print(f'\033[{n}A', end='')
        
    @staticmethod
    def move_down(n: int):
        if n > 0: print(f'\033[{n}B', end='')
        
    @staticmethod
    def del_line():
        print('\x1b[2K', end='')
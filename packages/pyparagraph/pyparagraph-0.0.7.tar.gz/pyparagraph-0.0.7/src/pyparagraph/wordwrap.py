#!/usr/bin/env python3
from collections import namedtuple
from copy import copy
from itertools import takewhile
import logging
import os

from PIL import ImageFont, Image, ImageDraw

from .linebreak import HBox, Penalty, Infinity, Glue
from .linked_list import LinkedList, Node

LineWidth = namedtuple("LineWidth", ["max", "ideal", "offset" ])
class Breakpoint:
    def __init__(self, position, demerits, ratio, line, fitness_class, totals, previous):
        self.position = position
        self.demerits = demerits
        self.ratio = ratio
        self.line = line
        self.fitness_class = fitness_class
        self.totals = totals
        self.previous = previous
    def __repr__(self):
        return f"Breakpoint(position={repr(self.position)}, demerits={repr(self.demerits)}, ratio={repr(self.ratio)}, line={repr(self.line)})"

def new_breakpoint(position, fitness_class, totals, candidate):
    previous = candidate.active if candidate else None
    demerits = candidate.demerits if candidate else 0
    ratio = candidate.ratio if candidate else 0
    totals = totals or Glue(0,0,0)
    line = (previous.data.line + 1) if previous else 0
    return Breakpoint(position, demerits, ratio, line, fitness_class, totals, previous)

Break = namedtuple("Break", ["position", "ratio"])
Candidate = namedtuple("Candidate", ["active", "demerits", "ratio"])
LineData = namedtuple("LineData", ["ratio", "nodes"])
def is_newline(n):
    return isinstance(n, Penalty) and (n.penalty <= -Infinity)

class WrapInfo:
    def __init__(self, font, line_max=80, line_ideal=None, line_widths=None):
        self.line_max = line_max
        if line_ideal is None:
            line_ideal = line_max
        self.line_ideal = line_ideal
        self.line_widths = line_widths
        self.demerits = namedtuple("Demerits", ["line", "flagged", "fitness"])(10,100,300)
        self.tolerance = 2
        self.font = font

    def calc_line_length(self, i):
        i = i - 1 + self._lines_processed # i is 1-based
        if self.line_widths and len(self.line_widths)>i:
            return LineWidth(max=self.line_widths[i][0], ideal = self.line_widths[i][0], offset=self.line_widths[i].offset)
        return LineWidth(max=self.line_max, ideal=self.line_ideal, offset=0)

class KnuthPlassWrap(WrapInfo):
    def linebreak(self, nodes, lines):
        self.activeNodes = LinkedList()
        self.sum_ = Glue(0,0,0)
        self.nodes = nodes
        breaks = []

        tmp = Node(Candidate(0, Infinity, 0))

        def compute_ratio(node, active, current_line):
            width = self.sum_.width - active.totals.width
            line_length = self.calc_line_length(current_line).ideal

            if isinstance(node, Penalty):
                width += node.width

            def diff_or_infinity(self_val, active_val):
                difference = self_val - active_val
                if difference <= 0:
                    return Infinity
                return (line_length - width) / difference

            if width < line_length:
                return diff_or_infinity(self.sum_.stretch, active.totals.stretch)
            elif width == line_length:
                return 0
            else:
                return diff_or_infinity(self.sum_.shrink, active.totals.shrink)

        def compute_sum(nodes):
            # We're only totalling up until the first HBox or first IP that isn't element 0
            def not_ends_list(node):
                return not (isinstance(node, HBox) or (node is not nodes[0] and is_newline(node)))

            # Add all the Glue nodes in that range to our base result
            return sum((node for node in takewhile(not_ends_list, nodes) if isinstance(node, Glue)), 
                         copy(self.sum_))

        def mainLoop(node, index, nodes, wobble=False):
            active = self.activeNodes[0] if self.activeNodes else None

            while active is not None:
                candidates = [ Candidate(None, Infinity, None)] * 4

                while active:
                    current_line = active.data.line+1
                    ratio = compute_ratio(nodes[index] if index<len(nodes) else None, active.data, current_line)

                    if ratio < -1 or is_newline(node):
                        self.activeNodes.remove(active)

                    if -1 <= ratio and ratio <= self.tolerance:
                        badness = 100 * (abs(ratio)**3)

                        demerits = (self.demerits.line + badness)**2
                        if isinstance(node, Penalty) and node.penalty >= 0:
                            demerits += node.penalty**2
                        elif isinstance(node, Penalty) and node.penalty > -Infinity:
                            demerits -= node.penalty**2

                        # Try to avoid having 2 flagged lines in a row (flagging usually means
                        # hyphenated)
                        if isinstance(node, Penalty) and len(nodes)>active.data.position and isinstance(nodes[active.data.position], Penalty):
                            demerits += self.demerits.flagged * node.flagged * nodes[active.data.position].flagged

                        class_cutoffs = { 0:-.5, 1:.5, 2:1, 3:Infinity+ratio}
                        current_class = min( k for k in class_cutoffs if ratio < class_cutoffs[k])

                        if abs(current_class - active.data.fitness_class) > 1:
                            demerits += self.demerits.fitness

                        demerits += active.data.demerits
                        
                        if demerits < candidates[current_class].demerits:
                            candidates[current_class] = Candidate(active, demerits, ratio)

                    active = active.next

                    if active is not None and active.data.line >= current_line:
                        break

                current_sum = compute_sum(self.nodes[index:])

                for fitness_class, candidate in enumerate(candidates):
                    if candidate.demerits < Infinity:
                        new_node = Node(new_breakpoint(index, fitness_class, current_sum, candidate))
                        if active is not None:
                            self.activeNodes.insertBefore(active, new_node)
                        else:
                            self.activeNodes.append(new_node)

        self.activeNodes.append(Node(new_breakpoint(0,0,None,None)))

        last = None

        for i, node in enumerate(self.nodes):
            if isinstance(node, HBox):
                self.sum_.width += node.width
            elif isinstance(node, Glue):
                if isinstance(last, HBox):
                    mainLoop(node, i, self.nodes, wobble=True)
                self.sum_.width += node.width
                self.sum_.stretch += node.stretch
                self.sum_.shrink += node.shrink
            elif isinstance(node, Penalty) and node.penalty < Infinity:
                mainLoop(node, i, self.nodes)
            last = node
        
        if self.activeNodes:
            tmp = min(self.activeNodes)

            while tmp is not None:
                breaks.append( Break(tmp.data.position, tmp.data.ratio))
                tmp = tmp.data.previous

            breaks.reverse()
            return breaks
        return []

    def wrap_nodes(self, nodes, lines_processed=0):
        self._lines_processed = lines_processed
        for tolerance in (1,2,3):
            logging.debug("Attempting to find fit with tolerance %d", tolerance)
            self.tolerance=tolerance
            nodes = copy(nodes)
            my_breaks = self.linebreak(nodes, None)
            if my_breaks:
                break
        else:
            logging.error("Cannot find a Knuth-Plass wrap, falling back to Greedy wrapping")
            wrapper = GreedyWrap(**self.args)
            return wrapper.wrap_nodes(nodes)

        lines = []
        line_start = 0
        for b in my_breaks[1:]:
            point = b.position
            r = b.ratio
            for j, n in enumerate(nodes[line_start:]):
                if isinstance(n, HBox) or is_newline(n):
                    line_start += j
                    break
            need_hyphen=False
            if isinstance(nodes[point], Penalty) and nodes[point].flagged and nodes[point].penalty > -Infinity:
                need_hyphen = True
                for n in nodes[point-1:line_start:-1]:
                    if isinstance(n, HBox):
                        need_hyphen = n.value[-1].isalpha()
                        which_font = n.font
                        break
            need_hyphen=[HBox(self.font.hyphen, which_font)] if need_hyphen else []
            lines.append(LineData(r, nodes[line_start:point+1]+need_hyphen))
            line_start = point

        return lines
    def wrap_nodes_to_lines(self, nodes, lines_processed = 0):
        self._lines_processed = lines_processed
        lines = self.wrap_nodes(nodes)

        text_lines = []
        for line in lines:
            text_lines.append([])
            indent = False
            spaces=0
            totalAdjustment = 0
            wordSpace = 10 #FIXME
            for node in line.nodes:
                if isinstance(node, HBox):
                    text_lines[-1].append(node.value)
                elif isinstance(node, Glue):
                    text_lines[-1].append(" "*(1 if node.width else 0))
        text_lines = [ "".join(t) for t in text_lines ]
        return text_lines

class GreedyWrap(WrapInfo):
    def wrap_nodes(self, nodes):
        lines = [[]]
        am_hyphenating = False
        for node in nodes:
            # No penalties in greedy wrapping
            if not isinstance(node, (Glue, HBox)):
                if node.width:
                    am_hyphenating = True
                continue
            if not lines[-1]:
                lines[-1].append(node)
            else:
                line_len = sum(node.width for node in lines[-1])
                if line_len + node.width < self.calc_line_length(len(lines)-1).ideal:
                    lines[-1].append(node)
                else:
                    if am_hyphenating:
                        if lines[-1] and isinstance(lines[-1][-1], HBox) and lines[-1][-1].value[-1].isalpha():
                            lines[-1].append(HBox(self.font.hyphen, self.font.font))
                    if isinstance(node, Glue):
                        lines.append([])
                    else:
                        lines.append([node])
                am_hyphenating = False
        return [LineData(1, line) for line in lines]

    def wrap_nodes_to_lines(self, nodes):
        lines = self.wrap_nodes(nodes)
        for i, line in enumerate(lines):
            lines[i] = "".join( v.value if isinstance(v, HBox) else " "*(1 if v.width else 0) for v in line.nodes)
        return lines

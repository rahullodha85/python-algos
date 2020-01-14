from enum import Enum


class Graph:
    def __init__(self):
        self.nodes = []


class Node:

    def __init__(self, d):
        self.data = d
        self.children = []
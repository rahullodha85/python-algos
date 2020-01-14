from rl.ctci.graph.Graph import Graph
from rl.ctci.graph.Graph import Node


class Solution:

    def search(self, g: Graph, start: Node, end: Node):

        q = []
        q.append(start)

        while len(q) > 0:
            current = q.pop(0)
            if current:
                for child in current.children:

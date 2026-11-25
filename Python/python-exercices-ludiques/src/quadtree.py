from __future__ import annotations
import ast

class QuadTree:
    NB_NODES : int = 4
    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree,bg: bool | QuadTree):
        self.hg = hg
        self.hd = hd
        self.bd = bd
        self.bg = bg

    @property
    def depth(self) -> int:
        """ Recursion depth of the quadtree"""
        return 1 + max(self.hg.depth if isinstance(self.hg, QuadTree) else 0,
                       self.hd.depth if isinstance(self.hd, QuadTree) else 0,
                       self.bd.depth if isinstance(self.bd, QuadTree) else 0,
                       self.bg.depth if isinstance(self.bg, QuadTree) else 0)
    

    @staticmethod
    def fromFile(filename: str) -> QuadTree:
        """ Open a given file, containing a textual representation of a list"""
        with open(filename, "r") as f:
            data = ast.literal_eval(f.read())
        return QuadTree.fromList(data)

    @staticmethod
    def fromList(data: list) -> QuadTree:
        """Generates a Quadtree from a list representation"""
        nodes = [
            QuadTree.fromList(node) if isinstance(node, list) else bool(node)
            for node in data
        ]
        return QuadTree(*nodes)

class TkQuadTree(QuadTree):
    def paint(self):
        """ TK representation of a Quadtree"""
        pass
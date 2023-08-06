#!/usr/local/bin/python3

import sys

class Graph():
    def __init__(self, infile):
        with open(infile) as f:
            self.V = int(f.readline())
            self.E = int(f.readline())
            self.G = [[] for i in range(self.V)]
            for i in range(self.E):
                From, To = f.readline().split()
                self.add_edge(int(From), int(To))
        f.close()


    def add_edge(self, v, w):
        assert v < self.V
        assert w < self.V
        self.G[v].append(w)
        self.G[w].append(v)
        pass


    def adj(self, v):
        assert v < self.V
        return self.G[v]


    def to_string(self):
        s = f'G: {self.V} vertices, {self.E} edges'
        return s

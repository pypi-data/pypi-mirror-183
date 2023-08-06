#!/usr/local/bin/python3

import sys
import graphviz

class Draw:
    def __init__(self):
        self.g = graphviz.Graph()
        self.g.engine = 'neato'
        self.g.attr('node', margin='0', fontsize='4',
                    fontcolor='white', color='black', shape='circle',
                    style='filled', width='0.1')
        self.g.attr('edge', color='grey', penwidth='0.75')


    def node_attr(self, **kwargs):
        self.g.attr('node', **kwargs)


    def edge_attr(self, **kwargs):
        self.g.attr('edge', **kwargs)


    def toPNG(self, Graph, path=[]):
        for v in range(Graph.V):
            self.g.node(str(v))

        pset = set()
        if len(path) >= 2:
            for i in range(len(path) - 1):
                pset.add((path[i], path[i+1]))
                pset.add((path[i+1], path[i]))

        seen = set()
        for v, e in enumerate(Graph.G):
            for w in e:
                if not (w, v) in seen:
                    if (w,v) in pset:
                        self.g.edge(str(v), str(w), color='black', penwidth='2.5')
                    else:
                        self.g.edge(str(v), str(w))
                    seen.add((v,w))

        self.g.view()

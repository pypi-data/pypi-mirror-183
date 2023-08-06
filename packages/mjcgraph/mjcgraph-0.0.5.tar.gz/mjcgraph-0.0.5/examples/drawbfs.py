#!/usr/local/bin/python3

import sys
from mjcgraph import graph
from mjcgraph import bfs
from mjcgraph import draw

infile = "../data/mediumG.txt"

G = graph.Graph(infile)
print(G.to_string())

bfs = bfs.BFSearch(G, 0)

bfpath = bfs.path_to(200)

fig = draw.Draw()
fig.toPNG(G, bfpath)

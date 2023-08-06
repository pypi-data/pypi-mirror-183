#!/usr/local/bin/python3

import sys
from mjcgraph import graph
from mjcgraph import draw

infile = "../data/tinyG.txt"

G = graph.Graph(infile)
print(G.to_string())

fig = draw.Draw()
fig.set_names(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'])
fig.node_attr(style='', fontcolor='black', fontsize='10')
fig.draw(G)

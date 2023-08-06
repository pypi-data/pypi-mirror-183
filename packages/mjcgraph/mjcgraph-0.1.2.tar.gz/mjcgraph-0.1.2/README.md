[![PyPI version](https://badge.fury.io/py/mjcgraph.svg)](https://badge.fury.io/py/mjcgraph)

# pygraph
A collection of graph algorithms and visualisations.

## Graph
The basic Graph object. Contains a list of nodes and edges.

Graphs can be populated manually or loaded from text files. The file format consists of two lines specifying the number (V) of vertices and (E) of edges followed by E pairs of connected vertices. For example:

    250
    1273
    244 246
    239 240
    238 245
    235 238
    233 240
    232 248
    231 248
    229 249
    228 241
    226 231
    223 242
    ...
    0 202
    0 204
    0 209
    0 211
    0 222
    0 225

## Draw
Draws the graph and a given path on it using Graphviz with neato layout. For example, the code

    G = graph.Graph('mediumG.txt')
    fig = draw.Draw()
    fig.draw(G)

will produce a figure looking similar to this:

![](https://raw.githubusercontent.com/mortenjc/pygraph/main/doc/graph.png)

### Graphviz keywords
The default values of node and adge attributes have been chosen to make
graphs render like in the text book 'Algorithms' by Robert Sedgewick.

You can customise the Graphviz attributes for nodes and edges, though:

    fig = draw.Draw()
    fig.node_attr(color='red')
    fig.edge_attr(penwidth='0.75')


## BFSearch
Breadth first search will find one of possibly multiple shortest paths.

    G = graph.Graph('mediumG.txt')
    bfs = bfs.BFSearch(G, 0)   # find paths from vertex 0
    bfpath = bfs.path_to(200)  # return path from vertex 0 to 200
    fig = draw.Draw()
    fig.draw(G, bfpath)

![](https://raw.githubusercontent.com/mortenjc/pygraph/main/doc/short.png)

## DFSearch
Depth first search will find one of possibly multiple paths of the graph. These
are not guaranteed to be longest, but they will typically be longer than the
paths found by breadth first search.

    G = graph.Graph('mediumG.txt')
    dfs = dfs.DFSearch(G, 0)
    dfpath = dfs.path_to(200)
    fig = draw.Draw()
    fig.draw(G, dfpath)

![](https://raw.githubusercontent.com/mortenjc/pygraph/main/doc/long.png)

## SymbolGraph
The symbol graph reads pairs of edge names and generates a Graph and a symbol table
mapping vertice indices to names.

    G = symbolgraph.SymbolGraph( "routes.txt")

    fig = draw.Draw()
    fig.set_names(G.keys)
    fig.node_attr(width='0.3', height='0.3', shape='circle', style='filled',
                  color='gray', fontcolor='black', fontsize='8')
    fig.draw(G.graph())

![](https://raw.githubusercontent.com/mortenjc/pygraph/main/doc/symbolg.png)

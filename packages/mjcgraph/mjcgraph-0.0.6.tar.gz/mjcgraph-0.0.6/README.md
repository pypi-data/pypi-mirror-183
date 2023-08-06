# pygraph
Learning graph algorithms. Inspired by the numerous
breadth first search problems in advent of code reminding
me of the Algorithms course I took way back then.

## Graph
The basic Graph object. Contains a list of nodes and edges.

Graphs can be loaded from ascii files, the format currently consist of two lines specifying the number (V) of vertices and (E) of edges followed by E pairs of connected vertices. For example:

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
Draws the graph and a given path on it using graphviz with neato layout. For example, the code

    G = graph.Graph('mediumG.txt')
    fig = draw.Draw()
    fig.toPNG(G, [])

will produce a figure looking similar to this:

![](https://raw.githubusercontent.com/mortenjc/pygraph/main/doc/graph.png)

## BFSearch
Breadth first search will find one of possibly multiple shortest paths.

    G = graph.Graph('mediumG.txt')
    bfs = bfs.BFSearch(G, 0)   # find paths from vertex 0
    bfpath = bfs.path_to(200)  # return path from vertex 0 to 200
    fig = draw.Draw()
    fig.toPNG(G, bfpath)

![](https://raw.githubusercontent.com/mortenjc/pygraph/main/doc/short.png)

## DFSearch
Depth first search will find one of possibly multiple paths of the graph. These
are not guaranteed to be longest, but they will typically be longer than the
paths found by breadth first search.

    G = graph.Graph('mediumG.txt')
    dfs = dfs.DFSearch(G, 0)
    dfpath = dfs.path_to(200)
    fig = draw.Draw()
    fig.toPNG(G, dfpath)

![](https://raw.githubusercontent.com/mortenjc/pygraph/main/doc/longest.png)

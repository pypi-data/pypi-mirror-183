Classes
=======

Graph
-----

.. py:class:: Graph(init)

   Creates a Graph object

   :param init: if integer (V) initialize empty Graph with V vertices. If string (filename) load and populate from file.


  .. py:method:: add_edge(v, w)

    Connects vertices v and w, both must be smaller than V

    :param v: vertice id
    :param w: vertice id


  .. py:method:: adj(v)

     Return a list of vertices adjacent to v

     :param v: vertice id
     :rtype: array of vertice ids


  .. py:method:: to_string()

    Cfreate a string representation of the Graph

    :rtype: graph string



SymbolGraph
-----------
Support Graph objects with named edges.

.. py:class:: SymbolGraph(filename)

   :param filename: file to read


  .. py:method:: graph()

    :rtype: Graph object


BFSearch
--------

DFSearch
--------

# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-13 19:41:32
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-14 22:13:48

# Given a directed graph, design an algorithm to
# find out whether there is a route between nodes

# http://stackoverflow.com/questions/19472530/representing-graphs-data-structure-in-python

graph: 
    adj list:
    a -> [(c,2),(d,5),(e,8)]
    b -> [(d,2)]
    c -> [(a,1), (b,5)]
    d -> [(c,2),(e,8)]
    e -> []
# from collections import defaultdict
# from pprint import pprint

# class Graph(object):
#     """ Graph data structure, undirected by default. """

#     def __init__(self, connections, directed=False):
#         self._graph = defaultdict(set)
#         self._directed = directed
#         self.add_connections(connections)

#     def add_connections(self, connections):
#         """ Add connections (list of tuple pairs) to graph """

#         for node1, node2 in connections:
#             self.add(node1, node2)

#     def add(self, node1, node2):
#         """ Add connection between node1 and node2 """

#         self._graph[node1].add(node2)
#         if not self._directed:
#             self._graph[node2].add(node1)

#     def remove(self, node):
#         """ Remove all references to node """

#         for n, cxns in self._graph.iteritems():
#             try:
#                 cxns.remove(node)
#             except KeyError:
#                 pass
#         try:
#             del self._graph[node]
#         except KeyError:
#             pass

#     def is_connected(self, node1, node2):
#         """ Is node1 directly connected to node2 """

#         return node1 in self._graph and node2 in self._graph[node1]

#     def find_path(self, node1, node2, path=[]):
#         """ Find any path between node1 and node2 (may not be shortest) """

#         path = path + [node1]
#         if node1 == node2:
#             return path
#         if node1 not in self._graph:
#             return None
#         for node in self._graph[node1]:
#             if node not in path:
#                 new_path = self.find_path(node, node2, path)
#                 if new_path:
#                     return new_path
#         return None

#     def __str__(self):
#         return '{}({})'.format(self.__class__.__name__, dict(self._graph))


# connections = [('A', 'B'), ('B', 'C'), ('B', 'D'),
#                    ('C', 'D'), ('E', 'F'), ('F', 'C')]
# g = Graph(connections, directed=True)
# pprint(g._graph)

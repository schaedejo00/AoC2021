
from D12.Graph import Graph

with open('example.txt', 'r', encoding="utf-8") as f:
#with open('input_1.txt', 'r', encoding="utf-8") as f:
    puzzleInput = f.read().split("\n")

graph: Graph = Graph()

for line in puzzleInput:
    start, end = line.split("-")
    graph.add_edge(start, end)

print(graph)


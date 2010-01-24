def add_node(g, node, level, color):
    try:
        int(node)
        shape = 'circle'
    except ValueError:
        shape = 'box'
    g.add_node(str(level)+'_'+node, label=str(node), shape=shape, color=color)

def add_edge(edges, from_node, to_node, level, value, color):
    edges.append( (str(level)+'_'+from_node,
        str(level+1)+'_'+to_node,
        {
            'label':str(value),
            'color':color,
            'fontcolor':color
            }
        ))

import json

json_net = json.load(open('table.json'))

import pygraphviz as pgv
graph = pgv.AGraph(directed=True)
edges = []

graph.graph_attr['rankdir'] = 'LR'
graph.node_attr['fontsize'] = '12'
graph.edge_attr['fontsize'] = '8'

for layer, level in zip(json_net, range(0, len(json_net))):
    for from_node, number in zip(sorted(layer), range(0, len(layer))):
        color = str(float(number)/len(layer)) + ', 0.8, 0.8'
        add_node(graph, from_node, level, color)
        #print layer[from_node]
        for to_node in layer[from_node]:
            add_edge(edges, from_node, to_node, level, layer[from_node][to_node], color)

#graph.add_edges_from(edge_graph.edges(keys=True))
for e in edges:
    graph.add_edge(e[0], e[1], **e[2])
graph.layout(prog='dot')
graph.draw('js.pdf')

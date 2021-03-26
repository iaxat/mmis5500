# HW 4
# Assignment
# MIS 5500

import requests
import json
from itertools import count, permutations,combinations

import networkx as nx
from networkx.classes.function import path_weight

import matplotlib.pyplot as plt

ids=["ripple","cardano","bitcoin-cash","eos","litecoin","ethereum","bitcoin"]
currencies=["xrp","ada","bch","eos","ltc","eth","btc"]

g = nx.DiGraph()
edges=[]

for i in range(len(ids)):
    for j in range(i+1,len(ids)):
        url = "https://api.coingecko.com/api/v3/simple/price?ids="+ids[i]+","+ids[j]+"&vs_currencies="+currencies[i]+","+currencies[j]+""
        req=requests.get(url)
        req_dict = json.loads(req.text)
        if(currencies[i]=='ada'):
            edges.append((currencies[i],currencies[j],float(req_dict[ids[i]][currencies[j]])))
        elif(currencies[j]=='ada'):
            pass
        else:
            edges.append((currencies[i], currencies[j],float(req_dict[ids[i]][currencies[j]])))
            edges.append((currencies[j], currencies[i],float(req_dict[ids[j]][currencies[i]])))
        j+=1
    i+=1

url = "https://api.coingecko.com/api/v3/simple/price?ids=cardano,ripple&vs_currencies=ada,xrp"
req=requests.get(url)
req_dict = json.loads(req.text)
edges.append(('ada','xrp',req_dict["cardano"]["xrp"]))

# print(edges)
g.add_weighted_edges_from(edges)

# # print all nodes
# print(g.nodes)

#for fun, you can save an image of your graph
pos = nx.circular_layout(g)  # pos = nx.nx_agraph.graphviz_layout(G)
nx.draw_networkx(g, pos)
labels = nx.get_edge_attributes(g, 'weight')
nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

plt.savefig("graph.png")


# print(g.nodes)
# input()
greatest_weight = -99999999
greatest_path = []
lowest_weight = 99999999
lowest_path = []
for n1, n2 in combinations(g.nodes, 2):
    print("paths from ", n1, "to", n2, "----------------------------------")
    for path in nx.all_simple_paths(g, source=n1, target=n2):
        # Update this code to multiply all the edges in the path and print
        # the factor
        path_weight_to = 1
        for i in range(len(path) - 1):
            # print("edge from",path[i],"to",path[i+1],": ",g[path[i]][path[i+1]]["weight"])
            path_weight_to *= g[path[i]][path[i + 1]]["weight"]

        print(path," : ",path_weight_to)

        path.reverse()

        path_weight_from = 1
        for i in range(len(path) - 1):
            path_weight_from *= g[path[i]][path[i + 1]]["weight"]

        print(path, " : ", path_weight_from)

        path_weight_factor = path_weight_to * path_weight_from

    if path_weight_factor > greatest_weight:
        greatest_weight = path_weight_factor
        greatest_path = path
    if path_weight_factor < lowest_weight:
        lowest_weight=path_weight_factor
        lowest_path=path

print("\n\ngreatest path weight factor : ",greatest_weight)
print("greatest path : ", greatest_path)
greatest_path.reverse()
print(greatest_path,"at weight: ", greatest_weight)

print("\n\nlowest path weight factor : ", lowest_weight)
print("lowest path : ", lowest_path)
lowest_path.reverse()
print(lowest_path, "at weight: ", lowest_weight)
print(0)

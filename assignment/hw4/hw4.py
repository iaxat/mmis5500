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
    for j in range(len(ids)) :
        if i!=j:
            url = "https://api.coingecko.com/api/v3/simple/price?ids="+ids[i]+","+ids[j]+"&vs_currencies="+currencies[i]+","+currencies[j]+""
            req_data=requests.get(url)
            currency_dict = json.loads(req_data.text)
            if(currencies[j]=='ada'):
                pass
            else:
                edges.append((currencies[i], currencies[j],float(currency_dict[ids[i]][currencies[j]])))
            j+=1
    i+=1

g.add_weighted_edges_from(edges)

# print(g.nodes)
# input()
greatest_weight = -99999999
greatest_path = []
lowest_weight = 99999999
lowest_path = []
for n1, n2 in combinations(g.nodes, 2):
    # print("paths from ", n1, "to", n2, "----------------------------------")
    for path in nx.all_simple_paths(g, source=n1, target=n2):
        # Update this code to multiply all the edges in the path and print
        # the factor
        path_weight_to = 1
        for i in range(len(path) - 1):
            # print("edge from",path[i],"to",path[i+1],": ",g[path[i]][path[i+1]]["weight"])
            path_weight_to *= g[path[i]][path[i + 1]]["weight"]

        # print(path," : ",path_weight_to)

        path.reverse()

        path_weight_from = 1
        for i in range(len(path) - 1):
            path_weight_from *= g[path[i]][path[i + 1]]["weight"]

        # print(path, " : ", path_weight_from)

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

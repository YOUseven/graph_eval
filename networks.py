import networkx as nx
import math

def network_scale(G, vis=True):
    """
    Count the scale of network
    :param G: networkx
    :param vis: look the result
    :return: the number of edges,
             the number of nodes,
             the density of G,
             the average of degrees,
             the number of isolated nodes
    """

    cnt_edges = len(G.edges)
    cnt_nodes = len(G.nodes)

    dens_G = nx.density(G)

    all_nodes_degree = dict(G.degree())
    avg_deg = round(sum(all_nodes_degree.values())/len(all_nodes_degree), 4)

    iso_nodes = [item for item in nx.isolates(G)]
    cnt_iso_nodes = len(iso_nodes)

    if vis:
        print("the number of edges: {}\nthe number of nodes: {}\nthe density of G: {}\nthe average of degrees: {:.4f}\nthe number of isolated nodes: {}\n"
              .format(cnt_edges, cnt_nodes, dens_G, avg_deg, cnt_iso_nodes))
    res = cnt_edges, cnt_nodes, dens_G, avg_deg, cnt_iso_nodes
    return res

def count_nodes_degree(G, vis=True):
    """
    Count the number of isolated\1-degree\greater than 1-degree nodes
    :param G: networkx
    :param vis: look the result
    :return: the number of isolated nodes,
             the number of 1-degree nodes,
             the number of greater than 1-degree nodes,
    """
    degree_0, degree_1, degree_big = [], [], []
    for node in G.nodes:
        d = G.degree(node)
        if d == 0:
            degree_0.append(node)
        elif d == 1:
            degree_1.append(node)
        else:
            degree_big.append(node)

    if vis:
        print('the number of isolated nodes: {}\nthe number of 1-degree nodes: {}\nthe number of greater than 1-degree nodes: {}'
              .format(len(degree_0), len(degree_1), len(degree_big)))

    res = degree_0, degree_1, degree_big
    return res

def renumber_network(x, key, G):
    """
    renumber the nodes of graph from zero to n-1
    :param x: dataframe, have the unique identification
              like 'xxx_id'
    :param key: str, the name of unique identification
    :param G: networkx, original graph
    :return: renumbered Graph ( from 0 to n-1 )
    """
    nodes_id = x[key].tolist()

    id2index = {}
    index = 0
    for node in nodes_id:
        if math.isnan(node):
            continue
        node = int(node)
        id2index[node] = index
        index += 1

    index_edges = []
    for edge in G.edges():
        if math.isnan(edge[0]) or math.isnan(edge[1]):
            continue
        tmp = (id2index[int(edge[0])], id2index[int(edge[1])])
        index_edges.append(tmp)

    G_index = nx.Graph()
    G_index.add_edges_from(index_edges)
    G_index.add_nodes_from(list(id2index.values()))

    return G_index
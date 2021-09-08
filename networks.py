import networkx as nx


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
    avg_deg = round(sum(all_nodes_degree.values())/len(all_nodes_degree))

    iso_nodes = [item for item in nx.isolates(G)]
    cnt_iso_nodes = len(iso_nodes)

    if vis:
        print("the number of edges: {}"+\
              "the number of nodes: {}"+\
              "the density of G: {}"+\
              "the average of degrees: {:.4f}"+\
              "the number of isolated nodes: {}".format(cnt_edges, cnt_nodes,
                                                        dens_G, avg_deg,
                                                        cnt_iso_nodes))
    res = cnt_edges, cnt_nodes, \
          dens_G, avg_deg, \
          cnt_iso_nodes
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
        d = graph.degree(node)
        if d == 0:
            degree_0.append(node)
        elif d == 1:
            degree_1.append(node)
        else:
            degree_big.append(node)

    if vis:
        print("the number of isolated nodes: {}" + \
              "the number of 1-degree nodes: {}" + \
              "the number of greater than 1-degree nodes: {}".format(degree_0, degree_1, degree_big))

    res = degree_0, degree_1, degree_big
    return res
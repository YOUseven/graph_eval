import networkx as nx

def df_to_graph(df, index=False):
    """
    According to the dataframe of network, building a Graph
    :param df: pandas.DataFrame, the source of data.
            source_id1, end_id1
            ...,...
            source_idn, end_idn
    :param index: renumber the nodes from 0
    :param vis: look the result
    :return: Graph, networkx
    TODO:find a faster way
    """
    G = nx.Graph()
    edges = []

    if index:
        id2index = {}
        index = 0
        nodes = list(set(df[:, 0].values.tolist() + df[:, 1].values.tolist()))
        for node in nodes:
            id2index[node] = index
            index += 1

    for i, row in df.iterrows():
        if index:
            src, end = id2index[row[0]], id2index[row[1]]
        else:
            src, end = row[0], row[1]
        edges.append((src, end))
    G.add_edges_from(edges)
    return G
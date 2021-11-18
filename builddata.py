import networkx as nx
import pandas as pd
import numpy as np
import torch
import math


def process_user(df_user, key):
    # 去重 去空
    df_user = df_user.dropna(how='all')
    df_user = df_user.drop_duplicates(key)
    df_user[key] = df_user[key].astype(int)
    return df_user

def process_network(df_user, df_friend, df_network, key):
    usr_node, frd_node = list(set(df_user[key].values.tolist())), list(set(df_friend[key].values.tolist()))
    node_list = list(set(usr_node+frd_node))
    G = nx.Graph()
    df_network = df_network.dropna(how='all')
    edges_list = []
    for index, row in df_network.iterrows():
        edge = (int(row[0]), int(row[1]))
        edges_list.append(edge)
    G.add_edges_from(edges_list)
    G.add_nodes_from(node_list)
    return G

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

def build_data(df_user, df_friend, df_network, key, feature_col, y_col, null_val):
    user_fea = process_user(df_user, key)
    friend_fea = process_user(df_friend, key)
    network = process_network(user_fea, friend_fea, df_network, key)

    # x
    friend_fea[y_col] = 2
    df_all_fea = pd.concat([user_fea, friend_fea])
    all_fea = process_user(df_all_fea, key)
    all_fea_x = all_fea.loc[:, feature_col]
    all_fea_x = all_fea_x.fillna(null_val)
    torch_x = torch.Tensor(np.array(all_fea_x))
    # y
    all_fea[y_col+'_inv'] = all_fea[y_col].apply(lambda x: 1-x if x>=0 else x)
    all_fea_y = all_fea[y_col+'_inv'].values.tolist()
    torch_y = torch.LongTensor(all_fea_y)
    # graph
    index_graph = renumber_network(all_fea, key, network)

    return torch_x, torch_y, index_graph

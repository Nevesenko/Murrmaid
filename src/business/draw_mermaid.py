import src.cleaning
import requests
##конфиги



def draw_nodes(df):
    res = []
    for item, name in zip(df['id'], df['properties.Name.title']):
        res.append(item + '(' + name + ')')
    return res

def draw_graph(df):
    res = [] #НУЖНО ИЗВЛЕКАТЬ ИМЕННО ID КОННЕКЕНОВ !!!
    for parent, child in zip(df['Parent'], df['Child']):
        #add function to determine a connction type
        res.append(parent + '---' + child)
    return res

def form_the_graph_schema(nodes, connections):
    MERMAID_CODE = 'graph '
    graph_type = 'LR' + ';'
    graph_nodes = ';'.join(nodes)
    graph_connectons = ';'.join(connections)
    res = MERMAID_CODE + graph_type + str(graph_nodes) +';' + str(graph_connectons)
    return res
    ####
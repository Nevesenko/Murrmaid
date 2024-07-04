import requests

import json

import src.backend.notion_api as nback
import src.cleaning.parsing_database_data as cleaning_data
import draw_mermaid
import excluding_categories

id_text = 'a942b4ba43f744eabf590a485617e466'
id_conn = 'e53476c1606644b7ba9bd12a3e13d61b'


def update_mermaid_graph(id, conn = None):
    res = cur = None
    cur = nback.parse_data(id)
    cur = cleaning_data.get_info(cur)
    cur = excluding_categories.exclude_title_fields(cur, 'properties.Name.title' )
    nodes = draw_mermaid.draw_nodes(cur)
    #####

    conns = nback.parse_data(conn)
    conns = cleaning_data.get_info(conns)
    conns = conns[['properties.Child.relation','properties.Parent.relation']]
    conns = conns.map(lambda x : x[0]['id'])
    conns = conns.rename(columns={'properties.Child.relation' : 'Child', 'properties.Parent.relation': 'Parent'})
    connections = draw_mermaid.draw_graph(conns)
    print(connections)
    final_string = draw_mermaid.form_the_graph_schema(nodes, connections)
    print(final_string)
    body = {  "code": {"rich_text": [{"type": "text","text": {"content": final_string}}],"language": "mermaid"}}
    o = requests.patch('https://api.notion.com/v1/blocks/3214708db6884b5b94d11e5aef0c78b7',
                   headers=nback.headers,
                       json = body)
    print(o)
update_mermaid_graph(id_text, id_conn)
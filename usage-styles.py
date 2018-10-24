import my_dash_component
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import json

app = dash.Dash('')

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True


# Object declaration
default_elements = [
    {
        'data': {'id': 'one', 'label': 'Node 1'},
        'position': {'x': 50, 'y': 50}
    },
    {
        'data': {'id': 'two', 'label': 'Node 2'},
        'position': {'x': 200, 'y': 200}
    },
    {
        'data': {'id': 'three', 'label': 'Node 3'},
        'position': {'x': 100, 'y': 150}
    },
    {
        'data': {'id': 'four', 'label': 'Node 4'},
        'position': {'x': 400, 'y': 50}
    },
    {
        'data': {'id': 'five', 'label': 'Node 5'},
        'position': {'x': 250, 'y': 100}
    },
    {
        'data': {'id': 'six', 'label': 'Node 6', 'parent': 'three'},
        'position': {'x': 150, 'y': 150}
    },

    {'data': {
        'source': 'one',
        'target': 'two',
        'label': 'Edge from Node1 to Node2'
    }},
    {'data': {
        'source': 'one',
        'target': 'five',
        'label': 'Edge from Node 1 to Node 5'
    }},
    {'data': {
        'source': 'two',
        'target': 'four',
        'label': 'Edge from Node 2 to Node 4'
    }},
    {'data': {
        'source': 'three',
        'target': 'five',
        'label': 'Edge from Node 3 to Node 5'
    }},
    {'data': {
        'source': 'three',
        'target': 'two',
        'label': 'Edge from Node 3 to Node 2'
    }},
    {'data': {
        'source': 'four',
        'target': 'four',
        'label': 'Edge from Node 4 to Node 4'
    }},
    {'data': {
        'source': 'four',
        'target': 'six',
        'label': 'Edge from Node 4 to Node 6'
    }},
    {'data': {
        'source': 'five',
        'target': 'one',
        'label': 'Edge from Node 5 to Node 1'
    }},
]

default_stylesheet = [
    {
        "selector": 'node',
        'style': {
            "content": "data(label)",
        }
    },
    {
        "selector": 'edge',
        'style': {
            "curve-style": "bezier",
        }
    },
]

styles = {
    'json-output': {
        'overflow-y': 'scroll',
        'height': 'calc(50% - 25px)',
        'border': 'thin lightgrey solid'
    },
    'tab': {'height': 'calc(98vh - 80px)'}
}

app.layout = html.Div([
    html.Div(className='eight columns', children=[
        my_dash_component.Cytoscape(
            id='cytoscape',
            elements=default_elements,
            layout={
                'name': 'preset'
            },
            style={
                'height': '95vh',
                'width': '100%'
            }
        )
    ]),

    html.Div(className='four columns', children=[
        dcc.Tabs(id='tabs', children=[
            dcc.Tab(label='Tap Objects', children=[
                html.Div(style=styles['tab'], children=[
                    html.P('Node Object JSON:'),
                    html.Pre(
                        id='tap-node-json-output',
                        style=styles['json-output']
                    ),
                    html.P('Edge Object JSON:'),
                    html.Pre(
                        id='tap-edge-json-output',
                        style=styles['json-output']
                    )
                ])
            ]),

            dcc.Tab(label='Tap Data', children=[
                html.Div(style=styles['tab'], children=[
                    html.P('Node Data JSON:'),
                    html.Pre(
                        id='tap-node-data-json-output',
                        style=styles['json-output']
                    ),
                    html.P('Edge Data JSON:'),
                    html.Pre(
                        id='tap-edge-data-json-output',
                        style=styles['json-output']
                    )
                ])
            ]),

            dcc.Tab(label='Mouseover Data', children=[
                html.Div(style=styles['tab'], children=[
                    html.P('Node Data JSON:'),
                    html.Pre(
                        id='mouseover-node-data-json-output',
                        style=styles['json-output']
                    ),
                    html.P('Edge Data JSON:'),
                    html.Pre(
                        id='mouseover-edge-data-json-output',
                        style=styles['json-output']
                    )
                ])
            ]),
            # dcc.Tab(label='Box Data', children=[
            #     html.Div(style=styles['tab'], children=[
            #         html.P('Node Data JSON:'),
            #         html.Pre(
            #             id='box-node-data-json-output',
            #             style=styles['json-output']
            #         ),
            #         html.P('Edge Data JSON:'),
            #         html.Pre(
            #             id='box-edge-data-json-output',
            #             style=styles['json-output']
            #         )
            #     ])
            # ])
        ]),

    ])
])


@app.callback(Output('tap-node-json-output', 'children'),
              [Input('cytoscape', 'tapNode')])
def displayTapNode(data):
    return json.dumps(data, indent=2)


@app.callback(Output('tap-edge-json-output', 'children'),
              [Input('cytoscape', 'tapEdge')])
def displayTapEdge(data):
    return json.dumps(data, indent=2)


@app.callback(Output('tap-node-data-json-output', 'children'),
              [Input('cytoscape', 'tapNodeData')])
def displayTapNodeData(data):
    return json.dumps(data, indent=2)


@app.callback(Output('tap-edge-data-json-output', 'children'),
              [Input('cytoscape', 'tapEdgeData')])
def displayTapEdgeData(data):
    return json.dumps(data, indent=2)


@app.callback(Output('mouseover-node-data-json-output', 'children'),
              [Input('cytoscape', 'mouseoverNodeData')])
def displayMouseoverNodeData(data):
    return json.dumps(data, indent=2)


@app.callback(Output('mouseover-edge-data-json-output', 'children'),
              [Input('cytoscape', 'mouseoverEdgeData')])
def displayMouseoverEdgeData(data):
    return json.dumps(data, indent=2)


# @app.callback(Output('box-node-data-json-output', 'children'),
#               [Input('cytoscape', 'boxNodeData')])
# def displayTapEdge(data):
#     print(data)
#     return json.dumps(data, indent=2)


@app.callback(Output('cytoscape', 'stylesheet'),
              [Input('cytoscape', 'tapNode')])
def generateStylesheet(node):
    if not node:
        return default_stylesheet

    stylesheet = default_stylesheet + [
        {
            "selector": 'node[id = "{}"]'.format(node['data']['id']),
            "style": {
                'background-color': '#FF4136',
                "border-width": 2,
                "border-style": "dotted",
                "border-color": "#FF851B",
                "border-opacity": 1,
                "opacity": 1
            }
        }
    ]

    edges = node['edgesData']

    for edge in edges:
        if edge['source'] == node['data']['id']:
            stylesheet.append({
                "selector": 'node[id = "{}"]'.format(edge['target']),
                "style": {
                    'background-color': 'red',
                    'opacity': 0.9,
                }
            })

            stylesheet.append({
                "selector": 'edge[id= "{}"]'.format(edge['id']),
                "style": {
                    "mid-target-arrow-color": "#FF851B",
                    "mid-target-arrow-shape": "vee",
                    "line-color": "#FF4136",
                    'opacity': 0.9
                }
            })

    return stylesheet


if __name__ == '__main__':
    app.run_server(debug=True)

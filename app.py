# app.py
from dash import Dash, html, dcc
import flask

# Flask server for Azure Functions
server = flask.Flask(__name__)
app = Dash(__name__, server=server, url_base_pathname='/')

app.layout = html.Div([
    html.H1("🚀 Dash app deployed on Azure Functions"),
    html.P("Hello from Sudheer's Azure Function!"),
    dcc.Graph(
        figure={
            'data': [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Sample'}],
            'layout': {'title': 'Simple Bar Chart'}
        }
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)

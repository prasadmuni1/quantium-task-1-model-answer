import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

data = pd.read_csv("output.csv")
data = data.sort_values(by="Date")

app = Dash(__name__)

fig = px.line(
    data,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales"
)

app.layout = html.Div([
    html.H1("Pink Morsel Visualizer"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
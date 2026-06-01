import pandas
from dash import Dash, html, dcc, Input, Output

from plotly.express import line

# the path to the formatted data file
DATA_PATH = "./output.csv"
COLORS = {
    "primary": "#FEDBFF",
    "secondary": "#D598EB",
    "font": "#522A61"
}

# load in data
data = pandas.read_csv(DATA_PATH)
data = data.sort_values(by="Date")

# initialize dash
dash_app = Dash(__name__)


# create the visualization
def generate_figure(chart_data):
    line_chart = line(chart_data, x="Date", y="Sales", title="Pink Morsel Sales")
    line_chart.update_layout(
        plot_bgcolor=COLORS["secondary"],
        paper_bgcolor=COLORS["primary"],
        font_color=COLORS["font"]
    )
    return line_chart


visualization = dcc.Graph(
    id="visualization",
    figure=generate_figure(data)
)

# create the header
header = html.H1(
    "Pink Morsel Visualizer",
    id="header",
    style={
        "background-color": COLORS["secondary"],
        "color": COLORS["font"],
        "border-radius": "20px"
    }
)

# Region picker
Region_picker = dcc.RadioItems(
    ["north", "east", "south", "west", "all"],
    "north",
    id="region_picker",
    inline=True
)
Region_picker_wrapper = html.Div(
    [
        Region_picker
    ],
    style={
        "font-size": "150%"
    }
)


# define the Region picker callback
@dash_app.callback(
    Output(visualization, "figure"),
    Input("region_picker", "value")
)
def update_graph(Region):
    # filter the dataset
    if Region == "all":
        trimmed_data = data
    else:
        trimmed_data = data[data["Region"] == Region]

    # generate a new line chart with the filtered data
    figure = generate_figure(trimmed_data)
    return figure


# define the app layout
dash_app.layout = html.Div(
    [
        header,
        visualization,
        Region_picker_wrapper
    ],
    style={
        "textAlign": "center",
        "background-color": COLORS["primary"],
        "border-radius": "20px"
    }
)

# this is only true if the module is executed as the program entrypoint
if __name__ == '__main__':
    dash_app.run()
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input

# dash helps you initialize your application.
# dash_core_components allows you to create interactive components like graphs, dropdowns, or date ranges.
# dash_html_components lets you access HTML tags.

######################################## 1. Get/transform data ##############################################
# read  the source data
data = pd.read_csv("data/avocado.csv")

# transform data so dash can render them correctly
# the data filter can be removed after we add user interactive data filter
# data = data.query("type == 'conventional' and region == 'Albany'")
# convert string to date
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

######################################## 4. include an external style sheet ###########################################
external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
######################################## 2. Greate an instance of Dash app ############################################
# create an instance of the Dash class. If you’ve used Flask before, then initializing a Dash class may look
# familiar. In Flask, you usually initialize a WSGI application using Flask(__name__). Similarly, for a Dash app,
# you use Dash(__name__).
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

# add a title to your dash app
app.title = "Avocado Analytics: Understand Your Avocados!"

################################### 3. Defining the Layout of Your Dash Application #################################
# This property dictates the look of your app. Below code will:
# 1. build a heading with a description
# 2. build two graphs below the heading.

# note html.Div() takes a list of children. These children are Dash components that are prepackaged in Python libraries.
# Some of them come with Dash when you install it. The rest you have to install separately.
#
# You’ll see two sets of components in almost every app:
# - Dash HTML Components provides you with Python wrappers for HTML elements. For example, you could use this library
#   to create elements such as paragraphs, headings, or lists.
# - Dash Core Components provides you with Python abstractions for creating interactive user interfaces. You can use
#   it to create interactive elements such as graphs, sliders, or dropdowns.
app.layout = html.Div(
    children=[
        # 1st html div for showing the site header
        html.Div(
            children=[
                # add a new component which is the logo
                html.P(children="🥑", className="header-emoji"),
                html.H1(
                    children="Avocado Analytics",
                    # use a css class to customize the style of this header h1
                    className="header-title"
                ),
                html.P(
                    children="Analyze the behavior of avocado prices"
                             " and the number of avocados sold in the US"
                             " between 2015 and 2018",
                    # use a css class to customize the style of this paragraph
                    className="header-description",
                ),
            ],
            # use a css class to customize the style of this header div
            className="header",
        ),
        # 2nd div for the data filtering menu
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Region", className="menu-title"),
                        dcc.Dropdown(
                            id="region-filter",
                            options=[
                                {"label": region, "value": region}
                                for region in np.sort(data.region.unique())
                            ],
                            value="Albany",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(children="Type", className="menu-title"),
                        dcc.Dropdown(
                            id="type-filter",
                            options=[
                                {"label": avocado_type, "value": avocado_type}
                                for avocado_type in data.type.unique()
                            ],
                            value="organic",
                            clearable=False,
                            searchable=False,
                            className="dropdown",
                        ),
                    ],
                ),
                html.Div(
                    children=[
                        html.Div(
                            children="Date Range",
                            className="menu-title"
                        ),
                        dcc.DatePickerRange(
                            id="date-range",
                            min_date_allowed=data.Date.min().date(),
                            max_date_allowed=data.Date.max().date(),
                            start_date=data.Date.min().date(),
                            end_date=data.Date.max().date(),
                        ),
                    ]
                ),
            ],
            className="menu",
        ),
        # 3rd div for the two graphs
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart",
                        config={"displayModeBar": False},
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="volume-chart",
                        config={"displayModeBar": False},
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)


################################5. defining call back functions###########################################
@app.callback(
    #  define the inputs and outputs of the callback
    [Output("price-chart", "figure"), Output("volume-chart", "figure")],
    [
        Input("region-filter", "value"),
        Input("type-filter", "value"),
        Input("date-range", "start_date"),
        Input("date-range", "end_date"),
    ],
)
def update_charts(region, avocado_type, start_date, end_date):
    mask = (
            (data.region == region)
            & (data.type == avocado_type)
            & (data.Date >= start_date)
            & (data.Date <= end_date)
    )
    filtered_data = data.loc[mask, :]
    # print(filtered_data.head())
    price_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["AveragePrice"],
                "type": "lines",
                "hovertemplate": "$%{y:.2f}<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Average Price of Avocados",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"tickprefix": "$", "fixedrange": True},
            "colorway": ["#17B897"],
        },
    }

    volume_chart_figure = {
        "data": [
            {
                "x": filtered_data["Date"],
                "y": filtered_data["Total Volume"],
                "type": "lines",
            },
        ],
        "layout": {
            "title": {"text": "Avocados Sold", "x": 0.05, "xanchor": "left"},
            "xaxis": {"fixedrange": True},
            "yaxis": {"fixedrange": True},
            "colorway": ["#E12D39"],
        },
    }
    return price_chart_figure, volume_chart_figure


if __name__ == "__main__":
    # use the embedded server to run the app, with logging level = debug, multi thread, at port 8050(default)
    app.run_server(debug=True, threaded=True, port=8050)

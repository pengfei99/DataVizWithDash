import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# dash helps you initialize your application.
# dash_core_components allows you to create interactive components like graphs, dropdowns, or date ranges.
# dash_html_components lets you access HTML tags.

######################################## 1. Get/transform data ##############################################
# read  the source data
data = pd.read_csv("data/avocado.csv")

# transform data so dash can render them correctly
data = data.query("type == 'conventional' and region == 'Albany'")
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
app = dash.Dash(__name__)

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
        # 1st html div
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
        # 2nd html div
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart",
                        # You remove the floating bar that Plotly shows by default.
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y": data["AveragePrice"],
                                    "type": "lines",
                                    # set the hover template so that when users hover over a data point, it shows
                                    # the price in dollars. Instead of 2.5, it’ll show as $2.5.
                                    "hovertemplate": "$%{y:.2f}"
                                                     "<extra></extra>",
                                },
                            ],
                            # Define new layout of the graph
                            # adjust the axis, the color of the figure, and the title format.
                            "layout": {
                                "title": {
                                    "text": "Average Price of Avocados",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17B897"],
                            },
                        },
                    ),
                    #  The card class wrap the graph in an html.Div with a "card" class. This will give the graph
                    #  a white background and add a small shadow below it.
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="volume-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y": data["Total Volume"],
                                    "type": "lines",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Avocados Sold",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#E12D39"],
                            },
                        },
                    ),
                    #  The card class wrap the graph in an html.Div with a "card" class. This will give the graph
                    #  a white background and add a small shadow below it.
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)


if __name__ == "__main__":
    # use the embedded server to run the app, with logging level = debug, multi thread, at port 8050(default)
    app.run_server(debug=True, threaded=True, port=8050)

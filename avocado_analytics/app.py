import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# dash helps you initialize your application.
# dash_core_components allows you to create interactive components like graphs, dropdowns, or date ranges.
# dash_html_components lets you access HTML tags.

######################################## 1. Get data ##############################################
# read  the source data
data = pd.read_csv("data/avocado.csv")

# transform data so dash can render them correctly
data = data.query("type == 'conventional' and region == 'Albany'")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

# create an instance of the Dash class. If you’ve used Flask before, then initializing a Dash class may look
# familiar. In Flask, you usually initialize a WSGI application using Flask(__name__). Similarly, for a Dash app,
# you use Dash(__name__).
app = dash.Dash(__name__)

################################### 2. Defining the Layout of Your Dash Application #################################
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
        html.H1(
            children="Avocado Analytics",
        ),
        html.P(
            children="Analyze the behavior of avocado prices"
                     " and the number of avocados sold in the US"
                     " between 2015 and 2018",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["AveragePrice"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Average Price of Avocados"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Total Volume"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Avocados Sold"},
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
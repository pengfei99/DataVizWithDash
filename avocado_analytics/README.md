# Avocado data analytics

This project uses plotly dash to visualize data of avocado. The main logic of the dashboard is located at app.py

We will use multiple version of app.py to illustrate the path of how to build a interactive data viz app.

## 1. First dash app (version 1)
In this version, we start to build a static page. Below is the complete code example

```python
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

######################################## 1. Get data ##############################################
# read  the source data
data = pd.read_csv("data/avocado.csv")

# transform data so dash can render them correctly
data = data.query("type == 'conventional' and region == 'Albany'")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

################################### 2. Create an instance of dash ###############################
app = dash.Dash(__name__)

################################### 3. Defining the Layout of Your Dash Application #################################
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

#################################### 4. run app by using dev server ##################################
if __name__ == "__main__":
    app.run_server(debug=True,threaded=True, port=8050)
```
### 1.1 Step 1. Dependencies
You can notice in below code, we import four libraries

```python
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
```

- dash helps you initialize your application.
- dash_core_components allows you to create interactive components like graphs, dropdowns, or date ranges.
- dash_html_components lets you access HTML tags.

### 1.2 Step 2. Data source
Below code is the basic pandas operations for data ingestion and transformation
```python
# read  the source data
data = pd.read_csv("data/avocado.csv")

# transform data so dash can render them correctly
data = data.query("type == 'conventional' and region == 'Albany'")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)
```
### 1.3 Step 3. Create an instance of dash app
Below code creates an instance of the Dash class. If you’ve used Flask before, then initializing a Dash class may look
familiar. In Flask, you usually initialize a WSGI application using Flask(__name__). Similarly, for a Dash app,
you use Dash(__name__).

```python
app = dash.Dash(__name__)
```

### 1.4 Step 4. Page layout

Below code defines the look of your app. In our case, it will:
1. build a heading with a description
2. build two graphs below the heading.

```python
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
```

Note **html.Div()** takes a list of children. These children are Dash components that are prepackaged in Python libraries.
Some of them come with Dash when you install it. The rest you have to install separately.

You’ll see two sets of components in almost every app:
- Dash HTML Components provides you with Python wrappers for HTML elements. For example, you could use this library
   to create elements such as paragraphs, headings, or lists.
- Dash Core Components provides you with Python abstractions for creating interactive user interfaces. You can use
   it to create interactive elements such as graphs, sliders, or dropdowns.

The first two element in children are **a heading (html.H1) and a paragraph (html.P)**. The dash core will transform
the python code into the following html code

```html
<div>
  <h1>Avocado Analytics</h1>
  <p>
    Analyze the behavior of avocado prices and the number
    of avocados sold in the US between 2015 and 2018
  </p>
  <!-- Rest of the app -->
</div>
```
The last tow element in children are two **dcc.Graph** components. 
- The first one plots the average prices of avocados during the period of study
  
- The second one plots the number of avocados sold in the United States during the same period.


### 1.5 Step 5 run the app 
Below code use the embedded server to run the dash app, with logging level = debug, multi thread, at port 8050(default)
```python
if __name__ == "__main__":
    app.run_server(debug=True,threaded=True, port=8050)
```

You need to run the app.py within the poetry virtual env. 
```shell
poetry run python avocado_analytics/app.py
```

Now you should be able to see the app via **http://127.0.0.1:8050/**

## 2. Make it look nicer (Version 2) 

Dash provides you with a lot of flexibility to customize the look of your application. You can use your own CSS or 
JavaScript files, set a favicon (small icon shown on the web browser), and embed images, among other advanced options.

### 2.1 Apply a Custom Style to Your Components

You can style components in two ways:

- Using the style argument of individual components
- Providing an external CSS file

#### 2.1.1 Using the style argument 
Using the style argument to customize your dashboard is straightforward. This argument takes a Python dictionary 
with key-value pairs consisting of the names of CSS properties, and the values you want to set.

For example if you want to change the color and font of the heading you can add a line style

```python
html.H1(
    children="Avocado Analytics",
    style={"fontSize": "48px", "color": "red"},
),
```

The downside of using the style argument is that it does not scale well as your codebase grows. If your dashboard has 
multiple components that you want to look the same, then you’ll end up repeating a lot of your code. 

The better solution is to use a custom CSS file (with javascript/typescript).

#### 2.1.2 Use custom css file

You need to do two things, if you want to include your own local CSS or JavaScript files. 
1. Create a folder called **assets/** in the root directory of your project, then save the style files (e.g. .css) that
   you want to add there.
   
2. In the app.py, for each dash component that you want to customize, use the className or id arguments to specify
the class or id in your custom css

**By default, Dash automatically serves any file included in assets/**. This will also work for adding a favicon or 
embedding images. As a result, you don't need to specify how dash can find the style files

For more information, please read the [class](https://www.w3schools.com/html/html_classes.asp) 
and [id](https://www.w3schools.com/html/html_id.asp) of html/css.

##### Below is an example:

If you wanted to adjust the font size and text color of the H1 element in app.py, 
1. Add following css styple code in assets/style.css 
```css
.header-title {
  font-size: 48px;
  color: red;
}
```
   
2. Add className argument in the header declaration. Below code uses a class selector to format the heading in 
   your CSS file. This selector will adjust the heading format.
```python
html.H1(
    children="Avocado Analytics",
    className="header-title",
),
```

**Note with this approach, you can reuse the style for any number of the dash component as long as you want these components to have the same style**
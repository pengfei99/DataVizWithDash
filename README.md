# DataVizWithDash


## 1. Introduction of data viz and dashboard

### 1.1 Why we need data viz?

Data analytics is all about finding insights and causing business strategy and operations decisions. 
While the most challenging part is finding new insights, the most important part is packaging these insights into 
something that is **consumable, reproducible, and update-able and that tracks the effects of change**.

Enter Dashboards, a (usually) interactive collection of visualizations that have a live connection to the data, 
and update over time. With the explosion in Data Science/Analytics as a field, so has there been an explosion in 
Dashboard products and tools, including ones that wouldn’t traditionally be thought of as dashboards.

### 1.2 Existing tools
We can divide the existing tools into four categories:

- Business Intelligence (No/Low Code) Tools — Microsoft Power BI, Tableau, Looker
- Hosted Notebook Dashboard Apps — Deepnote Dashboard, Hex Data Apps
- Front-end to SQL with automated plotting — Redash, Deepnote, Hex, Databricks etc.
- Python web apps — Plotly Dash, Streamlit


Read this [article](https://towardsdatascience.com/data-visualization-in-2021-an-overview-of-dashboarding-technology-in-the-age-of-big-data-79d490beffcf)
to understand the difference between these tools. It gives you advice on when to use them and in which situation one tool
is better than the others.


## 2. About this repo

In this repo, we will try to use **Plotly Dash** to build a data dashboard.

https://realpython.com/python-dash/#how-to-apply-a-custom-style-to-your-components

https://towardsdatascience.com/create-a-professional-dasbhoard-with-dash-and-css-bootstrap-e1829e238fc5

### 2.1 Introduction of Plotly Dash

Dash is an open source framework for building data visualization interfaces. Released in 2017 as a Python library, 
it’s grown to include implementations for R and Julia. Dash helps data scientists build analytical web applications 
without requiring advanced web development knowledge.

Three technologies constitute the core of Dash:

- Flask supplies the web server functionality.
- React.js renders the user interface of the web page.
- Plotly.js generates the charts used in your application.

Dash will help you build dashboards quickly. If you’re used to analyzing data or building data visualizations using 
Python, then Dash will be a useful addition to your toolbox. Here are a few examples of what you can make with Dash:

- [A dashboard to analyze trading positions in real-time](https://dash-gallery.plotly.host/dash-web-trader/)
- [A visualization of millions of Uber rides](https://dash-gallery.plotly.host/dash-uber-rides-demo/)
- [An interactive financial report](https://dash-gallery.plotly.host/dash-financial-report/)
- [Bank custom complain nlp](https://dash.gallery/dash-nlp/)

For more examples, you can visit the official [gallery](https://dash-gallery.plotly.host/Portal/)

### 2.2 Setup environment
There are many ways to set up a python dev environment, here I will use poetry
```shell
mkdir "DataVizWithDash"
poetry init
# follow the instruction to finish the project and virtual env set up

# add dependencies to the project
poetry add dash 

poetry add pandas
```

### 2.3 Build a Dash Application
For development purposes, it’s useful to think of the process of building a Dash application in two steps:

- Define the looks of your application using the app’s layout.
- Use callbacks to determine which parts of your app are interactive and what they react to.

The [avocado analytics](avocado_analytics/README.md) shows a simple example
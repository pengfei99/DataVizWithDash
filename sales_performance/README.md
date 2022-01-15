# Sales performance analytics

In the avocado analytic project, we have learned how to create a single page dashboard. In this project, we will develop
a multi-page dashboard.
Origin link:

https://towardsdatascience.com/create-a-professional-dasbhoard-with-dash-and-css-bootstrap-e1829e238fc5#059c

This tutorial will cover :

1. Setup project structure for multi-page

## 1. Setup project structure

Dash provides an official [doc](https://dash.plotly.com/urls) on how to set up project structure. Dash propose two types
of project structure:

1. app logic centric
2. code categories centric

### 1.1 App logic centric

In this type of project structure, we group code by the app logic. For example, below structure is an example

```text
- app.py
- index.py
- apps
   |-- __init__.py
   |-- app1.py
   |-- app2.py
- assets
- data
```

- app.py : it defines the app variables that are needed by Flask to run the app.
- index.py : it defines the mapping between the URLs and different app pages(i.e. an app page contains data viz html
  layouts, callbacks for handling user interaction, etc).

- apps: is a folder that contains all the app pages. (As the structure is app centric, we mix all the code types for
  this app in a single app1.py file)

- assets: is a folder that contains all additional web content files such as: images; favorite icon, .css files
- data: is a folder that contains the underlying data of the dashboard, it can be omitted if you call an api or database

### 1.2 Code categories centric

In this type of project structure, we group code by the type of code. For example, below structure is an example

```text
- app.py
- callbacks.py
- layouts.py
- index.py
- assets
- data
```
You can notice we don't separate code by apps, we separate them by the type of code. 

- layouts.py : it defines all pages html layouts. You can put repeated components (like the header, or the navbar) 
  in a function, when you need them just call the function, this can avoid many code repetitions. 
  
- callbacks.py : it defines all callbacks that define the user interactions with the graphs.

The rest is the same.

## 2. Use css javascript framework to make your dashboard nicer

A .css file define the properties (fonts properties, sizes, colors, backgrounds, …) of html components. As Dash uses
html components to visualize data, we need to add custom .css file to make your dashboard unique.

As we mentioned before, dash will read css style from the .css files stored in the “assets” folder. So you just put
the bootstrap style .css file in assets, then you can call different bootstrap style.

### 
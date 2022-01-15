import dash

app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server
# add a title to your dash app
app.title = "Sales performance: Understand Your business!"

# Note the app.py is no longer the entry point of the app. It's the index.py
# try to use python index.py to run the app

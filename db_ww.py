import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

data = pd.read_csv("gen_data.csv")

precip = data.precip
dt = data.time
res_level  =  data.res_level
res_level_pos = data.res_level+0.1*data.res_level
res_level_neg = data.res_level-0.1*data.res_level


# data = data.query("type == 'conventional' and region == 'Albany'")
# data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
# data.sort_values("Date", inplace=True)

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Water Watch: Understand Your Reservoirs!"

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="🥑", className="header-emoji"),
                html.H1(
                    children="Watch Water", className="header-title"
                ),
                html.P(
                    children="Analyze the different reservoirs "
                    " Water Level and Water Volume"
                    " between 2011 and 2020",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": dt,
                                    "y": res_level,
                                    "type": "lines",
                                    "color": ["#E12D39"],
                                    "hovertemplate": "$%{y:.2f}"
                                                     "<extra></extra>",
                                },
                                {   
                                    "x": dt,
                                    "y": res_level_pos,
                                    "type": "lines",
                                    "hovertemplate": "$%{y:.2f}"
                                                     "<extra></extra>",
                                },
                                {   
                                    "x": dt,
                                    "y": res_level_neg,
                                    "type": "lines",
                                    "hovertemplate": "$%{y:.2f}"
                                                     "<extra></extra>",
                                },
                            ],
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
                                #"colorway": ["#17B897"],
                            },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="volume-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": dt,
                                    "y": precip,
                                    "type": "bar",
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
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
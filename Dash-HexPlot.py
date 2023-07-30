import pandas as pd
import plotly.graph_objs as go
import plotly.colors as pc
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import numpy as np

# Create a DataFrame with random data
df = pd.DataFrame(np.random.randn(500, 4), columns=['mon', 'tues', 'wed', 'thurs'])

# Create a Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Hexbin Plot"),
    html.Label("Hexagon Radius"),
    dcc.Slider(
        id='gridsize-slider',
        min=0,
        max=100,
        value=15,
        marks={i: str(i) for i in range(0, 101, 10)},  # Marks from 0 to 100 with steps of 10
        step=1
    ),
    html.Label("Color Map"),
    dcc.Dropdown(
        id='color-dropdown',
        options=[{'label': cmap, 'value': cmap} for cmap in pc.PLOTLY_SCALES],
        value='YlGnBu'
    ),
    dcc.Graph(id='hexbin-plot')
])

# Define the callback to update the hexbin plot
@app.callback(
    Output('hexbin-plot', 'figure'),
    [Input('gridsize-slider', 'value'),
     Input('color-dropdown', 'value')]
)
def update_plot(gridsize, color_map):
    # Calculate bin size dynamically based on the range of data and desired number of bins
    x_bins = np.linspace(df['mon'].min(), df['mon'].max(), gridsize + 1)
    y_bins = np.linspace(df['thurs'].min(), df['thurs'].max(), gridsize + 1)

    # Create 2D histogram with hexagonal bins
    hist2d, _, _ = np.histogram2d(df['mon'], df['thurs'], bins=[x_bins, y_bins])
    bins_text = [[str(int(hist)) for hist in col] for col in hist2d]

    # Create scatter plot with hexagonal markers
    hexplot = go.Scatter(
        x=df['mon'],
        y=df['thurs'],
        mode='markers',
        marker=dict(
            symbol='hexagon',
            size=gridsize,
            sizemode='diameter',  # Use diameter to control hexagon size
            sizemin=5,
            opacity=0.7,
            line=dict(width=1),
            colorscale=color_map,
            colorbar=dict(title='Count')
        ),
        text=bins_text,
        hoverinfo='text'
    )

    layout = go.Layout(
        title='Hexbin Plot',
        xaxis=dict(title='x'),
        yaxis=dict(title='y')
    )

    return {'data': [hexplot], 'layout': layout}


# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

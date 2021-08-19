import plotly.express as px
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#%%---------------------Basic scatter----------------------------
x = np.arange(0, 6)
y = np.arange(2, 8)

fig = px.scatter(x, y)
fig.show()

# dataframe:
df = px.data.iris()
df['e'] = df['sepal_width']/100
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species', symbol='species', error_x='e')
fig.show()

# categorical axes
df = px.data.medals_long()

fig = px.scatter(df, y='nation', x='count', color='medal', symbol='medal')
fig.update_traces(marker_size=10)
fig.show()


#%% ---------------------------subplots:----------------------------
N = 20
x = np.linspace(0, 1, N)

fig = make_subplots(1, 3)
for i in range(1, 4):
    fig.add_trace(go.Scatter(x=x, y=np.random.random(N)), 1, i)
fig.update_xaxes(matches='x')
fig.show()


#%%------------------------write to file:-------------------------------
dir_plt = r'C:\Users\selta\Desktop'
# unit in inch: 300*in, scale control dpi. 1 = 300 dpi
fig.write_image(dir_plt+'/test.png', width=6*300, height=4*300, scale=2)

#%%---------------------------- color scale: ----------------------------
np.random.seed(1)
N = 100
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sz = np.random.rand(N) * 30

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode="markers",
    marker=go.scatter.Marker(
        size=sz,
        color=colors,
        opacity=0.6,
        colorscale="Viridis"
    )
))

fig.show()

#%%-------------------- LaTeX : https://plotly.com/python/LaTeX/ --------------------
c = 2

# note: if using format string, single {} needs to be converted to {{}}
fig = px.line(x, y, title=r'$\alpha_\text{{{}}} = 20 \pm 11\text{{ km s}}^{{-1}}$'.format(c))
fig.update_layout(
    xaxis_title=r'$\sqrt{(n_\text{c}(t|{T_\text{early}}))}$',
    yaxis_title=r'$d, r \text{ (solar radius)}$'
)
fig.show()

#%% ---------------------- bubble scatter:-------------------------------------
fig = go.Figure()
fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[10, 11, 12, 13],
                                mode='markers',
                                marker=dict(size=[40, 60, 80, 100],
                                            color=[0, 1, 2, 3],
                                            showscale=True)
                                ))

fig.show()

#%%---------------------- sunburst plot-----------------------------------------
df = px.data.gapminder().query("year == 2007")
fig = px.sunburst(df, path=['continent', 'country'], values='pop',
                  color='lifeExp', hover_data=['iso_alpha'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']))
# fig.show()
# if use go:
fig2 = go.Figure(go.Sunburst(labels=fig['data'][0]['labels'].tolist(), parents=fig['data'][0]['parents'].tolist(), values=fig['data'][0]['values'].tolist()))
# fig.add_trace()
fig2.show()
#%%------------------ plot img -----------------------------------

img = np.random.randn(100).reshape((10, 10))
fig = make_subplots(1, 2, column_widths=[0.7, 0.3])
# We use go.Image because subplots require traces, whereas px functions return a figure
fig.add_trace(go.Heatmap(z=img), 1, 1)
fig.add_trace(go.Histogram(x=img.flatten()), 1, 2)
fig.update_layout(height=400)
fig.show()
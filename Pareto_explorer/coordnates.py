import plotly.graph_objects as go
import numpy as np
import ipywidgets as widgets
from IPython.display import display
from plotly.graph_objs import FigureWidget
import numpy as np

class coordnates:

 def configure(self, idx = None):
  if idx is not None:
    pop = exp.pop().variables
    var = np.array([pop[idx-i]   for i in range(0,10)   ]  )

    arr = [
    dict(
        label=f'X{b+1}',
        values=var[:, b],
        range=[0, 1]
    )
    for b in range(var.shape[1])
]
    #arr = [ dict(label = f'X{b+1}', values = np.array(var[:,b])  , range = [np.min(pop[:,b]),np.max(pop[:,b])   ]) for b in range(0,var.shape[1])]
    colors = np.zeros(var.shape[0])
    colors[0]=1
  fig = go.Figure()

  fig.add_trace(

   go.Parcoords(
        line = dict(

          color = colors,
          colorscale=[
        [0.0, 'lightgray'],
        [0.99, 'lightgray'],
        [1.0, 'red']
    ]
        ),
        dimensions=arr
    ))
  fig.update_layout(

                     width = 1300,
                     height=700,
                     title=dict(
                     text=f'Decision variables for solution {idx}',
                     x=0.5,
                     xanchor='center',
                     y=0.9,
                     yanchor='bottom',
                     pad=dict(t=0),
                     font=dict(size=16,weight='bold')
                 ),
            margin=dict(l=30,r=30,b=0,t=180)
  )
  return fig
from dash import Dash, html, dcc, Input, Output
import threading
from google.colab.output import eval_js
from .plot_3D import plot_3D
from .coordnates import coordnates


class dashboard:

 def __init__(self,rank,idx_rank):
    self.rank = rank
    self.idx_rank = idx_rank
    self.plot = plot_3D(exp,[0,1,2])
    self.coordenate = coordnates()
    self.app = Dash(__name__)
    self.fig = self.plot.configure(rank,idx_rank)
    self.register_callback()



 def execute(self, rank_version = 1):

  thread = threading.Thread(target=self.run, daemon=True)
  thread.start()
  url = eval_js("google.colab.kernel.proxyPort(8050)")
  print(url)


 def build(self):
    self.app.layout = html.Div(
    [
        dcc.Store(
           id='rank_version',
           data = 0
        ),
        dcc.Graph(
            id ='paret',
            figure = self.fig
        ),
        dcc.Graph(
            id ='coordenate',
            figure = go.Figure()
        )
    ], style={
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'center'
    }
     )


 def run(self):
    self.app.run(
        host='0.0.0.0',
        port=8050,
        debug=False,
        use_reloader=False
    )


 def register_callback(self):

  self.build()

  @self.app.callback(Output('paret','figure'),
              Input('rank_version','data'),
            prevent_initial_call=True)

  def update_pareto(_):
   plot = plot_3D(exp,[0,1,2])

   return plot.configure(self.rank,self.idx_rank)



  @self.app.callback(Output('coordenate','figure'),
              Input('paret','clickData'),
            prevent_initial_call=True)

  def click_ponto(clickData):

   if clickData is None:
    return go.Figure()



   return self.coordenate.configure(clickData['points'][0]['customdata'])
from .dominance import dominance
from .dashboard import dashboard

class explorer:

  def __init__(self,population):
    self.population = population

  def executing(self):

    pareto = dominance()
    ranks = pareto.rank_pareto(self.population)
    idx_rank = list(dict.fromkeys(pareto.idx_rank(self.population,ranks)))
    idx_aux = pareto.associate_rank(ranks,idx_rank)
    db = dashboard(ranks,idx_aux)
    db.execute()
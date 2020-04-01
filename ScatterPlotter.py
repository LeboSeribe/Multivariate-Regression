from Plotter import Plotter
import seaborn as sns
import matplotlib.pyplot as plt
class ScatterPlotter(Plotter):
    def __init__(self,y,y_prediction,residual = None):
        super().__init__(y,y_prediction)
        self.residual = residual
    
    def plot(self):
        if self.residual is None:
            self.residual = self.run_calculations() 
        plt.scatter(self.y_predict,self.residual)
    
        
        
